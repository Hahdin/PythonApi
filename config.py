import json

try:
   config = json.loads(open("config.json", "r").read())
except:
   print("Error opening config.json, make sure it exists")
   quit()
