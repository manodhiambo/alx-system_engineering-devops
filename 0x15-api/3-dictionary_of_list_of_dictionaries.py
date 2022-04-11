#!/usr/bin/python3
""" Program that Gather data from an API and Export to JSON
 all tasks from all employees"""
import json
import requests
# from sys import argv

if __name__ == "__main__":
    """ Program Entry point """
    empId = 1
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    # payload1 = {'userId': empId}
    # payload2 = {'id': empId}

    # req_todo = requests.get(url_todo)
    all_users = requests.get(url_user).json()

    # Getting the NUMBER_OF_DONE_TASKS and total tasks
    # total_tasks = req_todo.json()
    # Employee name from users
    # user_data = req_user.json()
    # emp_name = user_data[0].get('username')
    # list_dict = []
    user_tasks = {}

    for empId in range(1, len(all_users) + 1):
        req_todo = requests.get(url_todo, params={'userId': empId})
        req_user = requests.get(url_user, params={'id': empId})

        total_tasks = req_todo.json()
        user_data = req_user.json()
        list_dict = []
        emp_name = user_data[0].get('username')

        for task in total_tasks:
            task_info = {}
            task_info['task'] = task.get('title')
            task_info['completed'] = task.get('completed')
            task_info['username'] = emp_name
            list_dict.append(task_info)
        user_tasks[empId] = list_dict

    with open('todo_all_employees.json', 'w') as json_file:
        info = json.dumps(user_tasks)
        json_file.write(info)
