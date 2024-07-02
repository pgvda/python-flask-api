from flask import Blueprint, request, jsonify
from app.models.customer_model import Customer
from app.extension import db

customer_bp = Blueprint('customers', __name__)

@customer_bp.route('/show/customer', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    result = [{'id': customer.id, 'name': customer.name, 'email': customer.email} for customer in customers]
    return jsonify(result)

@customer_bp.route('/add/customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], email=data['email'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer added!'}), 201

@customer_bp.route('/delete/customer/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    db.session.delete(customer)
    db.session.commit()
    
    return jsonify({'message': 'Customer deleted successfully'}), 200