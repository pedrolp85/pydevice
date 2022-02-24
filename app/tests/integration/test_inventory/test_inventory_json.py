import os

from fastapi.testclient import TestClient
from main import app
from model.device import Device
from settings import Settings, get_settings
from unittest import mock
import pytest


client = TestClient(app)

@pytest.fixture
def mock_env_var_json() -> None:
    with mock.patch.dict(os.environ, {"INVENTORY_SOURCE": "JSON", "INVENTORY_FILE_SOURCE": "tests/test_files/inventory"}):
        yield


def test_get_devices_json(mock_env_var_json):
    response = client.get("/device")
    assert response.status_code == 200
    assert len(response.json()) > 1
    assert response.json()[0]['name'] == "FW_INT1_json"

def test_get_device_json(mock_env_var_json):
    response = client.get("/device/2")
    assert response.status_code == 200
    assert response.json()['name'] == "BranchCSR1000v_json"

def test_create_device_json_successful(mock_env_var_json):
    devices_raw = client.get("/device")
    devices =  [ Device(**p) for p in devices_raw.json() ]
    last_number = (devices[-1]).id
    response = client.post("/device",
    json={
        "id": 100,
        "name": "FW_INT3_json",
        "manufacturer_id": 1,
        "model": "VM100",
        "state": "unknown",
        "mgmt_interface_id":7
        },
    )
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa")
    print(response.json())
    #assert response.status_code == 200
    assert response.json()['name'] == "FW_INT3_json"