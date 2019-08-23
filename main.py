from flask import Flask
from app import app, db
from app.models import Order, Vehicle

###############################################
if __name__ == "__main__":
    app.run(debug=True)