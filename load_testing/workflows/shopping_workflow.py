from locust import TaskSet, task
from tasks.product_tasks import browse_products
from tasks.cart_tasks import add_to_cart, view_cart
from tasks.checkout_tasks import checkout
from tasks.delay import delay, db_slow
from tasks.error404 import error404
from tasks.error500 import error500
from tasks.random_error import random_error

class ShoppingWorkflow(TaskSet):
    @task(5)
    def browse(self):
        browse_products(self)

    @task(4)
    def add_to_cart(self):
        add_to_cart(self)

    @task(3)
    def checkout(self):
        checkout(self)
    
    @task(2)
    def delay(self):
        delay(self)

    @task(2)
    def db_slow(self):
        db_slow(self)

    @task(1)
    def error404(self):
        error404(self)

    @task(1)
    def error500(self):
        error500(self)

    @task(1)
    def random_error(self):
        random_error(self)