from flask import *
from flask_pymongo import PyMongo

app=Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb+srv://priyankapasupula:priyanka@cluster0.gppoy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db


@app.route('/Registration',methods=["POST"])
def Registration():
    Id=request.form['Id']
    Name=request.form['Name']
    ContactNumber=request.form['Contact Number']
    Password=request.form['Password']
    Gender=request.form['Gender']
    
    print("Id:",Id)
    print("Name:",Name)
    print("Contact Number:",ContactNumber)
    print("Password:",Password)
    print("Gender:",Gender)
    
    db.user.insert_one(dict(request.form))

    

    
    
    if __name__ == '__main__':
        app.run(debug = True)