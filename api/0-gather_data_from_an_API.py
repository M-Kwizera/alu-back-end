#!/usr/bin/python3
""" gets todo
list back from an API """


import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Make the API request to get the TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todos_url)
    todos = json.loads(response.text)

    # Filter completed tasks
    completed_tasks = [task for task in todos if task['completed']]

    # Make another API request to get the employee's name
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    user = json.loads(response.text)
    employee_name = user['name']

    # Display the progress
    total_tasks = len(todos)
    completed_count = len(completed_tasks)
    print(
        f"Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")

    # Display the titles of completed tasks
    for task in completed_tasks:
        print("\t" + task["title"])
