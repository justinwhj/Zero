from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/computers/add_computer")
def add_computer():
    return "add_success"

@app.route("/computers/delete_computer")
def del_computer():
    return "delete_success"

@app.route("/computers/modify_computer")
def mod_computer():
    return "mod_success"

@app.route("/computers/query_computer")
def query_computer():
    return "que_success"

@app.route("/models/add_model")
def add_model():
    return "add_success"

@app.route("/models/delete_model")
def del_model():
    return "del_success"

@app.route("/models/modify_model")
def mod_model():
    return "mod_success"

@app.route("/models/query_model")
def que_model():
    return "query_success"

@app.route("/passwords/add_dict")
def add_dict():
    return "add_success"

@app.route("/passwords/del_dict")
def del_dict():
    return "del_success"

@app.route("/passwords/mod_dict")
def mod_dict():
    return "mod_success"

@app.route("/passwords/que_dict")
def que_dict():
    return "que_success"


if __name__=="__main__":
    app.run(host="127.0.0.1",port=80,debug=True)