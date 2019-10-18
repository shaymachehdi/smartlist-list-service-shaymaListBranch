from listservice import app,db
"""from listservice.productInvalid.models import ProductInvalid
p = ProductInvalid('adfsgaea', 'dfgfdvcgfgdfdsggfdg','1234dfg56vc789')
db.session.add(p)
db.session.commit() # This is needed to write the changes to database
ProductInvalid.query.all()
ProductInvalid.query.filter_by(designation='aaa').first()"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
