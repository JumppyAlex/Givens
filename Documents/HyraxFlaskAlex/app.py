from flask import *     # We import flask to VS code


#Create Flask App
app = Flask(__name__)
#We set session key 
app.secret_key= "Dub36%+ster"

#Add app features i.e Login , Register, Shopping......
@app .route('/hello')
def hello():
    return 'welcome to Flask Web'

@app.route('/about')
def about():
    return render_template('about.html')  #Link to HTML

@app.route('/help')
def help():
    return render_template('help.html')

#Default route
import pymysql
@app.route('/')
def home():

    #Create a connection database
    connection = pymysql.connect(host ='localhost',user='root', password='', database ='HyraxAlex')


    #Create an sql to get products 
    sql1="select * from products where product_category = 'detergents'"

    #Create a cursor -it will be used to RUN/EXECUTE SQL
    cursor1=connection.cursor()
    
    #RUN/EXECUTE SQL
    cursor1.execute(sql1)

    #How many products did Cursor  find
    detergents=cursor1.fetchall()    #Get a list of detergents
    #Take the laptops back to home.html
    
    #Select from another category
    sql2 ="select * from products where product_category='phones'"
    cursor2= connection.cursor()
    cursor2.execute(sql2)
    phones=cursor2.fetchall()

    #Select from another category
    sql3 ="select * from products where product_category='laptops'"
    cursor3= connection.cursor()
    cursor3.execute(sql3)
    laptops=cursor3.fetchall()

    #Select from another category
    sql4 ="select * from products where product_category='clothes'"
    cursor4= connection.cursor()
    cursor4.execute(sql4)
    clothes=cursor4.fetchall()




    return render_template('home.html',data=detergents,data2=phones,data3=laptops,data4=clothes
                           )


@app.route('/single/<product_id>')
def single(product_id):
    #Create a connection to the database 
    connection=pymysql.connect(host='localhost',user='root',password='',database='HyraxAlex')


    #Queryfrom database ,use the product_id
    #%s means it is a placeholder
    sql1="select * from products where product_id =%s"
    #Create a cursor to execute SQL
    cursor1=connection.cursor()
    #Execute SQL ,below product_id represent %s placeholder
    cursor1.execute(sql1,(product_id))
    
    #Fetch the product, its one product.
    product=cursor1.fetchone()

    #Above we have product,lets get the category
    category=product[4]
    sql2="select *from products where product_category=%s limit 4"
    cursor2=connection.cursor()
    cursor2.execute(sql2,(category))
    similar=cursor2.fetchall()

    #Lastly ,take the product_id to single.html
    return render_template('single.html',product=product,similar=similar)


@app.route('/signup',methods = ['POST','GET'])
def singup():
    if request.method =='POST':
        username=request.form['username']
        password=request.form['password']
        password2=request.form['password2']
        email=request.form['email']
        phone=request.form['phone']



        #Check if password are same 
        if password !=password2:
            return render_template('signup.html',message="Not Matching")
        
        elif len(password)<8:
            return render_template('signup.html',message="Must be 8 x-ters")
        
        else:
            connection =pymysql.connect(host='localhost',user='root',password='',database='HyraxAlex')

            #SQL
            sql1='''insert into users(username,password,email,phone)
            values(%s,%s,%s,%s)'''

            cursor1=connection.cursor()
            #Now execute your SQL provided real values to replace %s

            cursor1.execute(sql1,(username,password,email,phone))
            connection.commit()
            import sms
            sms.send_sms(phone,"Thank You for joining SokoGarden")
            #+254
            return render_template('signup.html',message="Success")
    
    else:   
        return render_template('signup.html',
                               message="Fill Details and submit")
    


@app.route('/signin', methods=['POST','GET'])
def signin ():
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']


        connection =pymysql.connect(host='localhost',user='root',password='',database='HyraxAlex')

        sql = "select  * from  users where username =%s and password =%s"
        cursor = connection .cursor()
        cursor.execute(sql,(username,password))

        if cursor.rowcount == 0:
            return render_template('/signin.html',message ='Incorrect!')
        
        else:
            #Its correct , take the user to Next Route
            session['key']=username #Each person a key with username
            return redirect('/')
    
    else:
        return render_template('signin.html',)
    


#Clear session - log out /sign out 
@app.route('/signout')
def signout():
    session.clear()
    return render_template('/signin')  #After signout go to login

      
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/mpesa', methods=['POST', 'GET'])
def mpesa_payment():
    if request.method == 'POST':
        phone = str(request.form['phone'])
        amount = str(request.form['amount'])
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return '<h3>Please Complete Payment in Your Phone and we will deliver in minutes</h3>' \
               '<a href="/" class="btn btn-dark btn-sm">Back to Products</a>'

     
@app.route('/vendors', methods=['POST','GET'])
def vendors ():
    if request.method == 'POST' :
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        county = request.form['county']
        password = request.form['password']
        password2 = request.form['password2']
        email = request.form['email']


       
         #Check if password are same 
        if password !=password2:
            return render_template('vendors.html',message="Not Matching")
        
        elif len(password)<8:
            return render_template('vendors.html',message="Must be 8 x-ters")
        
        else:
            connection =pymysql.connect(host='localhost',user='root',password='',database='HyraxAlex')

            #SQL
            sql1='''insert into vendors(firstname,lastname,county,password,password2,email,)
            values(%s,%s,%s,%s)'''

            cursor1=connection.cursor()
            #Now execute your SQL provided real values to replace %s

            cursor1.execute(sql1,(firstname,lastname,county,password,email,))
            connection.commit()
            #import sms
            #sms.send_sms(phone,"Thank You for joining SokoGarden")
            #+254
            return render_template('vendors.html',message="Success")
    
    else:
        return render_template('vendors.html',)
    


#TODO home route .This route will have products from DB
if __name__=='__main__':
    app.run(debug=True) # Debug is fixing errors in a code

#Always run the app.py .Then access the routes from  browser
#Base URL : http://127.0.0.1:5000
#coding .co.ke/notes
