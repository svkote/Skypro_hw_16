from flask import render_template, jsonify
from config import app, db
from models import User, Offer, Order


@app.route('/users/', method=['GET'])
def get_users():
    """Возвращает весь список пользователей"""
    try:
        users = db.session.query(User).all()
        return jsonify([user.serialize() for user in users])
    except Exception as e:
        return f'{e}'


@app.route('/users/<int:user_id>', method=['GET'])
def get_users_by_id(user_id):
    """Возвращает весь список пользователей"""
    try:
        users = db.session.query(User).filter(User.id == user_id).first()
        return jsonify([user.serialize() for user in users])
    except Exception as e:
        return f'{e}'


@app.route('/orders/', method=['GET'])
def get_orders():
    """Возвращает весь список пользователей"""
    try:
        orders = db.session.query(Order).all()
        return jsonify([order.get_order() for order in orders])
    except Exception as e:
        return f'{e}'


@app.route('/orders/<int:order_id>', method=['GET'])
def get_orders_by_id(order_id):
    """Возвращает весь список пользователей"""
    try:
        orders = db.session.query(Order).filter(Order.id == order_id).first()
        return jsonify([order.get_order() for order in orders])
    except Exception as e:
        return f'{e}'


@app.errorhandler(404)
def route_not_found(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def internal_server_error(error):
    return f"На сервере произошла ошибка {error}", 500


if __name__ == '__main__':
    app.run(debug=True)
