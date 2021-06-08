from flask import Flask
from flask import json
from werkzeug.wrappers import response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! haitham"


@app.route("/status")
def health_check():
    res = app.response_class(
        response = json.dumps({"result": "Ok - healthy"}),
        status = 200,
        mimetype = 'application/json'
    )
    return res

@app.route("/metrics")
def metrics():
    res = app.response_class(
        response = json.dumps({"status": "success", "code": 0, "data": "UserCount: 140, UserCountActive: 23"}),
        status = 200,
        mimetype = 'application/json'
    )
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0')

 