#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(url).json()
    user_name = user_response.get('name')

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todo_response = requests.get(todo_url).json()

    completed_tasks = [task for task in todo_response if task.get('completed')]
    total_tasks = len(todo_response)
    completed_tasks_count = len(completed_tasks)

    print(f"Employee {user_name} is done with tasks({completed_tasks_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
