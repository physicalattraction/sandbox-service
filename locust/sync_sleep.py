from locust import HttpUser, task


class SleepUser(HttpUser):
    @task
    def sync_sleep(self):
        self.client.get('/api/sync_sleep/')
