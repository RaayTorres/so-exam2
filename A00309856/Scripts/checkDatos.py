from flask import Flaskfrom flask import Flask, abort, request
from flask_restplus import Resource, Api
from flask_restplus import  fields
import json

from checkCommands import cMemoria, cDisco, cCpu, eServicio

app = Flask(__name__)


api = Api(app,version='1', title='API EN SWAGGER', description="recursos cpu")
ns = api.namespace('v1/information',description='recursos')
@ns.route('/')

class informacion(Resource):
 @api.response(200,'recursos consumidos')
 def get(self):
  list = {}

  list["RAM en uso"] = cMemoria()[0]
  list["Espacio de disco disponible"]= cDisco()[1]	
  list["Consumo de CPU"]= cCpu()[2]
  list["Estado del servicio sshd"]= eServicio()[0]
  return json.dumps(list),200

 @api.response(404,'HTTP 404 NOT FOUND')
 def post(self):
  return "HTTP 404 NOT FOUND",404


 @api.response(404,'HTTP 404 NOT FOUND')
 def put(self):
  return "HTTP 404 NOT FOUND",404


 @api.response(404,'HTTP 404 NOT FOUND')
 def delete(self):
  return "HTTP 404 NOT FOUND",404


if __name__=="__main__":

  app.run(host='0.0.0.0', port=8080, debug='True')

