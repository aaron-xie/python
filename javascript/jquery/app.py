#安装flask: python pip install flask pymysql
#pip 在python3.4+自带
from flask import Flask
from flask import request
import json
import pymysql

  #json操作
  #json.dumps()   object->json
  #json.loads()   json->object

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/api', methods=['GET', 'POST'])
def api():
    data = {"spam" : "foo", "parrot" : 42}
    in_json = json.dumps(data) # Encode the data
    return in_json

@app.route('/datalist', methods=['GET', 'POST'])
def datalist():
    # 打开数据库连接
    # db = pymysql.connect('localhost','root','','jiaoxue')
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='jiaoxue',charset='utf8')
 
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
     
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("select * from goods")
     
    # 使用 fetchone() 方法获取单条数据.
    # fetall()获取所有数据
    # data = cursor.fetchone()
    data = cursor.fetchall()

    # print(data);
     
    # 关闭数据库连接
    db.close()

    jsonData = []
    for row in data:  
            result = {} 
            result['id'] = row[0]  
            result['name'] = row[1]  
            result['price'] = row[2]  
            result['color'] = str(row[3])   
            result['size'] = str(row[4])   
            result['imgurl'] = str(row[5])   
            result['category'] = row[6]  
            result['createtime'] = row[7]  
            jsonData.append(result)
            # print u'转换为列表字典的原始数据：',jsonData

    # print(jsonData)
    # data->json
    in_json = json.dumps(jsonData) # Encode the data
    return in_json




if __name__ == '__main__':
    app.run()