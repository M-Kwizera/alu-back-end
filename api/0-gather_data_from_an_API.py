#!/usr/bin/python3
""" gets todo 
list back from an API """

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    user_response = requests.get(user_url)
    user = json.loads(user_response.text)

    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)
    todos_response = requests.get(todos_url)
    todos = json.loads(todos_response.text)

    completed_tasks = [todo for todo in todos if todo['completed']]

    print("Employee {} is done with tasks ({}/{})".format(
        user['name'], len(completed_tasks), len(todos)))

    for task in completed_tasks:
        print("\t{}".format(task["title"]))
