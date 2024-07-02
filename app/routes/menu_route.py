from flask import Blueprint, request, jsonify
from app.models.menu_model import Menu
from app.extension import db

menu_dp = Blueprint('menu', __name__)
menu_model = Menu()

@menu_dp.route('/show/menu', methods=['GET'])
def get_menues():
    menues = Menu.query.all()
    result = [{'id': menu.id, 'name': menu.name, 'price': menu.price} for menu in menues]
    return jsonify(result)

@menu_dp.route('/add/menu', methods=['POST'])
def add_menu():
    data = request.get_json()
    new_menu = Menu(name=data['name'], price=data['price'])
    db.session.add(new_menu)
    db.session.commit()
    return jsonify({'message': 'Menu added!'}), 201

@menu_dp.route('/delete/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    menu = Menu.query.get(id)
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    db.session.delete(menu)
    db.session.commit()
    
    return jsonify({'message': 'Menu deleted successfully'}), 200


@menu_dp.route('/edit/menu/<int:id>', methods =['PUT'])
def update_menu(id):
    menu = Menu.query.get(id)
    # print("menu is",id)
    if not menu:
        return jsonify({'message': 'no such menu found'}), 404
    
    
    data = request.get_json()


    menu.name = data.get('name', menu.name)
    menu.price = data.get('price', menu.price)
 
    try:
        db.session.commit()
        return jsonify({'message': 'menu updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to update menu', 'error': str(e)}), 500