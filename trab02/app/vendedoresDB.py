from dbConnection import DBConnection

class Vendedor:
    _id_vendedor  = None
    _cpf = None
    _nome = None
    _carteiradetrabalho = None
    _telefone  = None
    _dataadmissao = None
    _fg_ativo  = None

    def __init__(self, id_vendedor, cpf, nome, carteiradetrabalho, telefone, dataadmissao, fg_ativo):
        self._id_vendedor  = id_vendedor
        self._cpf = cpf
        self._nome = nome
        self._carteiradetrabalho = carteiradetrabalho,
        self._telefone  = telefone
        self._dataadmissao = dataadmissao
        self._fg_ativo  = fg_ativo

    def getIdVendedor(self):
        return self._id_vendedor

    def insereVendedor(self):
        query = '''
            INSERT INTO TRB02.TB_VENDEDORES (ID_VENDEDOR, CPF, NOME, CARTEIRADETRABALHO, TELEFONE, DATAADMISSAO, FG_ATIVO)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        params = (self._id_vendedor, self._cpf, self._nome, self._carteiradetrabalho, self._telefone, self._dataadmissao, self._fg_ativo)
        new_conn = DBConnection()
        new_conn.executeOnly(query, params)

    def selecionaVendedores(self = None):
        query = '''
            SELECT * FROM TRB02.TB_VENDEDORES
        '''
        params = None
        new_conn = DBConnection()
        return new_conn.executeRead(query, params)