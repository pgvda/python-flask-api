from flask_marshmallow import Marshmallow


ma = Marshmallow()




class CustomerSchema(ma.Schema):
   class Meta:
       fields = ('id', 'name', 'email')
admin_schema = AdminSchema()

