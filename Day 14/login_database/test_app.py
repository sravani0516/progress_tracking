# test_app.py

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# -------------------------
# Backend Logic Testing
# -------------------------
def test_login_success(client):
    response = client.post("/login", data={
        "username": "admin",
        "password": "1234"
    })

    assert b"Login Successful" in response.data


def test_login_failure(client):
    response = client.post("/login", data={
        "username": "admin",
        "password": "wrong"
    })

    assert b"Invalid Credentials" in response.data
