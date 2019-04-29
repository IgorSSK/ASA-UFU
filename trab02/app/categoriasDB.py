from dbConnection import DBConnection

class Categorias:
    
    _idCategoria = None
    _tituloCategoria = None
    _descricaoCategoria = None
    _fgAtivo = None

    def __init__(self, idCategoria, tituloCategoria = None, descricaoCategoria = None, fgAtivo = None):
        self._idCategoria = idCategoria
        self._tituloCategoria = tituloCategoria
        self._descricaoCategoria = descricaoCategoria
        self._fgAtivo = fgAtivo
    

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

    def atualizaCategoria(self, columns, values):
        query = '''
            UPDATE TRB02.TB_CATEGORIAS SET {columns} WHERE ID_CATEGORIA = %s 
        '''.format(columns = columns)
        params = values + (self._idCategoria,)
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)

    def deletaCategoria(self):
        query = '''
            DELETE FROM TRB02.TB_CATEGORIAS WHERE ID_CATEGORIA = %s
        '''
        params = self._idCategoria
        new_conn = DBConnection()
        return new_conn.executeOnly(query, params)