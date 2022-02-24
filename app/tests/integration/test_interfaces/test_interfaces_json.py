import os

from fastapi.testclient import TestClient
from main import app
from settings import Settings, get_settings
from unittest import mock
import pytest


client = TestClient(app)


def get_settings_override_interfaces_json():
    return Settings(interfaces_source="JSON", interfaces_file_source="tests/test_files/interfaces")

def test_get_interfaces_json():
    app.dependency_overrides[get_settings] = get_settings_override_interfaces_json
    response = client.get("/interface")
    assert response.status_code == 200
    assert len(response.json()) == 6
    assert response.json()[0]['name'] == "mgmt0_json"
    app.dependency_overrides = {}

def test_get_interface_json():
    app.dependency_overrides[get_settings] = get_settings_override_interfaces_json
    response = client.get("/interface/2")
    assert response.status_code == 200
    assert response.json()['name'] == "eth1/1_json"
    app.dependency_overrides = {}
