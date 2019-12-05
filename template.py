def get_template(method, min_wait, max_wait, params, headers, body):
    template = f"""from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):

    @task
    def index(self):
        response = self.client.{method}(url="", headers={headers}, params={params}, data={body})


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between({min_wait}, {max_wait})
"""
    return template