from locust import HttpUser, between
from workflows.shopping_workflow import ShoppingWorkflow
from workflows.admin_workflow import AdminWorkflow

class Shopper(HttpUser):
    wait_time = between(1, 3)
    tasks = [ShoppingWorkflow]

class Admin(HttpUser):
    wait_time = between(5, 10)
    tasks = [AdminWorkflow]
