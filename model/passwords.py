from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from marshmallow import Schema, fields,post_load

import config.db_config as db_config
from Utils.utils import update

engine = create_engine(db_config.DB_URI)
Base = declarative_base(engine)

class Password(Base):
    __tablename__ = "password"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))
    type = Column(Integer)
    location = Column(String(100))

    def __str__(self):
        return "<Password(name %s,type %s)>" %(self.name,self.type)

class PasswordSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str()
    type = fields.Int()
    location = fields.Str()

    @post_load
    def make_password(self,data,**kwargs):
        return Password(**data)

def add_pswd(request_data):
    session = sessionmaker(engine)()
    password_schema = PasswordSchema(many=False)
    password = password_schema.load(request_data)
    session.add_all([password])
    session.commit()
    session.close()

def del_pswd(id):
    session = sessionmaker(engine)()
    password = session.query(Password).filter_by(id=id).first()
    session.delete(password)
    session.commit()
    session.close()

def mod_pswd(request_data):
    session = sessionmaker(engine)()
    password_schema = PasswordSchema(many=False)
    new_password = password_schema.load(request_data)
    old_password = session.query(Password).filter_by(id=new_password.id).first()
    update(old_password,new_password)

    session.commit()
    session.close()

def query_one_pswd(id):
    session = sessionmaker(engine)()
    password_schema = PasswordSchema(many=False)
    password = session.query(Password).filter(Password.id==id).one()
    password = password_schema.dump(password)
    session.commit()
    session.close()

    return password

def query_all_pswd():
    session = sessionmaker(engine)()
    password_schema = PasswordSchema(many=True)
    # passwords = session.query(Password).filter(Password.name=='hello2').all()
    passwords = session.query(Password).all()
    passwords = password_schema.dump(passwords)
    session.commit()
    session.close()

    return passwords

if __name__=="__main__":
    add_pswd()
    query_all_pswd()