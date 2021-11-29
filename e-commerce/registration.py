from itertools import product
from os import name
from flask import *
from flask_pymongo import PyMongo

app=Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb+srv://priyankapasupula:priyanka@cluster0.gppoy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db


@app.route('/Registration',methods=["POST"])
def Registration():
    if request.method=='POST':
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
    if(len(name)>0 and len(Password)>0 and len(ContactNumber)>0):  
        db.user.insert_one(dict(request.form))
        return redirect(url_for('success'))
    else:
        return redirect(url_for('error')) 

    @app.route('/login',methods=["GET"])
    def login():
        Id=request.form['Id']
        Password=request.form['Password']

        print("Id:",Id)
        print("Password:",Password)

        db.user.find(dict(request.form))


    @app.route('/Reset password',methods=["PATCH"])   
    def ResetPassword():
        ContactNumber=request.form['contactNumber']
        Password=request.form['Password']

        print("ContactNumber:",ContactNumber)
        print("Password:",Password)

        db.user.update_one(dict(request.form))
    
    
    @app.route('/Getproduct',methods=["GET"])
    def Getproduct():
        Id=request.form['Id']
        product_name=request.form['product_name']
        product_price=request.form['product_price'] 
        product_image=request.form['product_image']
        product_description=request.form['product_description']

        print("Id:",Id)
        print("product_name:",product_name)
        print("product_price:",product_price)
        print("product_image:",product_image)
        print("product_description:",product_description)

        db.user.update_one(dict(request.form))
    

    @app.route('/Jewellery',methods=["GET"])
    def Jewellery():
        Id=request.form['Id']
        Jewellery_name=request.form['Jewellery_name']
        Jewellery_price=request.form['Jewellery_price'] 
        Jewellery_image=request.form['Jewellery_image']
        Jewellery_description=request.form['Jewellery_description']

        print("Id:",Id)
        print("Jewellery_name:",Jewellery_name)
        print("Jewellery_price:",Jewellery_price)
        print("Jewellery_image:",Jewellery_image)
        print("Jewellery_description:",Jewellery_description)

        db.user.update_one(dict(request.form))

@app.route('/Gadget',methods=["GET"])
def Gadget():
        Id=request.form['Id']
        Gadget_name=request.form['Gadget_name']
        Gadget_price=request.form['Gadget_price'] 
        Gadget_image=request.form['Gadget_image']
        Gadget_description=request.form['Gadget_description']

        print("Id:",Id)
        print("Gadget_name:",Gadget_name)
        print("Gadget_price:",Gadget_price)
        print("Gadget_image:",Gadget_image)
        print("Gadget_description:",Gadget_description)

        db.user.update_one(dict(request.form))


@app.route('/Delete user account',methods=["DELETE"])
def Deleteuseraccount():
    Id=request.form['Id']

    print("Id:",Id)

    db.user.update_one(dict(request.form))

    if __name__ == '__main__':
        app.run(debug = True)