#We will create an API  for Employee Management System
#Our API will have POST,GET,PUT,DELETE
from flask import*
from flask_restful import Resource,Api
import pymysql
import pymysql.cursors
#Create a Flask App
app = Flask(__name__)

#We convert above app to an API
api = Api(app)

#We create an API For Employee
class Employee(Resource):
    #We do POST,GET,PUT,DELETE.
    def post (self):
        data = request.json
        id_number = data['id_number']
        username = data['username']
        others = data['others']
        salary = data['salary']
        department = data['department']

        #Connect to DB
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    database='HYRAX API')
        
        #Cursor and SQL
        cursor = connection.cursor()
        sql = '''insert into employees(id_number,username,others,salary,department)values(%s,%s,%s,%s,%s)'''


        try:
            cursor.execute(sql,(id_number,username,others,salary,department))
            connection.commit()
            return jsonify({'message':'Saved Successfully'})
        except:
                return jsonify({'message':'Failed'})


    
    def get (self):
         connenction = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='HYRAX API')
         
         sql = "select * from employees"
         cursor  = connenction.cursor(pymysql.cursors.DictCursor)
         cursor.execute(sql)
         if cursor.rowcount == 0:
              return jsonify({'message':'No Empployees'})
         else:
              employees = cursor.fetchall()
              return jsonify(employees)
    
    def put (self):
        data = request.json
        id_number = data['id_number']
        salary = data['salary']
        connenction = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='HYRAX API')
        cursor =connenction.cursor()
        sql = "update employees set salary = %s  where id_number =%s"
        cursor.execute(sql,(salary,id_number))
        connenction.commit()
        return jsonify({'message':'Update Successful'})
        
        
        s
    
    def delete(self):
        data = request.json
        id_number = data['id_number']
        connenction = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='HYRAX API')
        cursor =connenction.cursor()
        sql = "delete from  employees   where id_number =%s"
        cursor.execute(sql,(id_number))
        connenction.commit()
        return jsonify({'message':'Deleted Successful'})
    



#We create a link to access out API
api.add_resource(Employee,'/employees')

#RUN APP
if __name__ == '__main__':
    app.run(debug=True)








