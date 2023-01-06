from flask import render_template, jsonify
from config import app, db
from models import User, Offer, Order


@app.route('/users/', method=['GET'])
def get_users():
    """Возвращает весь список пользователей"""
    users = db.session.query(User).all()
    return jsonify([user.serialize() for user in users])


@app.errorhandler(404)
def route_not_found(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def internal_server_error(error):
    return f"На сервере произошла ошибка {error}", 500


if __name__ == '__main__':
    app.run(debug=True)
