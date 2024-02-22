#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user = requests.get(url + "users/{}".format(employee_id)).json()
    # Fetch TODOs for the user
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Filter out completed tasks
    completed = [t.get("title") for t in todos if t.get("completed")]

    # Display the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for task in completed:
        print("\t {}".format(task))
