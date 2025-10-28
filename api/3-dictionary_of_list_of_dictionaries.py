#!/usr/bin/python3
"""
Script that fetches all employees' TODO lists from a REST API
and exports them to a JSON file.
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_url = "{}/users".format(base_url)
    users_response = requests.get(users_url)

    if users_response.status_code != 200:
        exit(1)

    users_data = users_response.json()

    todos_url = "{}/todos".format(base_url)
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        exit(1)

    todos_data = todos_response.json()

    all_employees_data = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = []
        for task in todos_data:
            if task.get("userId") == user_id:
                task_dict = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                user_tasks.append(task_dict)

        all_employees_data[user_id] = user_tasks

    filename = "todo_all_employees.json"

    with open(filename, mode='w') as json_file:
        json.dump(all_employees_data, json_file)
