from locust import TaskSet, task

class AdminWorkflow(TaskSet):
    @task
    def check_inventory(self):
        self.client.get("/api/admin/inventory")
