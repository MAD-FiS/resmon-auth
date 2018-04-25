from src.run import app, api
from flask import jsonify
import src.resources


@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})


api.add_resource(src.resources.UserRegistration, '/registration')
api.add_resource(src.resources.UserLogin, '/login')
api.add_resource(src.resources.SecretResource, '/secret')