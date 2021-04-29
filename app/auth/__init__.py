from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import *
from .views import *
from . import forms