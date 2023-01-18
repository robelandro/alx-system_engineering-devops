#!/usr/bin/python3
'''Module 1-export_to_CSV
Exports data got from API to CSV'''
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    user = requests.get(url).json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])
    tasks = requests.get(url).json()
    with open('{}.csv'.format(argv[1]), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([argv[1], user.get('username'),
                             task.get('completed'), task.get('title')])
