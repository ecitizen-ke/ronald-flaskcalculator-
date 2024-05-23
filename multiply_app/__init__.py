from flask import Blueprint

multiply_bp =Blueprint('multiply_bp',__name__)

from . import  routes
