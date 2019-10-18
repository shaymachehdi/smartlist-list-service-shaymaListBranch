from listservice import db
from datetime import datetime


class ListShared(db.Model):
    idListShared = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.idList'), nullable=True)
    group_id = db.Column(db.Integer, nullable=True)
    emailUser = db.Column(db.String(120), nullable=True)
    shared_at = db.Column(db.DateTime, default=datetime.utcnow)
    permission = db.Column(db.String(200))

    def __init__(self, list_id, group_id, emailUser, permission):
        self.list_id = list_id
        self.group_id = group_id
        self.emailUser = emailUser
        self.permission = permission


db.create_all()  # In case List table doesn't exists already. Else remove it