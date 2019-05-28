import json
msg = "Error opening config.json, make sure it exists"
try:
   config = json.loads(open("config.json", "r").read())
   # test for required settings, for example:
   # if (config.get('PORT') == None):
   #    msg ="PORT missing from config"
   #    quit()
   # or call get() and catch the KeyError below
except KeyError:
   print("Missing required KEY in config.json")
   quit()
except:
   print(msg)
   quit()
