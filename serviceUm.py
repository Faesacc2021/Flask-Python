import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
from LoginUser import LoginUser

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/serviceUm', methods=['GET','POST'])
@cross_origin(supports_credentials=True)
def serviceUm():
    data = json.dumps(request.json)
    data2 = json.loads(data)
    print(data2)
    loginUser = LoginUser(
        
    )
    print(loginUser.email)
    print(loginUser )
    return request.json
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=False, threaded=True)