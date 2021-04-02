from flask import Flask, jsonify
from helper import resolve

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    items = resolve()
    return jsonify(items)



