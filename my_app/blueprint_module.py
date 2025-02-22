from flask import Blueprint

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def home():
    return "Hello, World!" 