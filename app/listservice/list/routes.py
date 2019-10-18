from listservice import app, db
from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
from listservice.list.models import List

# Init bluebripnt
list = Blueprint('list', __name__)

# Init marshmallow
ma = Marshmallow(list)


# List schema
class ListSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('designation', 'recurrence', 'created_at', 'device_id')


# Init schema
list_schema = ListSchema()
lists_schema = ListSchema(many=True)


@list.route('/list', methods=['GET'])
def get_all_list():
    all_list = List.query.all()
    result = lists_schema.dump(all_list)
    return jsonify(result.data)


# Create a list

@list.route('/list/add', methods=['POST'])
def add_list():
    designation = request.json['designation']
    device_id = request.json['device_id']

    # Fetch list
    list = List.query.filter_by(device_id=device_id, designation=designation).first()

    if list is None:
        designation = request.json['designation']
        recurrence = request.json['recurrence']
        device_id = request.json['device_id']

        new_list = List(designation, recurrence, device_id)

        db.session.add(new_list)
        db.session.commit()

        return jsonify({
            'msg': 'New list successfully created !',
            'isCreated': True})

    else:
        return jsonify({
            'msg': 'you already registred that list !',
            'isCreated': False
        })


# Update a list

@list.route('/list/<id>', methods=['PUT'])
def update_list(id):
    list = List.query.get(id)

    if not list:
        return jsonify({'msg': 'No list found!',
                        'isUpdated': False
                        })

    designation = request.json['designation']

    list.designation = designation

    db.session.commit()

    return jsonify({'msg': 'List successfully updated!',
                    'isUpdated': True,
                    'Designation': list.designation})


# Deletes a list

@list.route('/list/<id>', methods=['DELETE'])
def delete_list(id):
    list = List.query.get(id)
    if not list:
        return jsonify({'msg': 'No list found!',
                        'isDeleted': False})

    db.session.delete(list)
    db.session.commit()
    return jsonify({'msg': 'List successfully deleted!',
                    'isDeleted': True,
                    })


# Get all lists by device

@list.route('/list/<int:device_id>', methods=['GET'])
def get_list(device_id):
    # Fetch user
    list = List.query.filter_by(device_id=device_id).first()
    if not list:
        return jsonify({'msg': 'No list found for this device!',

                        })
    return list_schema.jsonify(list)


# Get Single List with device_id and designation
@list.route('/list/<int:device_id>/<string:designation>', methods=['GET'])
def get_user(device_id, designation):
    # Fetch list
    list = List.query.filter_by(designation=designation, device_id=device_id).first()
    if not list:
        return jsonify({'msg': 'No list found!'})
    return list_schema.jsonify(list)