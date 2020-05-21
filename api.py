from celery.app.control import Inspect
from celery.result import AsyncResult
from flask import Flask, jsonify, request
from markupsafe import escape

from tasks import add as celery_add

app = Flask(__name__)


@app.route('/task/add', methods=['POST'])
def add():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    result = celery_add.delay(n1, n2)
    return jsonify(success=True, uuid=result.id)


@app.route('/status/<uuid:id>', methods=['GET'])
def get_status(id):
    result = AsyncResult(id)
    return jsonify(status=result.status)


@app.route('/status/active', methods=['GET'])
def get_active():
    i = Inspect()
    active_tasks = i.active()
    return jsonify(active_tasks)
