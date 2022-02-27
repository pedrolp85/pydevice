import os

from fastapi.testclient import TestClient
from main import app
from model.device import Device
from model.interface import L3Interface
from settings import Settings, get_settings
from unittest import mock
import pytest


client = TestClient(app)

@pytest.fixture
def mock_interface_var_ini() -> None:
    with mock.patch.dict(os.environ, {"INTERFACES_SOURCE": "INI", "INTERFACES_FILE_SOURCE": "tests/test_files/interfaces"}):
        yield

def test_get_interfaces_ini(mock_interface_var_ini):
    response = client.get("/interface")
    assert response.status_code == 200
    assert len(response.json()) > 1
    assert response.json()[0]['name'] == "mgmt0_ini"


def test_get_interface_json(mock_interface_var_ini):
    response = client.get("/interface/2")
    assert response.status_code == 200
    assert response.json()['name'] == "eth1/1_ini"


def test_create_interface_json_successful(mock_interface_var_ini):
    interfaces_raw = client.get("/interface")
    interfaces =  [ L3Interface(**p) for p in interfaces_raw.json() ]
    last_number = (interfaces[-1]).id
    response = client.post("/interface",
    json={
        "id": last_number+1 ,
        "name": "fastTest0"+str(last_number+1),
        "ip_address": "172.16.100.101",
        "device_id": 1 ,
        "ttl": 3 
        },
    )
    assert response.status_code == 200
    assert response.json()['name'] == "fastTest0"+str(last_number+1)
