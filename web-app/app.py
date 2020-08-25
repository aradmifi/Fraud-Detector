from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key' #you will need a secret key

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + "eyJraWQiOiIyMDIwMDcyNDE4MzEiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJpYW0tU2VydmljZUlkLTlmMTFhNzNkLWI1N2QtNGFhNy1iZTE0LTI3NzY4ZWVmODUzYyIsImlkIjoiaWFtLVNlcnZpY2VJZC05ZjExYTczZC1iNTdkLTRhYTctYmUxNC0yNzc2OGVlZjg1M2MiLCJyZWFsbWlkIjoiaWFtIiwiaWRlbnRpZmllciI6IlNlcnZpY2VJZC05ZjExYTczZC1iNTdkLTRhYTctYmUxNC0yNzc2OGVlZjg1M2MiLCJuYW1lIjoid2RwLXdyaXRlciIsInN1YiI6IlNlcnZpY2VJZC05ZjExYTczZC1iNTdkLTRhYTctYmUxNC0yNzc2OGVlZjg1M2MiLCJzdWJfdHlwZSI6IlNlcnZpY2VJZCIsImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImU4NmQ3YzU5OTA5MTkwYzg4ZGIzZDZjNjBhYWY1NTRkIiwiZnJvemVuIjp0cnVlfSwiaWF0IjoxNTk2MjA0NDczLCJleHAiOjE1OTYyMDgwNzMsImlzcyI6Imh0dHBzOi8vaWFtLmJsdWVtaXgubmV0L2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.Jza_BjwI9OstNsFj8G8fD3IfW3X_1_zAP1pwcUfKp-DsYxj9d07d4b2flIiM_wFjDS2ylxn7SI7nTBRGC9Fe2jMBqMUWQDkhsqA1gMJNuTzmGc-3Ik9KLLvHK56OwJjiy4UTMUL2L9tMWYufYRP0KVDLJ2qjeoGovWizqOOY5AbaMEKpnhrMIyLimPjnh5wwAtBc20BEjss5cj4WrbHmoLz4W63-jC3fHQgrLoVOm14EcS8154bkXEtHb-YbvIENOdf61PbOG5AObxkB6UxNAOGnHEuCGnb2J0l-ZUw2hCK7RIOtSxKXjKPBXdkdhHlmCd5Fg8ArtPjsshH4HKC70g","refresh_token":"OKCr2IM6fK31Y5sjsLvW9tppLqlh5y4_bk1Ms-I46fJRni_uOPbQf8cblyHo40f6Y7KV4fdnkyX9cTjSSS1wi5iaK4VpxwDKEGBsl0nY8fwAw3kUtX45_ij6Me-8mxKbu9b-HGh3BQdcqmFEHwtFb4o0cO8N6LpMqxujm9xstZSs24iXpgh1JbFwKAqObeEckLuZJe7DQtZSqP3LnhU2As3KtsbPZR-bU0XrK-VVdzXZBG1hraUmtvCCMOKumvHGia-cz3nJtllIS_gsw2mrep7eLrTDY0Vnxgt0aQkfGlXZGeYe7qXiOl8eiE4Ets8--vTQFnLOQp5KJql8KXO-DcVLVviX4WHQoA0XVAlfaQrVAnGa3ngXTGXXPlixhh78WzomoyzRKXX4dWfkw5z7kaIgKacwlKEEFmzNNXqKFbMXYKqGePi-K7ntHuTnoi_D_FDmFLhMRVWh3Xo-QfWFhZUiAQP0HSbK0AMrWAQXS_H9h5PCFLzozX8ezF8fAAzf0GjDU30CWK0KdA7yYA8uP5bFlavDYI4OUksyEFxqEMRIbQIxjQg8PeJJJ666pLAyFcR--po4pe4XwLgrXe2KdzQ2ephj1DkaximHN0z_YFSKQPMiotaEUaZVkgR-i2Q_yC3ANETTQIhzQ7E9-aQ4Tvng36Qs7u8H7vT_42aEo7rIHzhooLvVaUmESCFtYdNeGmk4g1LY5SmYbNe-dHQ1UEJrXPAfiXbvFMc0GWfdO_-VBPbmQgVLtLM6i5ywwdzfxu0d2y-OLFqrfB-n5jdN4S8VZdjAxDu8VR46MJRahBWIwswa7T2Q0zB9OjL1q5q7ddrXabQTFu3Jxazrapj7XsBt3uHQ6a6nF8LIb5gBktDNEsFs6XIk-e9TIzwJImsErsa9b95kKWunQr3Tom5idhsUkRMScxZUNllUGopOtfTyAR_kNkBykKsDMtKoBTY6BTEy_TIuOZLFWOGEWDSojwms_ctvwfBzAUD0mT2W20gw53sqNsozpJpbFqplYSP5at6R3I3EQ3s9M96Iu_2Y6PV8uszXd0eucxvgY27orq6fdP6MMEqShf3ScFgVQNEGiSc",
                  'ML-Instance-ID': "61862e37-c7bc-4fae-9d6e-5dc33e3d5700"}

        if(form.ID_Txn.data == None): 
          python_object = []
        else:
          #float(form.bmi.data)
            python_object = [int(form.ID_Txn.data), form.Hora_Txn.data, form.Sexo.data,
            form.Edo_Civil.data, form.Hijos.data, form.Monto_Txn.data, form.Establecimiento.data, 
            form.Tipo_Compra.data, form.Metodo_Pago.data, form.Edad.data]
        #Transform python objects to  Json

        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["ID_Txn", "Hora_Txn", "Sexo",
          "Edo_Civil", "Hijos", "Monto_Txn", "Establecimiento", "Tipo_Compra", "Metodo_Pago", "Edad"], "values": userInput }]}

        response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/v4/deployments/4c8b8b97-954b-4238-b09c-1d9276f8a39d/predictions", json=payload_scoring, headers=header)

        output = json.loads(response_scoring.text)
        print(output)
        
  
        form.abc = output # this returns the response back to the front page
        return render_template('index.html', form=form)