#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":


    base_url = (f"https://jsonplaceholder.typicode.com/")
    try:
        emp_id = int(argv[1])
    except Exception:
        exit()
    emp_response = requests.get(f"{base_url}/users/{emp_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={emp_id}")

    emp_data_json = emp_response.json()
    EMPLOYEE_NAME = emp_data_json.get("name")

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    for task in todos_response.json():
        TOTAL_NUMBER_OF_TASKS += 1
        if task.get("completed") is True:
            NUMBER_OF_DONE_TASKS +=1
            TASK_TITLE.append(task.get("title"))

    print("Employee {} is done with tasks ({}/{})".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    
    for task in TASK_TITLE:
        print(f"\t {task}")
