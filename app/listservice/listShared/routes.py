from listservice import db
from flask import request, jsonify, Blueprint
from flask_marshmallow import Marshmallow
from listservice.listShared.models import ListShared

listShared = Blueprint('listShared', __name__)

# Init marshmallow
ma = Marshmallow(listShared)


# TestClass schema
class ListSharedSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('list_id', 'group_id', 'emailUser', 'shared_at', 'permission')


# Init schema
listShared_schema = ListSharedSchema()
listsShared_schema = ListSharedSchema(many=True)


# get all listShared
@listShared.route('/listShared', methods=['GET'])
def get_list_Shared():
    all_shared_list = ListShared.query.all()
    result = listsShared_schema.dump(all_shared_list)
    return jsonify(result.data)

# get all listShared by mail
@listShared.route('/listShared/<string:emailUser>', methods=['GET'])
def get_all_listShared_emailUser(emailUser):
    all_shared_list = ListShared.query.filter_by(emailUser=emailUser)
    result = listsShared_schema.dump(all_shared_list)
    return jsonify(result.data)

# get all listShared by list_id
@listShared.route('/listShared_list_id/<int:list_id>', methods=['GET'])
def get_all_listShared_list_id(list_id):
    all_shared_list = ListShared.query.filter_by(list_id=list_id)
    result = listsShared_schema.dump(all_shared_list)
    return jsonify(result.data)

# get all listShared by group_id
@listShared.route('/listShared_group_id/<int:group_id>', methods=['GET'])
def get_all_listShared_group_id(group_id):
    all_shared_list = ListShared.query.filter_by(group_id=group_id)
    result = listsShared_schema.dump(all_shared_list)
    return jsonify(result.data)






# get single listShared by id/mail
@listShared.route('/listShared/<int:list_id>/<string:emailUser>', methods=['GET'])
def get_id_mail_listShared(list_id, emailUser):

    listShared = ListShared.query.filter_by(list_id=list_id, emailUser=emailUser).first()

    if not listShared:
        return jsonify({'msg': 'No listShared found!'
                        })
    return listShared_schema.jsonify(listShared)







# add listShared
@listShared.route('/listShared/add', methods=['POST'])
def add_listShared():
    emailUser = request.json['emailUser']
    list_id = request.json['list_id']
    group_id = request.json['group_id']

    # can't insert both of emailUser and group_id
    if emailUser is None or group_id is None:

        listShared = ListShared.query.filter_by(emailUser=emailUser, list_id=list_id, group_id=group_id).first()

        if listShared is None:
            list_id = request.json['list_id']
            group_id = request.json['group_id']
            emailUser = request.json['emailUser']
            permission = request.json['permission']

            new_listShared = ListShared(list_id, group_id, emailUser, permission)

            db.session.add(new_listShared)
            db.session.commit()

            return jsonify({
                'isCreated': True,

                'msg': 'New list is successfully shared !'
            })


        else:
            if emailUser is None:

                msg = 'the list has been shared with this group!'
            else:
                msg = 'the list has been shared with!' + emailUser

            return jsonify({
                'isCreated': False,

                'msg': msg
            })
    else:
        return jsonify({
            "msg": "you can't share this list"
        })


# #delete ListShared
@listShared.route('/listShared/delete/<int:list_id>', methods=['DELETE'])
def delete_listShared(list_id):
    # fetch listShared
    listShared = ListShared.query.filter_by(list_id=list_id).first()

    if not listShared:
        return jsonify({'msg': 'No listShared found !'})

    db.session.delete(listShared)
    db.session.commit()

    return jsonify({
        'msg': 'listShared has been deleted !'
    })
