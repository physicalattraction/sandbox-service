from locust import HttpUser, task


class SleepUser(HttpUser):
    @task
    def async_sleep(self):
        self.client.get('/api/async_sleep/')
