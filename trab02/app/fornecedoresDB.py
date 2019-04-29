from dbConnection import DBConnection

class Fornecedores:
    _id_fornecedor = None
    _cnpj = None
    _razaosocial = None
    _telefone = None
    _endereco = None
    _contato = None
    _fg_ativo = None

    def __init__(self, idFornecedor, cnpj = None, razaosocial = None, telefone = None, endereco = None, contato = None, fgAtivo = None):
        self._id_fornecedor = idFornecedor
        self._cnpj = cnpj
        self._razaosocial = razaosocial
        self._telefone = telefone
        self._endereco = endereco
        self._contato = contato
        self._fg_ativo = fgAtivo


    def insereFornecedor(self):
        query = '''
            INSERT INTO TRB02.TB_FORNECEDORES (ID_FORNECEDOR, CNPJ, RAZAOSOCIAL, TELEFONE, ENDERECO, CONTATO, FG_ATIVO)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        params = (self._id_fornecedor, self._cnpj, self._razaosocial, self._telefone, self._endereco, self._contato, self._fg_ativo)
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)

    def selecionaFornecedores(self = None):
        query = '''
            SELECT * FROM TRB02.TB_FORNECEDORES
        '''
        params = None
        new_conn = DBConnection()
        return new_conn.executeRead(query, params)

    def atualizaFornecedor(self, columns, values):
        query = '''
            UPDATE TRB02.TB_FORNECEDORES SET {columns} WHERE ID_FORNECEDOR = %s 
        '''.format(columns = columns)
        params = values + (self._id_fornecedor,)
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)

    def deletaFornecedor(self):
        query = '''
            DELETE FROM TRB02.TB_FORNECEDORES WHERE ID_FORNECEDOR = %s
        '''
        params = self._id_fornecedor
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)