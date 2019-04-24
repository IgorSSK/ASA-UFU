from flask import Flask, url_for, request, json, jsonify
from json import dumps

from clients import Client
from products import Product
from sales import Sale


app = Flask(__name__)

clients = []
products = []
sales = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'


@app.route('/client', methods = ['POST', 'GET'])
def api_client():
    if(request.method == 'POST'):
        request_data = request.get_json()
        
        for data in request_data:
            new_client = Client(data['id'], data['name'])
            clients.append(new_client)

        awsr = { 'err': 'Error creating client'}
        if(new_client != None):
            awsr = { 'status': 'ok' }

        return jsonify(awsr)
    elif(request.method == 'GET'):
        awsr = []
        for client in clients:
            element = { 'id': client.getId(), 'name': str(client.getName()) }
            awsr.append(element)
        return jsonify(awsr)


@app.route('/product', methods = ['POST', 'GET'])
def api_product():
    if(request.method == 'POST'):
        request_data = request.get_json()
        
        for data in request_data:
            new_product = Product(data['id'], data['product'], data['price'])
            products.append(new_product)

        awsr = { 'err': 'Error creating client'}
        if(new_product != None):
            awsr = { 'status': 'ok' }

        return jsonify(awsr)
    elif(request.method == 'GET'):
        awsr = []
        for product in products:
            element = { 'id': product.getId(), 'name': str(product.getProduct()), 'price': product.getPrice() }
            awsr.append(element)
        return jsonify(awsr)


@app.route('/newsale', methods = ['POST'])
def api_sale():
    request_data = request.get_json()

    for product in products:
        if(product.getId() == request_data['idProduct']):
            amount = request_data['amount']
            total = int(amount) * product.getPrice()
            new_sale = Sale(request_data['idClient'], request_data['idProduct'], amount, total)
            sales.append(new_sale)

            print(sales)
    return jsonify({ 'status': 'ok' })


@app.route('/sales/<idClient>', methods = ['GET'])
def api_sales(idClient):
    aws = []
    count = 0
    for sale in sales:
        if(sale.getIdClient() == int(idClient)):
            element = { 'product': sale.getIdProduct(), 'amount': sale.getAmount(), 'total': sale.getTotal() }
            aws.append(element)
            count = count + 1
    
    totalSales = { 'Total of Sales': count }
    aws.append(totalSales)
    return jsonify(aws)

if __name__ == '__main__':
    app.run()