from flask_restful import Resource,reqparse
from models.user import UserModule
   

class UserRegistator(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username',
        type = str,
        required = True,
        help = "This should not live blank.")

    parser.add_argument('password',
        type = str,
        required = True,
        help = "This should not live blank.")

    def post(self):
        data = UserRegistator.parser.parse_args()
        if UserModule.find_by_username(data['username']):
            return {"message":"A user is allready existes"},401

        user = UserModule(**data)
        user.save_to_db()

        return {"message":"created user sucesfully"},201


