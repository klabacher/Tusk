import postgresql
class DB(object):
    _db=None;
    def __init__(self, banco):
       self._db = postgresql.open(banco)
       print(banco)
    def insert(self, value):
        sql=f"INSERT max('{value}')"
        try:
           self._db.execute(sql)
        except:
          return False
        return True
    def consultar(self, sql):
        rs=None
        try:
          rs=self._db.prepare(sql)
        except:
          return None
        return rs
    def select(self, tabela, chave):
        sql='select max('+chave+') from '+tabela
        rs = self.consultar(sql)
        pk = rs.first()
        return pk+1
    def fechar(self):
        self._db.close()