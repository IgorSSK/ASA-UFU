from dbConnection import DBConnection

class Compra:
    _id_compra = None
    _id_fornecedor = None
    _id_produtos = None
    _id_categoria = None
    _datacompra = None
    _valortotal = None
    _quantidade = None
    _fg_ativo = None

    def __init__(self, id_compra, id_fornecedor = None, id_produtos = None, id_categoria = None, datacompra = None, valortotal = None, quantidade = None, fg_ativo = None):
        self._id_compra = id_compra
        self._id_fornecedor = id_fornecedor
        self._id_produtos = id_produtos
        self._id_categoria = id_categoria
        self._datacompra = datacompra
        self._valortotal = valortotal
        self._quantidade = quantidade
        self._fg_ativo = fg_ativo

    def __init_subclass__(self, id_compra):
        self._id_compra = id_compra


    def insereCompra(self):
        query = '''
            INSERT INTO TRB02.TB_COMPRAS (ID_COMPRA, ID_FORNECEDOR, ID_PRODUTOS, ID_CATEGORIA, DATACOMPRA, VALORTOTAL, QUANTIDADE, FG_ATIVO)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (self._id_compra, self._id_fornecedor, self._id_produtos, self._id_categoria, self._datacompra, self._valortotal, self._quantidade, self._fg_ativo)
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)

    def selecionaCompra(self = None):
        query = '''
            SELECT * FROM TRB02.TB_COMPRAS
        '''
        params = None
        new_conn = DBConnection()
        return new_conn.executeRead(query, params)

    def atualizaCompra(self, columns, values):
        query = '''
            UPDATE TRB02.TB_COMPRAS SET {columns} WHERE ID_COMPRA = %s 
        '''.format(columns = columns)
        params = values + (self._id_compra,)
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)

    def deletaCompra(self):
        query = '''
            DELETE FROM TRB02.TB_COMPRAS WHERE ID_COMPRA = %s
        '''
        params = self._id_compra
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)