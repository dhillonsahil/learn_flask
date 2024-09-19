from flask import Flask,render_template,request,jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1492'
)

myCursor=mydb.cursor()

@app.route('/',methods=['GET','POST'])
def hello_world():
   return render_template('index.html')

@app.route('/math',methods=['POST'])    
def math_operation():
    if (request.method=='POST'):
        operation= request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=''
        match operation:
           case 'add':
               result= 'the sum of {} and {} is {}'.format(num1,num2,num1+num2);
           case 'subtract':
               result= 'the difference of {} and {} is {}'.format(num1,num2,num1-num2);
           case 'multiply':
               result= 'the product of {} and {} is {}'.format(num1,num2,num1*num2);
           case 'divide':
               result= 'the quotient of {} and {} is {}'.format(num1,num2,num1/num2);
           case 'log':
               result= 'the log of {} is {}'.format(num1,num1**num2);
           case _:
               result= 'something went wrong'
        return render_template('results.html',result=result)
               
           
    


@app.route('/sahil')
def myName():
    data = request.args.get('x')
    return "this is the request data {}".format(data)

@app.route('/users')
def allUsers():
    myCursor.execute('select * from milkmanage.users');
    myresult = myCursor.fetchall()
    print(myresult[0])
    return myresult

if __name__ == '__main__':
    app.run(host='0.0.0.0')
