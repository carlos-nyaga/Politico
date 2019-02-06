from flask import Blueprint

bp = Blueprint('api',__name__)

from .views import parties, offices
from .models import parties_models