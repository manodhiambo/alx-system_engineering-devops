#!/usr/bin/python3
""" Program that Gather data from an API and Export to JSON """
import json
import requests
from sys import argv

if __name__ == "__main__":
    """ Program Entry point """
    empId = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    payload1 = {'userId': empId}
    payload2 = {'id': empId}

    req_todo = requests.get(url_todo, params=payload1)
    req_user = requests.get(url_user, params=payload2)

    # Getting the NUMBER_OF_DONE_TASKS and total tasks
    total_tasks = req_todo.json()
    # Employee name from users
    user_data = req_user.json()
    emp_name = user_data[0].get('username')
    list_dict = []
    user_tasks = {}

    with open('{}.json'.format(empId), 'w') as json_file:
        for task in total_tasks:
            task_info = {}
            task_info['task'] = task.get('title')
            task_info['completed'] = task.get('completed')
            task_info['username'] = emp_name
            list_dict.append(task_info)
        user_tasks[empId] = list_dict
        info = json.dumps(user_tasks)
        json_file.write(info)
