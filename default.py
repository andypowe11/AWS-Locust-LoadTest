from locust import HttpLocust, TaskSet

def home(l):
    l.client.get("/", verify=0, name="/")

def business(l):
    l.client.get("/business", verify=0, name="/business")


class UserBehavior(TaskSet):
    tasks = {home:10, business:5}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=10000
