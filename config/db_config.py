HOSTNAME = '127.0.0.1'
PORT = 3306
DATABASE = 'passwords_manager'
USERNAME = 'root'
PASSWORD = ''
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)
