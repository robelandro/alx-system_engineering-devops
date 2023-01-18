#!/usr/bin/python3
'''Module 3-dictionary_of_list_of_dictionaries
Exports all users from the API to JSON file
'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()
    url = 'https://jsonplaceholder.typicode.com/todos'
    tasks = requests.get(url).json()
    # Create a dictionary with the user id as key and a list of
    # dictionaries as value
    users_tasks = {}
    for user in users:
        users_tasks[user.get('id')] = []
    for task in tasks:
        # Create a dictionary with the task information
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = users[task.get('userId') - 1].get('username')
        # Append the dictionary to the list of dictionaries
        users_tasks[task.get('userId')].append(task_dict)
    # Write the dictionary to a JSON file
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(users_tasks, jsonfile)
