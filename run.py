import argparse

from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


def read_key(key_path):
    with open(key_path) as f:
        key = f.read()
    return key

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--key_path', type=str, default='jwt-secret-string')
    args = parser.parse_args()


app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
if __name__ == "__main__":
    app.config['JWT_SECRET_KEY'] = read_key(args.key_path)


@app.after_request
def apply_caching(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = \
        'PUT, GET, POST, DELETE, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = \
        'Origin, Accept, Content-Type, Authorization'
    return resp


db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

if __name__ == "__main__":
    from run import app
    import src.models
    import src.views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
