from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'


db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)


from src.run import app
import src.models
import src.views


app.run(host='0.0.0.0', port="5000")
