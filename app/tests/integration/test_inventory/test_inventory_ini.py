import os

from fastapi.testclient import TestClient
from main import app
from settings import Settings, get_settings
from unittest import mock
import pytest


client = TestClient(app)


def get_settings_override_ini():
    return Settings(inventory_source="INI", inventory_file_source="tests/test_files/inventory")

def test_get_devices_ini():
    app.dependency_overrides[get_settings] = get_settings_override_ini
    response = client.get("/device")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]['name'] == "FW_INT1_INI"
    app.dependency_overrides = {}

def test_get_device_ini():
    app.dependency_overrides[get_settings] = get_settings_override_ini
    response = client.get("/device/2")
    assert response.status_code == 200
    assert response.json()['name'] == "BranchCSR1000v_INI"
    app.dependency_overrides = {}

def test_create_device_ini():
    app.dependency_overrides[get_settings] = get_settings_override_ini
    response = client.post("/device/",
    json={
        "id": 4,
        "name": "FW_INT3_json",
        "manufacturer_id": 1,
        "model": "VM100",
        "mgmt_interface_id":7
        }
    )
    assert response.status_code == 307
    app.dependency_overrides = {}