from json import dump
import json
from flask import Flask, request
from flask import jsonify
from requests import Response
app = Flask(__name__)

@app.route('/service', methods=['GET','POST'])
def service():
    data = request.json
    print(data)
    return json.dumps(data)
  
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False, threaded=True)