#!/usr/bin/python3
""" Library to gather todo list from an API """

import urllib.request
import json

""" script to retrieve data from an API """


employee_id = int(input("Enter the employee ID: "))

# Make the API request to get the TODO list for the employee
url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
response = urllib.request.urlopen(url)
todos = json.loads(response.read())

# Filter completed tasks
completed_tasks = [todo for todo in todos if todo['completed']]

# Make another API request to get the employee's name
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = urllib.request.urlopen(url)
user = json.loads(response.read())
employee_name = user['name']

# Display the progress
total_tasks = len(todos)
completed_count = len(completed_tasks)
print(
    f"Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")

# Display the titles of completed tasks
for task in completed_tasks:
    print("\t", task['title'])
