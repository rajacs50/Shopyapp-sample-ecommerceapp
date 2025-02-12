from .models import Product, db

cart = []  # Simple in-memory cart for demonstration purposes

def get_all_products():
    return Product.query.all()

def add_to_cart(product_id):
    product = Product.query.get(product_id)
    if product:
        cart.append({'id': product.id, 'name': product.name, 'price': product.price})
    return cart

def get_cart():
    return cart

def checkout():
    total = sum(item['price'] for item in cart)
    cart.clear()
    return total
