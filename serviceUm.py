from json import dump
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS, cross_origin
from requests import Response

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/serviceUm', methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def serviceUm():
    data = request.json
    print(data)
    return jsonify(data)
  
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=False, threaded=True)