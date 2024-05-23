from flask import Blueprint

subtract_bp =Blueprint('subtract_bp',__name__)

from . import  routes
