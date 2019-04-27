from dbConnection import DBConnection

class Fornecedores:
    _id_fornecedor = None
    _cnpj = None
    _razaosocial = None
    _telefone = None
    _endereco = None
    _contato = None
    _fg_ativo = None

    def __init__(self, idFornecedor, cnpj, razaosocial, telefone, endereco, contato, fgAtivo):
        self._id_fornecedor = idFornecedor
        self._cnpj = cnpj
        self._razaosocial = razaosocial
        self._telefone = telefone
        self._endereco = endereco
        self._contato = contato
        self._fg_ativo = fgAtivo
    
    def getIdFornecedor(self):
        return self._id_fornecedor

    def getCnpj(self):
        return self._cnpj
    
    def getRazaoSocial(self):
        return self._razaosocial
    
    def getTelefone(self):
        return self._telefone
    
    def getEndereco(self):
        return self._endereco
    
    def getContato(self):
        return self._contato

    def getFgAtivo(self):
        return self._fg_ativo

    def insereFornecedor(self):
        query = '''
            INSERT INTO TRB02.TB_FORNECEDOR (ID_FORNECEDOR, CNPJ, RAZAOSOCIAL, TELEFONE, ENDERECO, CONTATO, FG_ATIVO)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        params = (self._id_fornecedor, self._cnpj, self._razaosocial, self._telefone, self._endereco, self._contato, self._fg_ativo)
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)

    def selecionaFornecedores(self = None):
        query = '''
            SELECT * FROM TRB02.TB_FORNECEDOR
        '''
        params = None
        new_conn = DBConnection()
        return new_conn.executeRead(query, params)