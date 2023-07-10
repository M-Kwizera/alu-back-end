#!/usr/bin/python3
""" gets to export
list back from an API """


import json
import requests
import sys

if __name__ == "__main__":
    user_link = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    user_response = requests.get(user_link)
    user_data = json.loads(user_response.text)

    employee_id = sys.argv[1]
    todos_link = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)
    todos_response = requests.get(todos_link)
    todos_data = json.loads(todos_response.text)

    completed_tasks = []
    for task in todos_data:
        if task['completed']:
            completed_tasks.append(task)

    print("Employee {} is done with tasks ({}/{}):".format(
        user_data['name'], len(completed_tasks), len(todos_data)))

    for task in completed_tasks:
        print("\t{}".format(task["title"]))
