from flask import Blueprint

bp2 = Blueprint('api2',__name__)


from .views import users, parties, candidates, offices
from .models import user_models

