from listservice import db
from datetime import datetime

class List(db.Model):
    idList = db.Column(db.Integer, primary_key=True)
    designation = db.Column(db.String(80), unique=True)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    recurrence = db.Column(db.String(200))
    listShared = db.relationship('ListShared', backref='list', lazy=True)
    listProduct = db.relationship('ListProduct', backref='list', lazy=True)
    productInvalid = db.relationship('ProductInvalid', backref='list', lazy=True)
    device_id = db.Column(db.Integer, nullable = False)
    def __init__(self, designation, recurrence, device_id):
        self.designation = designation
        self.recurrence = recurrence
        self.device_id = device_id

    def __repr__(self):
        return '<List %r>' % self.designation

db.create_all() # In case List table doesn't exists already. Else remove it