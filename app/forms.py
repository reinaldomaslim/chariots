from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import Order, Vehicle

class OrderForm(FlaskForm):
    #currently string of 'lat,lon'
    # address = StringField('Address', validators=[DataRequired()])
    load = FloatField('Load', validators=[DataRequired()])
    submit = SubmitField('Submit')

class VehicleForm(FlaskForm):
    vehiclename = StringField('Plate Number', validators=[DataRequired()])
    capacity = FloatField('Capacity', validators=[DataRequired()])
    submit = SubmitField('Submit')

