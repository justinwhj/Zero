from flask import Flask
import pymysql
import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article' #如果不指定表名，会默认以这个类名的小写为表名
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(100),nullable = False)
    content = db.Column(db.Text,nullable = False)

db.create_all()

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)