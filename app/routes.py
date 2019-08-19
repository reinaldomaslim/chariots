from app import app
from app import db
from app.models import Order, Vehicle
from app.forms import OrderForm, VehicleForm
from flask import render_template, flash, redirect, url_for, request
from cvrp import *
import time
paths = []

@app.route('/')
@app.route('/index')
def index():
    orders = Order.query.all()
    vehicles = Vehicle.query.all()

    return render_template("index.html", title='Home Page', orders=orders, vehicles=vehicles)
    
@app.route('/compute', methods=['GET', 'POST'])
def compute():
    global paths
    if len(paths) == 0:
        data = create_data_model()
        paths = solve_cvrp(data)
        time.sleep(1)
    return render_template("compute.html", title='Result', paths=paths)

@app.route('/result')
def result():
    return render_template("res.html", title='Result')

@app.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm()
    
    if form.validate_on_submit():
        order = Order(address=form.address.data, load=form.load.data)
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

    data['addresses'] = ['-0.068372,109.362745']
    data['demands'] = [0]
    data['depot'] = 0    
    data['vehicle_capacities'] = []

    orders = Order.query.all()
    for u in orders:
        data['addresses'].append(u.address)
        data['demands'].append(int(u.load))

    vehicles = Vehicle.query.all()
    for u in vehicles:
        data['vehicle_capacities'].append(int(u.capacity))

    data['num_vehicles'] = len(vehicles)

    data['distance_matrix'] = create_distance_matrix(data)

    print(len(data['addresses']))
    print(data['demands'])

    return data
