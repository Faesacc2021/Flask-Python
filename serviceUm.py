from json import dump
import json
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS, cross_origin
from requests import Response

class User(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/serviceUm', methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def serviceUm():
    data = json.dumps(request.json)
    data2 = json.loads(data)
    print(data2)
    user = User(**data2)
    print(user.firstName)
    print(user.lastName)
    return request.json
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=False, threaded=True)