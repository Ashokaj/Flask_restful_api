from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Security import authenticate, identity
from resouces.user import UserRegistator
from resouces.item import Item,Itemslist
from resouces.store import Store,StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'aj'
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app,authenticate,identity)

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')   
api.add_resource(Itemslist,'/items')
api.add_resource(StoreList,'/stores')   
api.add_resource(UserRegistator,'/registor')


if __name__ =='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug =True)