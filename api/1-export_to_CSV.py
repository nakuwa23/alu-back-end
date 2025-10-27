#!/usr/bin/python3
"""
Script that fetches an employee's TODO list from a REST API
and exports it to a CSV file.
"""
import csv
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
    username = user_data.get("username")

    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        sys.exit(1)

    todos_data = todos_response.json()

    filename = "{}.csv".format(employee_id)

    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
