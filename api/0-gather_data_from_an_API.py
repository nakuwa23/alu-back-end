#!/usr/bin/python3
"""
Script that fetches and displays an employee's TODO list progress
from a REST API given their employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        sys.exit(1)

    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))