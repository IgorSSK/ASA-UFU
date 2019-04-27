from dbConnection import DBConnection

class Categorias:
    
    _idCategoria = None
    _tituloCategoria = None
    _descricaoCategoria = None
    _fgAtivo = None

    def __init__(self, idCategoria, tituloCategoria, descricaoCategoria, fgAtivo):
        self._idCategoria = idCategoria
        self._tituloCategoria = tituloCategoria
        self._descricaoCategoria = descricaoCategoria
        self._fgAtivo = fgAtivo

    def getIdCategoria(self):
        return self._idCategoria
    
    def getTituloCategoria(self):
        return self._tituloCategoria
    
    def getDescricaoCategoria(self):
        return self._descricaoCategoria

    def getFgAtivo(self):
        return self._fgAtivo

    def insereCategoria(self):
        query = '''
            INSERT INTO TRB02.TB_CATEGORIAS (ID_CATEGORIA, TITULOCATEGORIA, DESCRICAOCATEGORIA, FG_ATIVO)
            VALUES (%s, %s, %s, %s)
        '''
        params = (self._idCategoria, self._tituloCategoria, self._descricaoCategoria, self._fgAtivo)
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)

    def selecionaCategoria(self = None):
        query = '''
            SELECT * FROM TRB02.TB_CATEGORIAS
        '''
        params = None
        new_conn = DBConnection()
        return new_conn.executeRead(query, params)