from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from marshmallow import Schema, fields,post_load

import config.db_config as db_config
from Utils.utils import update

engine = create_engine(db_config.DB_URI)
Base = declarative_base(engine)

class Model(Base):
    __tablename__ = "model"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))
    type = Column(Integer)
    location = Column(String(100))

    def __str__(self):
        return "<Model(name %s,type %s)>" %(self.name,self.type)

class ModelSchema(Schema):
    id = fields.Int(required=False)
    name = fields.Str()
    type = fields.Int()
    location = fields.Str()

    @post_load
    def make_model(self,data,**kwargs):
        return Model(**data)

def add_model(request_data):
    session = sessionmaker(engine)()
    model_schema = ModelSchema(many=False)
    model = model_schema.load(request_data)
    session.add_all([model])
    session.commit()
    session.close()

def del_model(id):
    session = sessionmaker(engine)()
    model = session.query(Model).filter_by(id=id).first()
    session.delete(model)
    session.commit()
    session.close()

def mod_model(request_data):
    session = sessionmaker(engine)()
    model_schema = ModelSchema(many=False)
    new_model = model_schema.load(request_data)
    old_model = session.query(Model).filter_by(id=new_model.id).first()
    update(old_model,new_model)
    session.commit()
    session.close()

def query_one_model(id):
    session = sessionmaker(engine)()
    model_schema = ModelSchema(many=False)
    model = session.query(Model).filter(Model.id==id).one()
    model = model_schema.dump(model)
    session.commit()
    session.close()

    return model

def query_all_models():
    session = sessionmaker(engine)()
    model_schema = ModelSchema(many=True)
    # models = session.query(Model).filter(Model.name=='hello2').all()
    models = session.query(Model).all()
    models = model_schema.dump(models)
    session.commit()
    session.close()

    return models

if __name__=="__main__":
    add_model()
    query_all_models()