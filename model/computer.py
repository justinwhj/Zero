from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from marshmallow import Schema, fields,post_load

import config.db_config as db_config
from Utils.utils import update

engine = create_engine(db_config.DB_URI)
Base = declarative_base(engine)

class Computer(Base):
    __tablename__ = "computer"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))
    host = Column(String(50))

    def __str__(self):
        return "<Computer(name %s,host %s)>" %(self.name,self.host)

class ComputerSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str()
    host = fields.Str()

    @post_load
    def make_computer(self,data,**kwargs):
        return Computer(**data)

def add_computer(request_data):
    session = sessionmaker(engine)()
    computer_schema = ComputerSchema(many=False)
    computer = computer_schema.load(request_data)
    session.add_all([computer])
    session.commit()
    session.close()

def del_computer(id):
    session = sessionmaker(engine)()
    computer1 = session.query(Computer).filter_by(id=id).first()
    session.delete(computer1)
    session.commit()
    session.close()

def mod_computer(request_data):
    session = sessionmaker(engine)()
    computer_schema = ComputerSchema(many=False)
    new_computer = computer_schema.load(request_data)
    old_computer = session.query(Computer).filter_by(id=new_computer.id).first()
    update(old_computer,new_computer)
    session.commit()
    session.close()

def query_one_computer(id):
    session = sessionmaker(engine)()
    computer_schema = ComputerSchema(many=False)
    computer = session.query(Computer).filter(Computer.id==id).one()
    computer = computer_schema.dump(computer)
    session.commit()
    session.close()

    return computer

def query_all_computer():
    session = sessionmaker(engine)()
    computer_schema = ComputerSchema(many=True)
    # computers = session.query(Computer).filter(Computer.name=='hello2').all()
    computers = session.query(Computer).all()
    computers = computer_schema.dump(computers)
    session.commit()
    session.close()

    return computers

if __name__=="__main__":
    com_data1 = {
        "name":"hello2222",
        "host":"127.0.0.1"
    }

    com_data2 = {
        "id": 1,
        "name": "hello1111",
        "host": "127.0.0.1"
    }

    add_computer(com_data1)
    mod_computer(com_data2)
    res1 = query_all_computer()
    print(res1)
    res2 = query_one_computer(1)
    print(res2)

    # comp = Computer(id=1,name="test",host="127.0.0.1")
    # print(comp)
    # com_schema = ComputerSchema(many=False)
    # result1 = com_schema.dump(comp)
    # print(result1)
    #
    # result2 =com_schema.load(com_data)
    # print(result2)

    # result = com_schema.load(com_data)
    # print(result.data)

    # add_computer()
    # query_all_computer()





