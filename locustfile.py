from locust import HttpUser, task, between # type: ignore

class ApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_endpoint(self):
          self.client.get("/posts/1")
