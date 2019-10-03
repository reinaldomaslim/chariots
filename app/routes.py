from app import app
from app import db
from app.models import Order, Vehicle
from app.forms import OrderForm, VehicleForm
from flask import render_template, flash, redirect, url_for, request
from cvrp import *
import time
import json


path_data = []
depot = '-0.068372,109.362745'

@app.route('/')
@app.route('/index')
def index():
    orders = Order.query.all()
    vehicles = Vehicle.query.all()
    return render_template("index.html", title='Home Page', orders=orders, vehicles=vehicles)
    

@app.route('/delete_order', methods=['POST'])
def delete_order():
    print(request.form.get('status'))
    Order.query.filter_by(id=request.form.get('delete_order')).delete()
    db.session.commit()
    orders = Order.query.all()
    vehicles = Vehicle.query.all()
    return render_template("index.html", title='Home Page', orders=orders, vehicles=vehicles)
    

@app.route('/delete_vehicle', methods=['POST'])
def delete_vehicle():
    Vehicle.query.filter_by(id=request.form.get('delete_vehicle')).delete()
    db.session.commit()
    orders = Order.query.all()
    vehicles = Vehicle.query.all()
    return render_template("index.html", title='Home Page', orders=orders, vehicles=vehicles)
    

@app.route('/compute', methods=['GET', 'POST'])
def compute():
    global path_data

    data = create_data_model()
    routes = solve_cvrp(data)
    time.sleep(1)

    orders = Order.query.all()
    vehicles = Vehicle.query.all()

    paths = []

    path_data = []
    for i in range(len(routes)):
        
        path = []
        lat_lng = []

        vehicle = vehicles[i]
        path.append(vehicle.vehiclename+' : ')
        route = routes[i][0]
        total_dist = int(routes[i][1]/1000)
        total_load = routes[i][2]
        

        for j in range(1, len(route)):


            if j == 1:
                src = depot
            else:
                src = orders[route[j-1]-1].latlon

            if j == len(route)-1:
                dst = depot
            else:
                dst = orders[route[j]-1].latlon

                order = orders[route[j]-1]
                order.vehicle_id = vehicle.id
                address = order.address.split(',')[0]
                path.append(address)


                if j < len(route)-2:
                    path.append(' > ')

            now = datetime.now()
            directions_result = gmaps.directions(src,
                                                dst,
                                                mode="driving",
                                                departure_time=now)[0]
            
            polyline = directions_result['overview_polyline']['points']
            coordinates = np.asarray(decode_polyline(polyline))

            lat_lng.extend(coordinates.tolist())


        path.append(' | distance: '+str(total_dist)+' km')
        path.append(' | load: '+str(total_load))
        path = ''.join(path)
        paths.append(path)

        path_data.append(lat_lng)


    return render_template("compute.html", title='Compute', paths=paths)

@app.route('/result')
def result():
    global path_data

    orders = Order.query.all()
    orders_data = [[float(depot.split(',')[0]), float(depot.split(',')[1])]]

    for order in orders:
        latlon = order.latlon.split(',')
        orders_data.append([float(latlon[0]), float(latlon[1])])        

    return render_template("res.html", title='Map', path_data = json.dumps(path_data), orders_data = json.dumps(orders_data))

@app.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm()
    
    if form.validate_on_submit():

        address = request.form.get('autocomplete')
        
        geocode_result = gmaps.geocode(address)[0]['geometry']['location']
        latlon = str(geocode_result['lat'])+','+str(geocode_result['lng'])
        
        order = Order(address = address, latlon=latlon, load=form.load.data)
        db.session.add(order)
        db.session.commit()
        flash('order added')

        return redirect(url_for('index'))

    return render_template('order.html', title='Orders', form=form)

@app.route('/vehicle', methods=['GET', 'POST'])
def vehicle():
    form = VehicleForm()
    
    if form.validate_on_submit():
        vehicle = Vehicle(vehiclename=form.vehiclename.data, capacity=form.capacity.data)
        db.session.add(vehicle)
        db.session.commit()

        flash('vehicle added')
        return redirect(url_for('index'))

    return render_template('vehicle.html', title='Vehicles', form=form)





def create_data_model():
    """Stores the data for the problem."""
    data = {}

    data['addresses'] = [depot]
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
