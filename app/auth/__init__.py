from flask import Blueprint

# auth blueprint
auth = Blueprint('auth',__name__)

from . import views,forms