from flask_restful import Api, Resource, reqparse
import data
users = data.users # leave in global space

class User(Resource):
   
   def get(self, name):
      print(self)
      for user in users:
         if (name == user["name"]):
            return user, 200

   def post(self, name):
      parser = reqparse.RequestParser()
      parser.add_argument("age")
      args = parser.parse_args()
      for user in users:
         if (name == user["name"]):
            return "User with name {} already exists".format(name), 400
      user = {
         "name": name,
         "age" : args["age"],
      }
      user.append(user)
      return user, 201

   def put(self, name):
      parser = reqparse.RequestParser()
      parser.add_argument("age")
      args = parser.parse_args()
      for user in users:
         if (name == user["name"]):
            user["age"] = args["age"]
            return user, 200
      user = {
         "name": name,
         "age" : args["age"],
      }
      user.append(user)
      return user, 201
   def delete(self, name):
      global users
      users = [user for user in users if user["name"] != name]
      return "{} is deleted".format(name), 200
   
