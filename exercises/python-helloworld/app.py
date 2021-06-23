from flask import Flask
from flask import json
import logging
from werkzeug.wrappers import response
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Main request Successfull")
    return "Hello World! haitham from docker"


@app.route("/status")
def health_check():
    res = app.response_class(
        response = json.dumps({"result": "Ok - healthy"}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.info("Status method request successfully")
    return res

@app.route("/metrics")
def metrics():
    res = app.response_class(
        response = json.dumps({"status": "success", "code": 0, "data": "UserCount: 140, UserCountActive: 23"}),
        status = 200,
        mimetype = 'application/json'
    )
    app.logger.info("metrics request successfully")
    return res

if __name__ == "__main__":
    ## stream logs to app.log file
    logging.basicConfig(filename='app.log', level= logging.DEBUG)
    app.run(host='0.0.0.0')

 