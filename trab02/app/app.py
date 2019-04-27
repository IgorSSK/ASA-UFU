from flask import Flask, url_for, request, json, jsonify
from json import dumps
from comprasDB import Compra
from fornecedoresDB import Fornecedores
from produtosDB import Produto
from vendasDB import Venda
from vendedoresDB import Vendedor
from categoriasDB import Categorias

app = Flask(__name__)

@app.route('/')
def api_default():
    return 'Welcome!!'

@app.route('/categorias', methods = ['POST', 'GET'])
def api_categorias():
    if(request.method == 'POST'):
        _data = request.get_json()
        _newcategoria = Categorias(_data['idCategoria'], _data['tituloCategoria'], _data['descricaoCategoria'], _data['fgAtivo'])

        retorno = _newcategoria.insereCategoria()
        return jsonify(retorno)
    elif(request.method == 'GET'):
        return jsonify(Categorias.selecionaCategoria())

@app.route('/compras', methods = ['POST', 'GET'])
def api_compras():
    if(request.method == 'POST'):
        _data = request.get_json()
        _newcompra = Compra(_data['idCompra'], _data['idFornecedor'], _data['idProduto'], _data['idCategoria'], _data['dataCompra'], _data['valorTotal'], _data['quantidade'], _data['fgAtivo'])

        retorno = _newcompra.insereCompra()
        return jsonify(retorno)
    elif(request.method == 'GET'):
        return jsonify(Compra.selecionaCompra())

@app.route('/fornecedores', methods = ['POST', 'GET'])
def api_fornecedores():
    if(request.method == 'POST'):
        _data = request.get_json()
        _newfornecedor = Fornecedores(_data['idFornecedor'], _data['cnpj'], _data['razaosocial'], _data['telefone'], _data['endereco'], _data['contato'], _data['fgAtivo'])

        retorno = _newfornecedor.insereFornecedor()
        return jsonify(retorno)
    elif(request.method == 'GET'):
        return jsonify(Fornecedores.selecionaFornecedores())

@app.route('/produtos', methods = ['POST', 'GET'])
def api_produtos():
    if(request.method == 'POST'):
        _data = request.get_json()
        _newprodutos = Produto(_data['idProduto'], _data['idFornecedor'], _data['idCategoria'], _data['nomeProduto'], _data['descricaoProduto'], _data['valorUnitario'], _data['quantidade'], _data['quantidadeMinima'], _data['fgAtivo'])

        retorno = _newprodutos.insereProduto()
        return jsonify(retorno)
    elif(request.method == 'GET'):
        return jsonify(Produto.selecionaProdutos())

@app.route('/vendas', methods = ['POST', 'GET'])
def api_vendas():
    if(request.method == 'POST'):
        _data = request.get_json()
        _newvenda = Venda(_data['idVenda'], _data['idVendedor'], _data['idCategoria'], _data['idProdutos'], _data['dataVenda'], _data['valorTotal'], _data['quantidade'], _data['fgAtivo'])

        retorno = _newvenda.insereVenda()
        return jsonify(retorno)
    elif(request.method == 'GET'):
        return jsonify(Venda.selecionaVendas())

if __name__ == '__main__':
    app.run()