from json import dump
import json
from flask import Flask, request
from flask import jsonify
from requests import Response
app = Flask(__name__)

@app.route('/serviceUm', methods=['GET','POST'])
def serviceUm():
    data = request.json
    print(data)
    return jsonify(data)
  
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=False, threaded=True)