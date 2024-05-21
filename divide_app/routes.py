from . import divide_bp
from flask import request , jsonify
from .divide import divide

@divide_bp.route('/divide',methods=['GET'])
def divide_route():
    num1 = int(request.args.get('num1',0))
    num2 = int(request.args.get('num2',0))
    result = divide(num1,num2)
    return jsonify({'result':result})