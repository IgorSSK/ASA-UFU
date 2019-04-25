from flask import Flask, url_for, request, json, jsonify
from json import dumps

from categoriasDB import Categorias

app = Flask(__name__)

@app.route('/')
def api_default():
    return 'Welcome!!'

@app.route('/categorias', methods = ['POST'])
def api_categorias():
    Categorias(1,'Teste','Teste',0).insereCategoria()
    return { 'status': '200 - OK'}


if __name__ == '__main__':
    app.run()