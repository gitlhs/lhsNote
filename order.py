from flask import Blueprint
order = Blueprint("order",__name__)

@order.route('/order')
def register():   
    return "order