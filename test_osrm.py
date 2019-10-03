import osrm

osrm.RequestConfig.host = "router.project-osrm.org"

list_coord = [[21.0566163803209, 42.004088575972],
            [21.3856064050746, 42.0094518118189],
            [20.9574645547597, 41.5286973392856],
            [21.1477394809847, 41.0691482795275],
            [21.5506463080973, 41.3532256406286]]

list_id = ['name1', 'name2', 'name3', 'name4', 'name5']

time_matrix, snapped_coords = osrm.table(list_coord,
                                          ids_origin=list_id,
                                          output='dataframe')

print(time_matrix)
