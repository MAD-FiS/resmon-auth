from flask import jsonify
import src.resources


def add_resources(api):
    api.add_resource(src.resources.Index, '/')
    api.add_resource(src.resources.UserRegistration, '/registration')
    api.add_resource(src.resources.UserLogin, '/login')
    api.add_resource(src.resources.SecretResource, '/secret')
