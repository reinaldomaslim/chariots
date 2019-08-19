from app import app, db
from app.models import Order, Vehicle
from werkzeug.security import generate_password_hash, check_password_hash
import numpy as np 
#debugging tool, set FLASK_APP=erp.py
# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Post': Post}

# u = User(username='John', email='john@example.com')
# db.session.add(u)
# db.session.commit()

# u = User(username='Sasha', email='sasha@example.com')
# db.session.add(u)
# db.session.commit()

# users = User.query.all()
# for u in users:
#     print(u.id, u.username)

# p = Post(body='my first post!', author=users[1])
# db.session.add(p)
# db.session.commit()

# posts = Post.query.all()
# for p in posts:
#     print(p.id, p.author.username, p.body)

# print(User.query.order_by(User.username.desc()).all())

#delete everything
orders = Order.query.all()
for u in orders:
    print(u.id, u.address, u.load, u.timestamp, u.vehicle_id)
    db.session.delete(u)

vehicles = Vehicle.query.all()
for v in vehicles:
    print(v.id, v.vehiclename, v.capacity)
    db.session.delete(v)

db.session.commit()



depot = '-0.068372,109.362745'
f = open('./data/destinations.txt', 'r')
lines = f.readlines()
loads = np.random.randint(5, 12, len(lines))
for i in range(len(lines)):
    line = lines[i]
    latlon = line.split()
    address = latlon[0]+latlon[1]
    load = loads[i]
    order = Order(address=address, load=load)
    db.session.add(order)
    db.session.commit()
        

caps = [45, 40, 45, 50]
for i in range(len(caps)):
    vehicle = Vehicle(vehiclename='veh_'+str(i), capacity=caps[i])
    db.session.add(vehicle)
    db.session.commit()

# hash_pass = generate_password_hash('foobar')
# print(hash_pass)

# login = check_password_hash(hash_pass, 'foobar')
# print(login)
# login = check_password_hash(hash_pass, 'blobsie')
# print(login)