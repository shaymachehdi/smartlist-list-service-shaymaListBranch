from listservice import db

class ProductInvalid(db.Model):
    idProductInvalid = db.Column(db.Integer, primary_key=True)
    designation = db.Column(db.String(200))
    qrcode = db.Column(db.String(150), unique=True)
    barcode = db.Column(db.String(150), unique=True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.idList'), nullable=False)

    def __init__(self, designation, qrcode,barcode, list_id):
        self.designation = designation
        self.barcode = barcode
        self.qrcode = qrcode
        self.list_id = list_id

    def __repr__(self):
        return '<ProductInvalid %r>' % self.designation

db.create_all() # In case user table doesn't exists already. Else remove it
