import flask
from flask import request, jsonify
from pentaho.pentahoapimanager import PentahoApiManager
from shark import Shark
import logging

app = flask.Flask(__name__)
app.config["DEBUG"] = True
logging.basicConfig(filename='C:\Windows\Temp\demo.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def hello():
    return jsonify("Hello World!")


@app.route('/api/v1/roles/all', methods=['GET'])
def api_all():
    app.logger.info('Processing default request')
    sammy = Shark()
    sammy.listPentahoUsers()
    return jsonify(sammy.listPentahoRoles())


app.run()