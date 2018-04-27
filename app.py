import pymysql.cursors
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route('/')
#connection.cursor().execute("CREATE TABLE TO_DO (ID int NOT NULL AUTO_INCREMENT, Item varchar(100),PRIMARY KEY (ID))")
def index():
    return render_template('index.html')
    

@app.route('/todo/create', methods=['POST'])
def addTask():
    content = request.form['content']
    if (content == ''):
        return jsonify(result="fail", msg="no task was given")
    else:
        connection=pymysql.connect(host='localhost',user='root',db='td_list')
        with connection.cursor() as cursor:
            sql = "INSERT INTO `TO_DO` (`Item`) VALUES (%s)"
            cursor.execute(sql, (content))
            connection.commit()
        connection.close()
        return jsonify(result="success", task=content)
@app.route('/todo/read', methods=['GET'])
def fetchList():
    connection=pymysql.connect(host='localhost',user='root',db='td_list')
    with connection.cursor() as cursor:
        msql = "SELECT Item FROM TO_DO "
        cursor.execute(msql)
        
        result = cursor.fetchall()
        to_do=[]
        for x in result:
            for y in x:
                to_do.append(y)
    connection.close()
    return jsonify(result="success", data=to_do)
@app.route('/todo/update', methods=['PUT'])
def itemUpdate():
    connection=pymysql.connect(host='localhost',user='root',db='td_list')
    o_c = request.form['o_c']
    n_c = request.form['n_c']
    if (n_c == ''):
        return jsonify(result="fail", msg="no task was given")
    with connection.cursor() as cursor:
        msql = "SELECT ID FROM TO_DO WHERE Item = %s "
        cursor.execute(msql, o_c)
        result = cursor.fetchone()
        cursor.execute ("UPDATE TO_DO SET Item=%s WHERE ID=%s", (n_c,result))

    connection.commit()
        
    connection.close()
    return jsonify(result="success")
@app.route('/todo/delete', methods=['DELETE'])
def itemDelete():
    content = request.form['item']
    connection=pymysql.connect(host='localhost',user='root',db='td_list')
    with connection.cursor() as cursor:
         msql = "SELECT ID FROM TO_DO WHERE Item = %s "
         cursor.execute(msql, content)
         result = cursor.fetchone()
         print(result)
         sql= "DELETE FROM TO_DO WHERE ID= %s" 
         cursor.execute(sql,(result,))
         connection.commit()
    connection.close()
    return jsonify(result="success")





if __name__ == "__main__":
    app.run(host='0.0.0.0')
