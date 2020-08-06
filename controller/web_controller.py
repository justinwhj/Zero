import json
import os

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename

from model.computer import *
from model.model import *
from model.passwords import *

import service.password_service as pass_service

app = Flask(__name__,template_folder="../templates",static_folder="../static")
root_path = os.path.join(os.path.dirname(__file__) , os.path.pardir)

###############################################################################################################
#-------------------------------------------------用户管理模块-------------------------------------------------#
###############################################################################################################
@app.route("/")
def hello():
    return render_template("login.html")

@app.route("/user/login",methods=["POST"])
def login():
    return redirect(url_for("rque_dict"))

@app.route("/user/register",methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/user/forget",methods=["GET"])
def forget():
    return render_template("forgot-password.html")

@app.route("/user/recover",methods=["GET","POST"])
def recover():
    return render_template("recover-password.html")

###############################################################################################################
#-------------------------------------------------设备管理模块-------------------------------------------------#
###############################################################################################################
@app.route("/computers/add_computer",methods=["POST"])
def radd_computer():
    computer = {
        "name":request.values.get("name"),
        "host":request.values.get("host")
    }
    add_computer(computer)
    return redirect(url_for("rquery_computer"))

@app.route("/computers/delete_computer",methods=["POST","GET"])
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

@app.route("/computers/find_computer",methods=["POST","GET"])
def rfind_computer():
    old_computer = {
        "id": 0,
        "name":"",
        "host":""
    }
    action = "add"
    id = request.values.get("id")
    if int(id)!=0:
        old_computer = query_one_computer(id)
        action = "modify"
    return render_template("computer_modify.html",old_computer=old_computer,action=action)

@app.route("/computers/query_computer",methods=["POST","GET"])
def rquery_computer():
    computers = query_all_computer()
    return render_template("computer_list.html",computers=computers)

###############################################################################################################
#-------------------------------------------------模型管理模块-------------------------------------------------#
###############################################################################################################
@app.route("/models/add_model",methods=["POST"])
def radd_model():
    model = {
        "name":request.values.get("name"),
        "type":request.values.get("type"),
        "location":request.values.get("location")
    }
    add_model(model)
    return redirect(url_for("rque_model"))

@app.route("/models/delete_model",methods=["POST","GET"])
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

@app.route("/models/find_model",methods=["POST","GET"])
def rfind_model():
    action = "add"
    old_model = {
        "id": 0,
        "name": "",
        "type": "",
        "location": ""
    }

    id = request.values.get("id")
    if int(id)!=0:
        # 更新模型
        old_model = query_one_model(id)
        action = "modify"
    return render_template("model_modify.html",old_model=old_model,action=action)

@app.route("/models/query_model",methods=["POST","GET"])
def rque_model():
    models = query_all_models()
    return render_template("model_list.html",models=models)

###############################################################################################################
#-------------------------------------------------口令管理模块-------------------------------------------------#
###############################################################################################################
@app.route("/passwords/add_dict",methods=["POST"])
def radd_dict():
    f = request.files['pass_txt']
    upload_path = os.path.join(root_path, 'data\\passwords', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
    f.save(upload_path)

    password = {
        "name": request.values.get("name"),
        "type": request.values.get("type"),
        "location": secure_filename(f.filename),
    }
    add_pswd(password)
    return redirect(url_for("rque_dict"))

@app.route("/passwords/del_dict",methods=["POST","GET"])
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

@app.route("/passwords/find_dict",methods=["POST","GET"])
def rfind_dict():
    old_dict = {
        "id": 0,
        "name":"",
        "type":"",
        "location":""
    }
    action = "add"
    id = request.values.get("id")

    if int(id)!=0:
        old_dict = query_one_pswd(id)
        action = "mod"
    return render_template("password_modify.html",old_dict=old_dict,action=action)

@app.route("/passwords/que_dict",methods=["POST","GET"])
def rque_dict():
    passwords = query_all_pswd()
    return render_template("password_list.html",passwords=passwords)

@app.route("/passwords/analyze_dict",methods=["POST","GET"])
def ranalyze_dict():
    id = request.values.get("id")
    dict_to_analyze = query_one_pswd(id)
    path = "\\data\\passwords\\"+dict_to_analyze["location"]

    analysis = pass_service.analyze_single_dict(path)
    return render_template("password_analysis2.html",test="hello test",data=json.dumps(analysis))

@app.route("/passwords/compare_dict",methods=["POST","GET"])
def rcompare_dict():
    id1 = request.values.get("txt1")
    id2 = request.values.get("txt2")
    return render_template("password_compare.html", test="hello test", data=json.dumps({}))

@app.route("/passwords/password_generate",methods=["POST","GET"])
def rgenerate_dict():
    return render_template("password_generate.html")
###############################################################################################################
#-------------------------------------------------公共响应模块-------------------------------------------------#
###############################################################################################################
@app.route("/utils/find_path",methods=["POST"])
def rfind_path():
    path = request.values.get("path")
    paths = os.listdir(root_path + "\\data\\passwords\\"+path)
    res = []
    for i in range(len(paths)):
        res.append(os.path.join(path,paths[i]))
    return json.dumps(res)


if __name__=="__main__":
    app.run(host="127.0.0.1",port=61116,debug=True)


