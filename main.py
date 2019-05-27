from flask import Flask
from flask_restful import Api, Resource, reqparse
import user

app = Flask(__name__)
api = Api(app)
  
api.add_resource(user.User, "/user/<string:name>")
app.run(debug=True)