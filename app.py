from flask import jsonify, request
from config import app, db
from migrate import init_database
from models import User, Offer, Order


@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    """Возвращает весь список пользователей"""
    if request.method == 'GET':
        try:
            users = db.session.query(User).all()
            return jsonify([user.serialize() for user in users])
        except Exception as e:
            return f'{e}'
    elif request.method == 'POST':
        data = request.json
        with db.session.begin():
            db.session.add(User(**data))
        return 'Успешно добавлен'


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_users_by_id(user_id):
    """Возвращает весь список пользователей"""
    data = request.json
    user = db.session.query(User).filter(User.id == user_id).first()

    if request.method == 'GET':
        try:
            return jsonify(user.serialize())
        except Exception as e:
            return f'{e}'

    elif request.method == 'PUT':
        if user is None:
            with db.session.begin():
                db.session.add(User(**data))
            return 'Успешно добавлен'
        else:
            with db.session.begin():
                db.session.query(User).filter(User.id == user_id).update(request.json)
            return 'Успешно обновлен'

    elif request.method == 'DELETE':
        if user is None:
            return 'Не найден'
        else:
            with db.session.begin():
                db.session.query(User).filter(User.id == user_id).delete()
            return 'Успешно Удален'


@app.route('/orders/', methods=['GET', 'POST'])
def get_orders():
    """Возвращает весь список пользователей"""
    if request.method == 'GET':
        try:
            orders = db.session.query(Order).all()
            return jsonify([order.get_order() for order in orders])
        except Exception as e:
            return f'{e}'
    elif request.method == 'POST':
        data = request.json
        with db.session.begin():
            db.session.add(Order(**data))
        return 'Успешно добавлен'


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_orders_by_id(order_id):
    """Возвращает весь список пользователей"""
    order = db.session.query(Order).filter(Order.id == order_id).first()
    data = request.json

    if request.method == 'GET':
        try:
            return jsonify(order.get_order())
        except Exception as e:
            return f'{e}'
    elif request.method == 'PUT':

        if order is None:
            with db.session.begin():
                db.session.add(Order(**data))
            return 'Успешно добавлен'
        else:
            with db.session.begin():
                db.session.query(Order).filter(Order.id == order_id).update(request.json)
            return 'Успешно обновлен'
    elif request.method == 'DELETE':

        if order is None:
            return 'Не найден'
        else:
            with db.session.begin():
                db.session.query(Order).filter(Order.id == order_id).delete()
            return 'Успешно Удален'


@app.route('/offers/', methods=['GET', 'POST'])
def get_offers():
    """Возвращает весь список пользователей"""
    if request.method == 'GET':
        try:
            offers = db.session.query(Offer).all()
            return jsonify([offer.get_offer() for offer in offers])
        except Exception as e:
            return f'{e}'
    elif request.method == 'POST':
        data = request.json
        with db.session.begin():
            db.session.add(Offer(**data))
        return 'Успешно добавлен'


@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offers_by_id(offer_id):
    """Возвращает весь список пользователей"""
    data = request.json
    offer = db.session.query(Offer).filter(Offer.id == offer_id).first()

    if request.method == 'GET':
        try:
            return jsonify(offer.get_offer())
        except Exception as e:
            return f'{e}'

    elif request.method == 'PUT':
        if offer is None:
            with db.session.begin():
                db.session.add(Offer(**data))
            return 'Успешно добавлен'
        else:
            with db.session.begin():
                db.session.query(Offer).filter(Offer.id == offer_id).update(request.json)
            return 'Успешно обновлен'

    elif request.method == 'DELETE':

        if offer is None:
            return 'Не найден'
        else:
            with db.session.begin():
                db.session.query(Offer).filter(Offer.id == offer_id).delete()
            return 'Успешно Удален'


@app.errorhandler(404)
def route_not_found(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def internal_server_error(error):
    return f"На сервере произошла ошибка {error}", 500


if __name__ == '__main__':
    with app.app_context():
        init_database()
    app.run(debug=True)
