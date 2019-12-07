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


def get_template_with_kafka(method, min_wait, max_wait, params, headers, body, kafka_bootstrap):
    template = f"""import json
from locust import HttpLocust, TaskSet, task, between
from kafka import KafkaProducer

kafka_producer = KafkaProducer(bootstrap_servers="",
                               value_serializer=lambda m: json.dumps(m, ensure_ascii=False).encode('utf-8'))

class WebsiteTasks(TaskSet):

    @task
    def index(self):
        response = self.client.{method}(url="", headers={headers}, params={params}, data={body})
        message = dict()
        messsage['status_code'] = response.status_code
        kafka_producer.send(topic, message)
    

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between({min_wait}, {max_wait})
"""
    return template
