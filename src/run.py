import argparse

from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


def read_key(key_path):
    with open(key_path) as f:
        key = f.read().rstrip()
    return key


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key_path', type=str, default='data/jwt.key')
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()


app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = \
    'eea637dfa8c5da0db6740b4b5708ee7aecc1d5f9f830d1ce7ab9df480bace474d8db8484b84ee'\
    '4b16e8fbb490e0ac519caaec508379622abe051ba2a9dcda431'

if __name__ == "__main__":
    app.config['JWT_SECRET_KEY'] = \
        'eea637dfa8c5da0db6740b4b5708ee7aecc1d5f9f830d1ce7ab9df480bace474d8db8484b84ee'\
        '4b16e8fbb490e0ac519caaec508379622abe051ba2a9dcda431'
    # read_key(args.key_path)


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
    from src.run import app
    import src.models
    import src.views

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port)
