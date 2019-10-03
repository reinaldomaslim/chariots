"""Capacited Vehicles Routing Problem (CVRP)."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from datetime import datetime
from gmplot import gmplot
import urllib
import json
import numpy as np 
import googlemaps
from dotenv import load_dotenv
import os
import osrm


load_dotenv()
api = os.getenv("API")

depot = '-0.068372,109.362745'
gmaps = googlemaps.Client(key=api)
# colors = ['r', 'maroon', 'darkorange','orange', 'yellow', 'green', 'seagreen', 'blue']

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'maroon', 'olive', 'teal', 'orange', 'lime', 'cyan', 'magenta', 'mint', 'navy']


def decode_polyline(polyline_str):
    index, lat, lng = 0, 0, 0
    coordinates = []
    changes = {'latitude': 0, 'longitude': 0}

    # Coordinates have variable length when encoded, so just keep
    # track of whether we've hit the end of the string. In each
    # while loop iteration, a single coordinate is decoded.
    while index < len(polyline_str):
        # Gather lat/lon changes, store them in a dictionary to apply them later
        for unit in ['latitude', 'longitude']: 
            shift, result = 0, 0

            while True:
                byte = ord(polyline_str[index]) - 63
                index+=1
                result |= (byte & 0x1f) << shift
                shift += 5
                if not byte >= 0x20:
                    break

            if (result & 1):
                changes[unit] = ~(result >> 1)
            else:
                changes[unit] = (result >> 1)

        lat += changes['latitude']
        lng += changes['longitude']

        coordinates.append([lat / 100000.0, lng / 100000.0])

    return coordinates

def send_request(origin_addresses, dest_addresses, api):
    """ Build and send request for the given origin and destination addresses."""
    def build_address_str(addresses):
        # Build a pipe-separated string of addresses
        address_str = ''
        for i in range(len(addresses) - 1):
            address_str += addresses[i] + '|'
        address_str += addresses[-1]
        return address_str

    request = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
    origin_address_str = build_address_str(origin_addresses)
    dest_address_str = build_address_str(dest_addresses)
    request = request + '&origins=' + origin_address_str + '&destinations=' + \
                       dest_address_str + '&key=' + api
    jsonResult = urllib.request.urlopen(request).read().decode("utf-8")
    response = json.loads(jsonResult)
    return response

def build_distance_matrix(response):
    distance_matrix = []
    for row in response['rows']:
        row_list = [row['elements'][j]['distance']['value'] for j in range(len(row['elements']))]
        distance_matrix.append(row_list)
    return distance_matrix

def create_distance_matrix(data, mode = 'utm'):
    addresses = data["addresses"]

    if mode == 'real':    
        # Distance Matrix API only accepts 100 elements per request, so get rows in multiple requests.
        max_elements = 100
        num_addresses = len(addresses) # 16 in this example.
        # Maximum number of rows that can be computed per request (6 in this example).
        max_rows = max_elements // num_addresses
        # num_addresses = q * max_rows + r (q = 2 and r = 4 in this example).
        q, r = divmod(num_addresses, max_rows)
        dest_addresses = addresses
        distance_matrix = []
        # Send q requests, returning max_rows rows per request.
        for i in range(q):
            origin_addresses = addresses[i * max_rows: (i + 1) * max_rows]
            
            response = send_request(origin_addresses, dest_addresses, api)
            distance_matrix += build_distance_matrix(response)

        # Get the remaining remaining r rows, if necessary.
        if r > 0:
            origin_addresses = addresses[q * max_rows: q * max_rows + r]
            response = send_request(origin_addresses, dest_addresses, api)
            distance_matrix += build_distance_matrix(response)

    elif mode == 'utm':
        
        distance_matrix = np.zeros((len(addresses), len(addresses)))
        for i in range(len(addresses)):
            for j in range(i+1, len(addresses)):
                dist = utm_dist(addresses[i], addresses[j])
                distance_matrix[i][j] = dist
                distance_matrix[j][i] = dist

    # else:
    print(addresses)

    print(distance_matrix)

    return distance_matrix

def utm_dist(add1, add2):
    R = 6373.0
    lat1 = np.radians(float(add1.split(',')[0]))
    lon1 = np.radians(float(add1.split(',')[1]))
    lat2 = np.radians(float(add2.split(',')[0]))
    lon2 = np.radians(float(add2.split(',')[1]))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    distance = int(R * c * 1000)

    return distance    



def str2ll(str_coord):

    lat = float(str_coord.split(',')[0])
    lon = float(str_coord.split(',')[1])
    return [lat, lon]

def print_solution(data, manager, routing, assignment):
    """Prints assignment on console."""

    html_name = './app/templates/res.html'
    depot_latlon = str2ll(depot)
    gmap = gmplot.GoogleMapPlotter(depot_latlon[0], depot_latlon[1], 15, api)

    total_distance = 0
    total_load = 0

    routes = []
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load = 0

        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            plan_output += ' {0} Load({1}) -> '.format(node_index, route_load)

            route.append(node_index)
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        route.append(0)

        plan_output += ' {0} Load({1})\n'.format(manager.IndexToNode(index),
                                                 route_load)
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        plan_output += 'Load of the route: {}\n'.format(route_load)
        print(plan_output)

        total_distance += route_distance
        total_load += route_load
        routes.append([route, route_distance, route_load])
        
    #     coordinates = []
    #     for i in range(len(route)-1):
    #         src = data['addresses'][route[i]]
    #         dst = data['addresses'][route[i+1]]
            
    #         latlon = str2ll(src)
    #         if route[i] == 0:
    #             color = 'pink'
    #         else:
    #             color = colors[vehicle_id%len(colors)]

    #         gmap.marker(latlon[0], latlon[1], color)
            
    #         now = datetime.now()
    #         directions_result = gmaps.directions(src,
    #                                             dst,
    #                                             mode="driving",
    #                                             departure_time=now)[0]
            
    #         polyline = directions_result['overview_polyline']['points']
    #         coordinates = np.asarray(decode_polyline(polyline))
    #         gmap.plot(coordinates[:, 0], coordinates[:, 1], colors[vehicle_id%len(colors)], edge_width=2)
        

        
    # if gmap is not None:
    #     #save plot as html
    #     gmap.draw(html_name)

    print('Total distance of all routes: {}m'.format(total_distance))
    print('Total load of all routes: {}'.format(total_load))

    return routes

    #draw html for this
def solve_cvrp(data):

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if assignment:
        paths = print_solution(data, manager, routing, assignment)
    return paths


def create_data_model():
    """Stores the data for the problem."""
    data = {}

    data['addresses'] = ['-0.068372,109.362745']
    data['demands'] = [0]
    data['depot'] = 0    
    data['vehicle_capacities'] = []

    orders = Order.query.all()
    for u in orders:
        data['addresses'].append(u.latlon)
        data['demands'].append(int(u.load))

    vehicles = Vehicle.query.all()
    for u in vehicles:
        data['vehicle_capacities'].append(int(u.capacity))

    data['num_vehicles'] = len(vehicles)

    data['distance_matrix'] = create_distance_matrix(data)

    print(len(data['addresses']))
    print(data['demands'])

    return data



def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model()
    solve_cvrp(data)


if __name__ == '__main__':
    main()