#!/usr/bin/python3
<<<<<<< HEAD
"""create flask app blueprint"""
=======
"""the init file"""
>>>>>>> 0acdfdd76635065400801bf29961a2c12c44f730
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
