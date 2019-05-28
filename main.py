from flask import Flask
from flask_restful import Api, Resource, reqparse
import user
import json
import config as server

# http://flask.pocoo.org/docs/0.12/config/ for settings
app = Flask(__name__)
api = Api(app)
  
api.add_resource(user.User, "/user/<string:name>")
app.run(debug=True, port=server.config['PORT'])