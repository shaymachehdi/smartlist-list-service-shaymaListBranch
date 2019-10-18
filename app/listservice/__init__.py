from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/testdb' #in local environement
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@mysql/list_ms_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'shhhh...iAmASecret!'
db = SQLAlchemy(app)

# Init marshmallow
ma = Marshmallow(app)

from listservice.list.routes import list
app.register_blueprint(list)

from listservice.productInvalid.routes import productsInvalid
app.register_blueprint(productsInvalid)

from listservice.listProduct.routes import listProduct
app.register_blueprint(listProduct)

from listservice.listShared.routes import listShared
app.register_blueprint(listShared)

