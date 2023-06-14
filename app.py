import json
import mariadb
import dbcreds
import dbhelper
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.post('/api/painting')
def new_painting():
    try:
        error =  dbhelper.check_endpoint_info(request.json,["artist","date_painted","name","image_url"])
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure("call new_painting(?,?,?,?)",[request.json.get("artist"),request.json.get("date_painted"),request.json.get("name"),request.json.get("image_url")])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response("something went wrong",500)
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')

@app.get('/api/painting')
def get_all_paintings():
    try:
        error =  dbhelper.check_endpoint_info(request.args,["artist"])
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure("call get_all_paintings(?)",[request.args.get("artist")])
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return "something went wrong"
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')




if(dbcreds.production_mode == True):
    print("Running Production Mode")
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)
