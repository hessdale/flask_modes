import json
import mariadb
import dbcreds
import dbhelper
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)






app.run(debug=True)
