import json
from flask import Response
from flask_restful import Resource, reqparse
from src.models import UserModel
from flask_jwt_extended import create_access_token, jwt_required

parser = reqparse.RequestParser()
parser.add_argument('username',
                    help='This field cannot be blank', required=True)
parser.add_argument('password',
                    help='This field cannot be blank', required=True)


def create_response(body):
    resp = Response(json.dumps(body))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] =\
        'PUT, GET, POST, DELETE, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] =\
        'Origin, Accept, Content-Type, Authorization'
    return resp


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return create_response({'message':
                                    'User {} already exists'
                                    .format(data['username'])})

        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password'])
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=data['username'],
                                               expires_delta=False)
            return create_response({
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token
            })
        except Exception:
            return {'message': 'Something went wrong'}, 500

    def option(self):
        return create_response({})


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])

        if not current_user:
            return create_response({'message':
                                    'User {} doesn\'t exist'
                                     .format(data['username'])})

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'],
                                               expires_delta=False)
            return create_response({
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token})
        else:
            return create_response({'message': 'Wrong credentials'})

    def option(self):
        return create_response({})


class SecretResource(Resource):
    @jwt_required
    def get(self):
        return create_response({'valid': True})

    def option(self):
        return create_response({})
