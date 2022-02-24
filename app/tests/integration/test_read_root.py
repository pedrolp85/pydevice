import os

from fastapi.testclient import TestClient
from main import app
from settings import Settings, get_settings
from unittest import mock
import pytest

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "This is the PyDevice API root dir "}