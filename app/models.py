from app import db
from datetime import datetime


class Vehicle(db.Model):
    #id is primary key, unique id value
    id = db.Column(db.Integer, primary_key=True)
    vehiclename = db.Column(db.String(10), index=True, unique=True)
    capacity = db.Column(db.Float)
    orders = db.relationship('Order', backref='vehicle', lazy='dynamic')

    def __repr__(self):
        return '<Vehicle {}>'.format(self.vehiclename)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(140))
    latlon = db.Column(db.String(140))
    load = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    #user_id relates order to vehicle.driver
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def __repr__(self):
        return '<Order {}>'.format(self.address)
