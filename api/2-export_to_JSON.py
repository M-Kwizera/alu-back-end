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

    # Create a dictionary to store the TODO list progress
    todo_progress = {
        "employee_name": employee_name,
        "completed_tasks": completed_tasks,
        "total_tasks": len(todos),
        "completed_count": len(completed_tasks)
    }

    # Export the TODO list progress to a JSON file
    filename = f"employee_{employee_id}_todos.json"
    with open(filename, 'w') as file:
        json.dump(todo_progress, file, indent=4)

    print(f"TODO list progress exported to {filename} successfully.")
