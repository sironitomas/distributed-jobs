from celery.result import AsyncResult
from flask import Flask, jsonify, request
from markupsafe import escape

from tasks import add as celery_add

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


@app.route('/add', methods=['POST'])
def add():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    result = celery_add.delay(n1, n2)
    response = jsonify(success=True, uuid=result.id)
    return response


@app.route('/status/<uuid:uuid>', methods=['GET'])
def status(uuid):
    result = AsyncResult(uuid)
    return jsonify(ready=result.ready())
