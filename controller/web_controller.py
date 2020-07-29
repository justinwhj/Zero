from flask import Flask,render_template,request,redirect,url_for

from model.computer import *
from model.model import *
from model.passwords import *

app = Flask(__name__,template_folder="../templates",static_folder="../static")

@app.route("/")
def hello(name=None):
    return render_template("index.html",name=name)

@app.route("/computers/add_computer",methods=["POST"])
def radd_computer():
    computer = {
        "name":request.values.get("name"),
        "host":request.values.get("host")
    }
    add_computer(computer)
    return redirect(url_for("rquery_computer"))

@app.route("/computers/delete_computer",methods=["POST"])
def rdel_computer():
    id = request.values.get("id")
    del_computer(id)
    return redirect(url_for("rquery_computer"))

@app.route("/computers/modify_computer",methods=["POST"])
def rmod_computer():
    new_computer = {
        "id":request.values.get("id"),
        "name": request.values.get("name"),
        "host": request.values.get("host")
    }
    mod_computer(new_computer)
    return redirect(url_for("rquery_computer"))

@app.route("/computers/find_computer",methods=["POST"])
def rfind_computer():
    id = request.values.get("id")
    old_computer = query_one_computer(id)
    return render_template("computer_modify.html",old_computer=old_computer)

@app.route("/computers/query_computer",methods=["POST","GET"])
def rquery_computer():
    computers = query_all_computer()
    return render_template("computer.html",computers=computers)

@app.route("/models/add_model",methods=["POST"])
def radd_model():
    model = {
        "name":request.values.get("name"),
        "type":request.values.get("type"),
        "location":request.values.get("location")
    }
    add_model(model)
    return redirect(url_for("rque_model"))

@app.route("/models/delete_model",methods=["POST"])
def rdel_model():
    id = request.values.get("id")
    del_model(id)
    return redirect(url_for("rque_model"))

@app.route("/models/modify_model",methods=["POST"])
def rmod_model():
    new_model = {
        "id":request.values.get("id"),
        "name": request.values.get("name"),
        "type": request.values.get("type"),
        "location": request.values.get("location")
    }
    mod_model(new_model)
    return redirect(url_for("rque_model"))

@app.route("/models/find_model",methods=["POST"])
def rfind_model():
    id = request.values.get("id")
    old_model = query_one_model(id)
    return render_template("model_modify.html",old_model=old_model)

@app.route("/models/query_model",methods=["POST","GET"])
def rque_model():
    models = query_all_models()
    return render_template("model.html",models=models)

@app.route("/passwords/add_dict",methods=["POST"])
def radd_dict():
    password = {
        "name": request.values.get("name"),
        "type": request.values.get("type"),
        "location": request.values.get("location")
    }
    add_pswd(password)
    return redirect(url_for("rque_dict"))

@app.route("/passwords/del_dict",methods=["POST"])
def rdel_dict():
    id = request.values.get("id")
    del_pswd(id)
    return redirect(url_for("rque_dict"))

@app.route("/passwords/mod_dict",methods=["POST"])
def rmod_dict():
    new_password = {
        "id":request.values.get("id"),
        "name": request.values.get("name"),
        "type": request.values.get("type"),
        "location": request.values.get("location")
    }
    mod_pswd(new_password)
    return redirect(url_for("rque_dict"))

@app.route("/passwords/find_dict",methods=["POST"])
def rfind_dict():
    id = request.values.get("id")
    old_dict = query_one_pswd(id)
    return render_template("password_modify.html",old_dict=old_dict)

@app.route("/passwords/que_dict",methods=["POST","GET"])
def rque_dict():
    passwords = query_all_pswd()
    return render_template("password.html",passwords=passwords)


if __name__=="__main__":
    app.run(host="127.0.0.1",port=80,debug=True)