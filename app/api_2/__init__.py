from flask import Blueprint

bp2 = Blueprint('api2',__name__)

from .views import user
