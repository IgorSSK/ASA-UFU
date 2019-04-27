from dbConnection import DBConnection

class Venda:
    _id_venda = None
    _id_vendedor = None
    _id_categoria = None
    _id_produtos = None
    _datavenda = None
    _valortotal = None
    _quantidade = None
    _fg_ativo = None

    def __init__(self, id_venda, id_vendedor, id_produtos, id_categoria, datavenda, valortotal, quantidade, fg_ativo):
        self._id_venda = id_venda
        self._id_vendedor = id_vendedor
        self._id_categoria = id_categoria
        self._id_produtos = id_produtos
        self._datavenda = datavenda
        self._valortotal = valortotal
        self._quantidade = quantidade
        self._fg_ativo = fg_ativo

    def getIdVenda(self):
        return self._id_venda

    def insereVenda(self):
        query = '''
            INSERT INTO TRB02.TB_VENDAS (ID_VENDA, ID_VENDEDOR, ID_CATEGORIA, ID_PRODUTOS, DATAVENDA, VALORTOTAL, QUANTIDADE, FG_ATIVO)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (self._id_venda, self._id_vendedor, self._id_produtos, self._id_categoria, self._datavenda, self._valortotal, self._quantidade, self._fg_ativo)
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)

    def selecionaVendas(self = None):
        query = '''
            SELECT * FROM TRB02.TB_VENDAS
        '''
        params = None
        new_conn = DBConnection()
        return new_conn.executeRead(query, params)