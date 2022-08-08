from services.database_helper import define_database
from setup.Message import Message

class UserService():
    def getById(id: int):
        db = define_database()
        try:
            rows = db(db.users.id ==id).select()
            return Message(data = rows[0])
        except:
            return Message(success=False, message="Erro ao obter usuário")
        finally:
            db.close()
            
    def getAll(page=1, pageSize = 10):
        db = define_database()
        try:
            rows = db(db.users).select(limitby=((page-1)*pageSize, page*pageSize))
            return Message(data = rows.as_list())
        except:
            return Message(success=False, message="Erro ao obter usuário")
        finally:
            db.close()