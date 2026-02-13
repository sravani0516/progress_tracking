from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/api/tasks", json={
        "title": "Test Task",
        "description": "Testing",
        "completed": False
    })
    assert response.status_code == 201


def test_get_all_tasks():
    response = client.get("/api/tasks")
    assert response.status_code == 200


def test_update_task():
    # Create first
    create = client.post("/api/tasks", json={
        "title": "Update Test",
        "description": "Before",
        "completed": False
    })
    task_id = create.json()["id"]

    # Update
    response = client.put(f"/api/tasks/{task_id}", json={
        "title": "Updated",
        "description": "After",
        "completed": True
    })

    assert response.status_code == 200
    assert response.json()["completed"] == True


def test_delete_task():
    create = client.post("/api/tasks", json={
        "title": "Delete Test"
    })
    task_id = create.json()["id"]

    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 200


# -----------------------------
# Negative Tests
# -----------------------------

def test_create_without_title():
    response = client.post("/api/tasks", json={
        "description": "No title"
    })
    assert response.status_code == 422


def test_get_non_existing_task():
    response = client.get("/api/tasks/9999")
    assert response.status_code == 404


def test_invalid_data_type():
    response = client.post("/api/tasks", json={
        "title": "Invalid",
        "description": "Test",
        "completed": "yes"   # invalid because StrictBool
    })
    assert response.status_code == 422
