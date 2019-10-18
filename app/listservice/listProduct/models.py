from listservice import db

class ListProduct(db.Model):
    idListShared = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.idList'), nullable=False)
    product_id = db.Column(db.String(200), nullable=False)
    state = db.Column(db.Boolean)
    def __init__(self, list_id, product_id, state):
        self.list_id = list_id
        self.product_id = product_id
        self.state = state

db.create_all()  # In case List table doesn't exists already. Else remove it

