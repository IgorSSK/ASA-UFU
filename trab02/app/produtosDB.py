from dbConnection import DBConnection

class Produto:
    _id_produtos = None
    _id_fornecedor = None
    _id_categoria = None
    _nomeproduto = None
    _descricaoproduto  = None
    _valorunitario = None
    _quantidade = None
    _quantidademinima = None
    _fg_ativo = None

    def __init__(self, idProduto, idFornecedor, idCategoria, nomeProduto, descricaoProduto, valorUnit, quantidade, quantidadeMin, fgAtivo):
        self._id_produtos = idProduto 
        self._id_fornecedor = idFornecedor
        self._id_categoria = idCategoria
        self._nomeproduto = nomeProduto
        self._descricaoproduto = descricaoProduto
        self._valorunitario = valorUnit
        self._quantidade = quantidade
        self._quantidademinima = quantidadeMin
        self._fg_ativo = fgAtivo

    def getIdProduto(self):
        return self._id_produtos
    
    def getNomeProduto(self):
        return self._nomeproduto
    
    def getDescricaoProduto(self):
        return self._descricaoproduto
    
    def getValorUnitario(self):
        return self._valorunitario
    
    def getQuatidade(self):
        return self._quantidade

    def getQuatidadeMinima(self):
        return self._quantidademinima

    def insereProduto(self):
        query = '''
            INSERT INTO TRB02.TB_PRODUTOS (ID_PRODUTOS, ID_FORNECEDOR, ID_CATEGORIA, NOMEPRODUTO, DESCRICAOPRODUTO, VALORUNITARIO, QUANTIDADE, QUANTIDADEMINIMA, FG_ATIVO)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (self._id_produtos, self._id_fornecedor, self._id_categoria, self._nomeproduto, self._descricaoproduto, self._valorunitario, self._quantidade, self._quantidademinima, self._fg_ativo)
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)

    def selecionaProdutos(self = None):
        query = '''
            SELECT * FROM TRB02.TB_PRODUTOS
        '''
        params = None
        new_conn = DBConnection()
        return new_conn.executeRead(query, params)