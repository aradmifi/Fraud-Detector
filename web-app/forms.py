from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField, TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
   ID_Txn = IntegerField('ID')
   Hora_Txn = StringField('Hora')
   Sexo = StringField('Sexo')
   Edo_Civil = StringField('Estado Civil')
   Hijos = StringField('Hijos')
   Monto_Txn = IntegerField('Monto')
   Establecimiento = StringField('Establecimiento')
   Tipo_Compra = StringField('Tipo de compra')
   Metodo_Pago = StringField('Metodo de pago')
   Edad = IntegerField('Edad')
   submit = SubmitField('Predicción')
   abc = "" # this variable is used to send information back to the front page
