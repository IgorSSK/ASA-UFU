from flask import Flask, url_for, request, json, jsonify
from json import dumps


app = Flask(__name__)

@app.route('/')
def api_default(self):
    return 'Welcome'

if __name__ == '__main__':
    app.run()