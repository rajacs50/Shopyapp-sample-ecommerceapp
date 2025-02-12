from flask import Blueprint, jsonify, request
from .services import get_all_products, add_to_cart, get_cart, checkout
import sys

main = Blueprint('main', __name__)

@main.route('/api/products', methods=['GET'])
def get_products():
    products = get_all_products()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

@main.route('/api/cart', methods=['GET'])
def view_cart():
    return jsonify(get_cart())

@main.route('/api/cart', methods=['POST'])
def add_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    updated_cart = add_to_cart(product_id)
    return jsonify(updated_cart)

@main.route('/api/checkout', methods=['POST'])
def checkout_cart():
    total = checkout()
    return jsonify({'message': 'Checkout complete!', 'total': total})

@main.route("/api/error500", methods=["GET"])
def error_500():
    return jsonify({"error": "Internal Server Error"}), 500

@main.route("/api/error404", methods=["GET"])
def error_404():
    return jsonify({"error": "Not Found"}), 404

@main.route("/api/delay", methods=["GET"])
def delayed_response():
    import time
    time.sleep(1)  # Simulate a delay
    return jsonify({"message": "Delayed response"})

# Simulated endpoint for generating errors
@main.route("/api/simulate-error", methods=["GET"])
def simulate_error():
    error_type = request.args.get("type", "random")
    handle_exception('test error')
    if error_type == "random":
        # Randomly raise one of the following errors
        errors = [
            ValueError("This is a simulated ValueError."),
            KeyError("This is a simulated KeyError."),
            ZeroDivisionError("This is a simulated ZeroDivisionError."),
            Exception("This is a simulated general Exception."),
        ]
        raise random.choice(errors)
    elif error_type == "500":
        # Force a 500 Internal Server Error
        return "Simulated Internal Server Error", 500
    elif error_type == "404":
        # Force a 404 Not Found Error
        return "Simulated Not Found Error", 404
    else:
        # If no matching type, return bad request
        return "Invalid error type specified", 400

from app import db
@main.route('/api/simulate-db-slow', methods=['GET'])
def simulate_db_slow():
    query = "SELECT pg_sleep(5);"  # PostgreSQL-specific function to delay execution
    result = db.session.execute(query)
    return jsonify({"message": "Database query took too long"}), 200


# Catch and log all exceptions
def handle_exception(e):
    # Log the error details for debugging

    print("Error: Invalid input.", file=sys.stderr)
    raise ValueError
    sys.exit(1)
