def add_to_cart(client):
    response = client.client.get("/api/products")
    if response.status_code == 200:
        products = response.json()
        if products:
            product_id = products[0]['id']  # Pick the first product
            client.client.post("/api/cart", json={"product_id": product_id})

def view_cart(client):
    client.client.get("/api/cart")
