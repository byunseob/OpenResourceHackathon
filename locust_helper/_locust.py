from locust import HttpLocust, TaskSet, task, between
class WebsiteTasks(TaskSet):

    @task
    def index(self):
        response = self.client.get(url="", headers=None, params={'name': 'byunseob'}, data=None)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(1, 1)
