import random

def random_product_id(products):
    return random.choice(products)['id'] if products else None
