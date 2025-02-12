from config import API_ENDPOINTS

def browse_products(client):
    """Simulate browsing the product catalog."""
    response = client.client.get(API_ENDPOINTS["products"])
    if response.status_code == 200:
        print("Browsed products successfully.")
    else:
        print(f"Failed to browse products: {response.status_code}")
