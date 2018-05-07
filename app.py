from flask import Flask,render_template,request
import pymysql

APP=Flask(__name__)

lst=[]

connection = pymysql.connect(host="localhost",port=3306, user="root",password="password",db = 'mysql')
cursor=connection.cursor()
connection.commit()

@APP.route("/")
def index():
    return render_template("index.html", lst = lst)

@APP.route("/search", methods = ["GET","POST"])
def search():
    try:
        if request.method == "POST":
            name = request.form["search_name"]
            temp = []
            for item in lst: 
                if name in item:
                    temp.append(item)
        return render_template("index.html", lst = temp)
    except ValueError:
        pass

    return render_template("index.html", lst = lst)
@APP.route("/create", methods = ["GET","POST"])
def create():
    if request.method == "POST":
        item = request.form["task_name"]
        lst.append(item)
        cursor.execute("INSERT INTO mysql.Tasks(task_name) Values(%s) ", item)
        connection.commit()
        return render_template("index.html", lst = lst)

    return render_template("index.html", lst = lst)

@APP.route("/delete",methods = ["GET","POST"])
def delete():
    try:
        if request.method == "POST":
            item = request.form["delete_name"]
            lst.remove(item)
            cursor.execute("DELETE FROM mysql.Tasks WHERE task_name=(%s)",item)
            connection.commit()
            return render_template("index.html", lst = lst)
    except ValueError:
        pass
    return render_template("index.html", lst = lst)

@APP.route("/replace",methods = ["GET","POST"])
def replace():
    try:
        if request.method == "POST":
            item1 = request.form["replace_1"]
            item2 = request.form["replace_2"]
            index = lst.index(item1)
            lst[index] = item2
            cursor.execute("UPDATE db.Tasks SET task_name=(%s) WHERE task_name=(%s)",(item2,item1))
            connection.commit()
            return render_template("index.html", lst =lst)
    except ValueError:
        pass
    return render_template("index.html", lst = lst)

if __name__ == "__main__":
        APP.run(host='0.0.0.0')

