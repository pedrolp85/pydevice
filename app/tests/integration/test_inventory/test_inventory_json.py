import os

from fastapi.testclient import TestClient
from main import app
from settings import Settings, get_settings
from unittest import mock
import pytest


client = TestClient(app)


def get_settings_override_json():
    return Settings(inventory_source="JSON", inventory_file_source="tests/test_files/inventory")

def test_get_devices_json():
    app.dependency_overrides[get_settings] = get_settings_override_json
    response = client.get("/device")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]['name'] == "FW_INT1_json"
    app.dependency_overrides = {}

def test_get_device_json():
    app.dependency_overrides[get_settings] = get_settings_override_json
    response = client.get("/device/2")
    assert response.status_code == 200
    assert response.json()['name'] == "BranchCSR1000v_json"
    app.dependency_overrides = {}


# def test_get_device_id_json():
#     response = client.get("/device/1")
#     assert response.status_code == 200
#     assert response.json() == {
#     "id": 1,
#     "name": "FW_INT1_json",
#     "manufacturer_id": 1,
#     "model": "VM100",
#     "state": None,
#     "mgmt_interface_id": 2
# }