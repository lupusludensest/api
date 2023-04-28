import requests
import uuid

ENDPOINT = "https://todo.pixegami.io"
# test_todo_api_28_apr_2023.py
# pytest test_todo_api_28_apr_2023.py
# python -m pytest
# python -m pytest -v
# python -m pytest -v -s

def test_can_create_task(): # python -m pytest -k test_can_create_task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    expected_status_code = 200
    assert create_task_response.status_code == expected_status_code, f'Error. Expected status code: {expected_status_code}, but actual status code: {create_task_response.status_code}'

    create_task_data = create_task_response.json()

    task_id = create_task_data["task"]['task_id']
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == expected_status_code, f'Error. Expected status code: {expected_status_code}, but actual status code: {get_task_response.status_code}'
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"], f'Error. Expected content: {payload["content"]}, but actual content: {get_task_data["content"]}'
    assert get_task_data["user_id"] == payload["user_id"], f'Error. Expected user_id: {payload["user_id"]}, but actual user_id: {get_task_data["user_id"]}'

def test_can_update_task(): # python -m pytest -k test_can_update_task
    expected_status_code = 200

    # create task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == expected_status_code, f'Error. Expected status code: {expected_status_code}, but actual status code: {create_task_response.status_code}'
    task_id = create_task_response.json()["task"]['task_id']

    # update the task
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my_updated_content",
        "is_done": True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200, f'Error. Expected status code: {expected_status_code}, but actual status code: {update_task_response.status_code}'

    # get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == expected_status_code, f'Error. Expected status code: {expected_status_code}, but actual status code: {get_task_response.status_code}'
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"], f'Error. Expected content: {new_payload["content"]}, but actual content: {get_task_data["content"]}'
    assert get_task_data["is_done"] == new_payload["is_done"], f'Error. Expected user_id: {new_payload["user_id"]}, but actual user_id: {get_task_data["user_id"]}'

def test_can_list_tasks(): # python -m pytest -v -s .\test_todo_api_28_apr_2023.py::test_can_list_tasks
    expected_status_code = 200
    # create N tasks
    n = 3
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == expected_status_code, f'Error. Expected status code: {expected_status_code}, but actual status code: {create_task_response.status_code}'

    # list tasks, and check that there are N items
    user_id = payload["user_id"]
    list_tasks_response = list_tasks(user_id)
    assert list_tasks_response.status_code == expected_status_code, f'Error. Expected status code: {expected_status_code}, but actual status code: {list_tasks_response.status_code}'
    data = list_tasks_response.json()

    tasks = data["tasks"]
    assert len(tasks) == n, f'Error. Expected {n} tasks, but actual: {len(tasks)}'

def test_can_delete_task(): # python -m pytest -v -s .\test_todo_api_28_apr_2023.py::test_can_delete_task
    expected_status_code = 200
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == expected_status_code, f'Error. Expected status code: {expected_status_code}, but actual status code: {create_task_response.status_code}'
    task_id = create_task_response.json()["task"]['task_id']

    # delete the task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == expected_status_code, f'Error. Expected status code: {expected_status_code}, but actual status code: {delete_task_response.status_code}'

    # get the task and check that it does not exist
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404, f'Error. Expected status code: 404, but actual status code: {get_task_response.status_code}'

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")


def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"my_test_content_{uuid.uuid4().hex}"

    return {
  "content": content,
  "user_id": user_id,
  "is_done": False,
    }





