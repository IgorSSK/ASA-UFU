import psycopg2

class DBConnection:
    _cursor = None
    _connection = None

    def __init__(self):
        self._connection = psycopg2.connect(user="postgres", password="Lock@001", host="127.0.0.1", port="5432",database="asa")
        self._cursor = self._connection.cursor()

    def getCursor(self):
        return self._cursor

    def getConnection(self):
        return self._connection

    def closeConnection(self):
        self._connection.close()

    def closeCursor(self):
        self._cursor.close()

    def executeOnly(self, query, params):
        try:
            self.getCursor().execute(query, params)
            status = True
        except (Exception, psycopg2.Error) as error:
            status = error
        finally:
            if(status == True):
                self.getConnection().commit()
            self.getCursor().close()
            self.getConnection().close()
        
        return status
        
