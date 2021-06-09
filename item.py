import sqlite3
from sqlite3.dbapi2 import Cursor
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required = True,
        help = "This field can't live empty")

    parser.add_argument('store_id',
        type=int,
        required = True,
        help = "Every item need a store id")

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message":"item not found"},404
    
    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':"an item with name '{}' allredy exists.".format(name)},400
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except Exception as error:
            print(error)
            return {"message":"An error occured at inserting time."},500
        return item.json(),201   

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':'Item delete'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        # updated_item = ItemModule(name,data['price'])
        if item is None:
            item = ItemModel(name,**data)
        else:
            item.price = data['price']
            
        item.save_to_db()
        return item.json(),201
        

class Itemslist(Resource):
    def get(self):
        return {"items":[item.json() for item in ItemModel.query.all()]}

    