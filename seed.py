from app import create_app, db
from app.models import Product

app = create_app()

with app.app_context():
    db.create_all()
    products = [
        Product(name="Laptop", price=999.99),
        Product(name="Phone", price=499.99),
        Product(name="Headphones", price=149.99),
        Product(name="Computer", price=1049.99),
        Product(name="Accessories Pack", price=99.99),

    ]
    db.session.bulk_save_objects(products)
    db.session.commit()
