## Added another endpoint and included typical assertions in both
from locust import HttpUser, task, between # type: ignore

class ApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def GET_Post_Details(self):
        with self.client.get("/posts/1", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"{response.status_code}")
            if "userId" not in response.text:
                response.failure("Response doesn't contain \"userId\". \
                    Body might be empty or return incorrect content")
    
    @task
    def GET_Post_List(self):
        with self.client.get("/posts", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"{response.status_code}")
            if "userId" not in response.text:
                response.failure("Response doesn't contain \"userId\". \
                    Body might be empty or return incorrect content")
        