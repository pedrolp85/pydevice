import os

from fastapi.testclient import TestClient
from main import app
from settings import Settings, get_settings
from unittest import mock
import pytest


client = TestClient(app)


def get_settings_override_yaml():
    return Settings(inventory_source="YML", inventory_file_source="tests/test_files/inventory")

def test_get_devices_yaml():
    app.dependency_overrides[get_settings] = get_settings_override_yaml
    response = client.get("/device")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]['name'] == "FW_INT1_yaml"
    app.dependency_overrides = {}

def test_get_device_yaml():
    app.dependency_overrides[get_settings] = get_settings_override_yaml
    response = client.get("/device/2")
    assert response.status_code == 200
    assert response.json()['name'] == "BranchCSR1000v_yaml"
    app.dependency_overrides = {}