from listservice import app, db
from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
import json
from listservice.listProduct.models import ListProduct

# Init bluebripnt
listProduct = Blueprint('listProduct', __name__)

# Init marshmallow
ma = Marshmallow(listProduct)


# TestClass schema
class ListProductSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('designation', 'barcode', 'qrcode', 'list_id')


# Init schema
listProduct_schema = ListProductSchema()
listsProduct_schema = ListProductSchema(many=True)


@listProduct.route('/listProduct', methods=['GET'])
def get_list_Products():
    all_list_of_products = ListProduct.query.all()
    result = listsProduct_schema.dump(all_list_of_products)
    return jsonify(result.data)


# # Create a list
#
# @listProduct.route('/listProduct/add', methods=['POST'])
# def add_list_product():
#     list_id = request.json['list_id']
#     product_id = request.json['product_id']
#
#     # Fetch porduct list
#     listProduct = ListProduct.query.filter_by(list_id=list_id, product_id=product_id).first()
#
#     if (condtion):
#         if listProduct is None:
#             list_id = request.json['list_id']
#             product_id = request.json['product_id']
#
#             new_list_product = ListProduct(list_id, product_id)
#
#             db.session.add(new_list_product)
#             db.session.commit()
#
#             return jsonify({
#                 'msg': 'New product list successfully created !',
#                 'isCreated': True
#             })
#
#         else:
#             return jsonify({
#                 'msg': 'you already registred that product list !',
#                 'isCreated': False
#             })
#
#     else:
#         return jsonify({
#                 'msg': 'Invalid product',
#                 'isCreated': False
#             })
#


# Deletes a product list

@listProduct.route('/listProduct/<int:idProduct>/<int:idList>', methods=['DELETE'])
def delete_list_product():
    list_id = request.json['list_id']
    product_id = request.json['product_id']

    # Fetch list
    listProduct = ListProduct.query.filter_by(list_id=list_id, product_id=product_id).first()

    if not listProduct:
        return jsonify({'msg': 'No product list found!',
                        'isDeleted': False})

    db.session.delete(list)
    db.session.commit()
    return jsonify({'msg': 'Product list successfully deleted!',
                    'isDeleted': True,
                    })
