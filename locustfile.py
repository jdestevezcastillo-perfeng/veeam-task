from locust import HttpUser, task, between # type: ignore

class ApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_endpoint(self):
          with self.client.get("/posts/1", catch_response=True) as response:
              # Standard status code assertion
              if response.status_code != 200:
                  response.failure(f"Status code = {response.status_code}")
                  
              # Assert missing data in response to show errors
              """ if "Hello" not in response.text:
                  response.failure("\"Hello\" is missing from the response") """
