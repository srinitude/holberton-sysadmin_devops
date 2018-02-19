#!/usr/bin/python3
"""
Populate a dictionary comprising values that are lists of dictionaries
"""
if __name__ == '__main__':
    import requests
    import json
    from collections import OrderedDict

    base_url = 'https://jsonplaceholder.typicode.com/'
    users_endpt = base_url + 'users'
    todos_endpt = base_url + 'todos'

    usernames = {}
    users = requests.get(users_endpt).json()
    for user in users:
        usernames[user.get('id')] = user.get('username')

    tasks = {}
    todos = requests.get(todos_endpt).json()
    for todo in todos:
        user_id = todo.get('userId')
        if user_id not in tasks:
            tasks[user_id] = []
        task = OrderedDict()
        task['username'] = usernames[user_id]
        task['task'] = todo.get('title')
        task['completed'] = todo.get('completed')
        tasks[user_id].append(task)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(tasks, f)
