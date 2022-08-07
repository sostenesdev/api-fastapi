from models.BaseModel import BaseModel
from models.database_helper import define_database
from setup.Message import Message

class User(BaseModel):
    def __init__(self,name, username, email, password, user_group_id):
        super().__init__(self)
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.user_group_id = user_group_id
    
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
            rows = db(db.users).select(limit=((page-1)*pageSize, page*pageSize))
            return Message(data = rows.json())
        except:
            return Message(success=False, message="Erro ao obter usuário")
        finally:
            db.close()