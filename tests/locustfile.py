#!/usr/bin/env python

import random

from locust import TaskSet, task, HttpLocust

HTTP_URL = "http://0.0.0.0:5050/http://www.allitebooks.com/"
KEYWORD = ['python', 'php', 'go', 'java', 'c', 'c++', 'ruby', 'css', 'javascript', 'html', 'perl', 'c#', '.net']


class ITBooksBehavior(TaskSet):
    @task(2)
    def interface_1(self):
        print("{}?s={}".format(HTTP_URL, KEYWORD[random.randint(0, len(KEYWORD) - 1)]))
        self.client.get("{}?s={}".format(HTTP_URL, KEYWORD[random.randint(0, len(KEYWORD) - 1)]))


class ITBooks(HttpLocust):
    host = HTTP_URL
    task_set = ITBooksBehavior
    min_wait = 20
    max_wait = 100
