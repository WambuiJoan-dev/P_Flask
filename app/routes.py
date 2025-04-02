#for url definitions and view functions

from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Hello!'