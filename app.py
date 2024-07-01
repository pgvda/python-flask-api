from flask import Flask, jsonify, request
from flask_mysqldb import MySQL



employees = [{'id':1, 'name':'vidusha'},{'id':2, 'name':'shashini'}]
menus = [{'MenuItemID': 1, 'itemName':'item1', 'price':'Rs.100'}]
orders=[{'order_ID':1, 'total':'RS.200'}]
customer=[{'customer_ID':1, 'customer_name':'dilshan','contact':'076-xxxxxxx'}]

def employee_is_valid(employee):
    required_fields = ['name']
    for field in required_fields:
        if field not in employee:
            return False
    return True


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'resturent'
mysql = MySQL(app)

# @app.route('/')
# def hello():
#     return "Hello, World!"



@app.route('/employee', methods=['GET'])
def get_employee():
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/register-employee', methods=['POST'])
def create_employee():
    global nextEmployeeId
    employee = json.loads(request.data)
    if not employee_is_valid(employee):
        return jsonify({'error': 'invalid employee '}),400
    
    employee['id'] = nextEmployeeId
    nextEmployeeId +=1
    employees.append(employee)

    return '', 201, {'location': f'/employees/{employee["id"]}'}

#Menu

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menus)

@app.route('/new/menu', methods=['POST'])
def create_new_menu():
    return jsonify({'new menu added'})
    

#order

@app.route('/order',methods=['GET'])
def get_order():
    return jsonify(orders)