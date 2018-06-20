import argparse
from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from src.models import db
from src.views import add_resources


app = Flask(__name__)
api = Api(app)
add_resources(api)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
jwt = JWTManager(app)


def read_key(key_path):
    with open(key_path) as f:
        key = f.read().rstrip()
    return key


@app.after_request
def apply_caching(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = \
        'PUT, GET, POST, DELETE, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = \
        'Origin, Accept, Content-Type, Authorization'
    return resp


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key_path', type=str, default='data/jwt.key')
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    app.config['JWT_SECRET_KEY'] = read_key(args.key_path)
    app.run(host='0.0.0.0', port=args.port)
