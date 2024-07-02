from flask import Blueprint,request, jsonify
from app.models.employee_model import Employee
from app.extension import db

employee_dp = Blueprint('employees',__name__)
employee_model = Employee()

@employee_dp.route('/show/employee', methods=['GET'])
def get_employee():
    employees = Employee.query.all()
    result = [{'id': employee.id, 'name': employee.name, 'email': employee.email} for employee in employees]
    return jsonify(result)


@employee_dp.route('/add/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(name=data['name'], email=data['email'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message':'employee added'}),201

@employee_dp.route('/delete/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'error': 'Employee not found'}), 404

    db.session.delete(employee)
    db.session.commit()
    
    return jsonify({'message': 'Employee deleted successfully'}), 200