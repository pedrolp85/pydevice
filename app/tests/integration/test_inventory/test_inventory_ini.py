import os

from unittest import mock
from fastapi.testclient import TestClient
from main import app
from settings import Settings, get_settings
from unittest import mock
import pytest


client = TestClient(app)

@pytest.fixture
def mock_env_var_ini() -> None:
    with mock.patch.dict(os.environ, {"INVENTORY_SOURCE": "INI", "INVENTORY_FILE_SOURCE": "tests/test_files/inventory"}):
        yield

def test_get_devices_ini(mock_env_var_ini):
    response = client.get("/device")
    assert response.status_code == 200
    assert len(response.json()) > 1 
    assert response.json()[0]['name'] == "FW_INT1_INI"

def test_get_device_ini(mock_env_var_ini):
    response = client.get("/device/2")
    assert response.status_code == 200
    assert response.json()['name'] == "BranchCSR1000v_INI"

# def test_create_device_ini():
#     app.dependency_overrides[get_settings] = get_settings_override_ini
#     response = client.post("/device",
#     json={
#         "id": 4,
#         "name": "FW_INT3_json",
#         "manufacturer_id": 1,
#         "model": "VM100",
#         "state": "unknown",
#         "mgmt_interface_id":7
#         },
#     )
#     assert response.status_code == 307
#     assert response == 0
#     app.dependency_overrides = {}