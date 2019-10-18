from listservice import app,db
from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
import json
from listservice.productInvalid.models import ProductInvalid

# Init bluebripnt
productsInvalid = Blueprint('productsInvalid', __name__)

# Init marshmallow
ma = Marshmallow(productsInvalid)

# TestClass schema
class ProductInvalidSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('designation', 'barcode', 'qrcode', 'list_id')

# Init schema
productinvalid_schema = ProductInvalidSchema()
productsinvalid_schema = ProductInvalidSchema(many=True)

@productsInvalid.route('/prodcutsInvalid', methods=['GET'])
def get_products_invalid():
    all_products_invalid =ProductInvalid.query.all()
    result = productsinvalid_schema.dump(all_products_invalid)
    return jsonify(result.data)
