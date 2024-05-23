from . import multiply_bp
from flask import request, jsonify
from .multiply import multiply

@multiply_bp.route('/multiply',methods=['GET'])
def add_route():
    num1 = int(request.args.get('num1',0))
    num2 = int(request.args.get('num2',0))
    result = multiply(num1,num2)
    return jsonify({'result':result})
