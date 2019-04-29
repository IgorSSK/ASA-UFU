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
@app.route('/categorias/<idCategoria>', methods = ['PUT', 'DELETE'])
def api_categorias(idCategoria = None):
    if(request.method == 'POST'):
        _data = request.get_json()
        _newcategoria = Categorias(_data['idCategoria'], _data['tituloCategoria'], _data['descricaoCategoria'], _data['fgAtivo'])

        retorno = _newcategoria.insereCategoria()
        return jsonify(retorno)

    elif(request.method == 'GET'):
        return jsonify(Categorias.selecionaCategoria())

    elif(request.method == 'PUT'):
        columns = ''
        values = ()
        _data = request.get_json()

        for key in _data:
            columns += key + ' = %s, '

        for value in _data.values():
            values += (value,)

        return jsonify(Categorias(idCategoria).atualizaCategoria(columns[0:len(columns)-2], values))

    elif(request.method == 'DELETE'):
        return jsonify(Categorias(idCategoria).deletaCategoria())


@app.route('/compras', methods = ['POST', 'GET'])
@app.route('/compras/<idCompra>', methods = ['PUT', 'DELETE'])
def api_compras(idCompra = None):
    if(request.method == 'POST'):
        _data = request.get_json()
        _newcompra = Compra(_data['idCompra'], _data['idFornecedor'], _data['idProduto'], _data['idCategoria'], _data['dataCompra'], _data['valorTotal'], _data['quantidade'], _data['fgAtivo'])

        retorno = _newcompra.insereCompra()
        return jsonify(retorno)
    elif(request.method == 'GET'):
        return jsonify(Compra.selecionaCompra())

    elif(request.method == 'PUT'):
        columns = ''
        values = ()
        _data = request.get_json()

        for key in _data:
            columns += key + ' = %s, '

        for value in _data.values():
            values += (value,)

        return jsonify(Compra(idCompra).atualizaCompra(columns[0:len(columns)-2], values))

    elif(request.method == 'DELETE'):
        return jsonify(Compra(idCompra).deletaCompra())


@app.route('/fornecedores', methods = ['POST', 'GET'])
@app.route('/fornecedores/<idFornecedor>', methods = ['PUT', 'DELETE'])
def api_fornecedores(idFornecedor = None):
    if(request.method == 'POST'):
        _data = request.get_json()
        _newfornecedor = Fornecedores(_data['idFornecedor'], _data['cnpj'], _data['razaosocial'], _data['telefone'], _data['endereco'], _data['contato'], _data['fgAtivo'])

        retorno = _newfornecedor.insereFornecedor()
        return jsonify(retorno)

    elif(request.method == 'GET'):
        return jsonify(Fornecedores.selecionaFornecedores())
    
    elif(request.method == 'PUT'):
        columns = ''
        values = ()
        _data = request.get_json()

        for key in _data:
            columns += key + ' = %s, '

        for value in _data.values():
            values += (value,)

        return jsonify(Fornecedores(idFornecedor).atualizaFornecedor(columns[0:len(columns)-2], values))

    elif(request.method == 'DELETE'):
        return jsonify(Fornecedores(idFornecedor).deletaFornecedor())


@app.route('/produtos', methods = ['POST', 'GET'])
@app.route('/produtos/<idProduto>', methods = ['PUT', 'DELETE'])
def api_produtos(idProduto = None):
    if(request.method == 'POST'):
        _data = request.get_json()
        _newprodutos = Produto(_data['idProduto'], _data['idFornecedor'], _data['idCategoria'], _data['nomeProduto'], _data['descricaoProduto'], _data['valorUnitario'], _data['quantidade'], _data['quantidadeMinima'], _data['fgAtivo'])

        retorno = _newprodutos.insereProduto()
        return jsonify(retorno)

    elif(request.method == 'GET'):
        return jsonify(Produto.selecionaProdutos())

    elif(request.method == 'PUT'):
        columns = ''
        values = ()
        _data = request.get_json()

        for key in _data:
            columns += key + ' = %s, '

        for value in _data.values():
            values += (value,)

        return jsonify(Produto(idProduto).atualizaProduto(columns[0:len(columns)-2], values))

    elif(request.method == 'DELETE'):
        return jsonify(Produto(idProduto).deletaProduto())


@app.route('/vendas', methods = ['POST', 'GET'])
@app.route('/vendas/<idVenda>', methods = ['PUT', 'DELETE'])
def api_vendas(idVenda = None):
    if(request.method == 'POST'):
        _data = request.get_json()
        _newvenda = Venda(_data['idVenda'], _data['idVendedor'], _data['idCategoria'], _data['idProdutos'], _data['dataVenda'], _data['valorTotal'], _data['quantidade'], _data['fgAtivo'])

        retorno = _newvenda.insereVenda()
        return jsonify(retorno)

    elif(request.method == 'GET'):
        return jsonify(Venda.selecionaVendas())

    elif(request.method == 'PUT'):
        columns = ''
        values = ()
        _data = request.get_json()

        for key in _data:
            columns += key + ' = %s, '

        for value in _data.values():
            values += (value,)

        return jsonify(Venda(idVenda).atualizaVenda(columns[0:len(columns)-2], values))

    elif(request.method == 'DELETE'):
        return jsonify(Venda(idVenda).deletaVenda())

@app.route('/vendedores', methods = ['POST', 'GET'])
@app.route('/vendedores/<idVendedor>', methods = ['PUT', 'DELETE'])
def api_vendedores(idVendedor = None):
    if(request.method == 'POST'):
        _data = request.get_json()
        _newvendedor = Vendedor(_data['idVendedor'], _data['cpf'], _data['nome'], _data['carteiradetrabalho'], _data['telefone'], _data['dataadmissao'], _data['fgAtivo'])

        retorno = _newvendedor.insereVendedor()
        return jsonify(retorno)

    elif(request.method == 'GET'):
        return jsonify(Vendedor.selecionaVendedores())

    elif(request.method == 'PUT'):
        columns = ''
        values = ()
        _data = request.get_json()

        for key in _data:
            columns += key + ' = %s, '

        for value in _data.values():
            values += (value,)

        return jsonify(Vendedor(idVendedor).atualizaVendedores(columns[0:len(columns)-2], values))

    elif(request.method == 'DELETE'):
        return jsonify(Vendedor(idVendedor).deletaVendedores())

if __name__ == '__main__':
    app.run()