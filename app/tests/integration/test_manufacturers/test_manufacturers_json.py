import os

from model.manufacturer import Manufacturer

from unittest import mock
from fastapi.testclient import TestClient
from main import app
from settings import Settings, get_settings
from unittest import mock
import pytest


client = TestClient(app)

@pytest.fixture
def mock_env_manufacturers_json() -> None:
    with mock.patch.dict(os.environ, {"MANUFACTURERS_SOURCE": "JSON", "MANUFACTURERS_FILE_SOURCE": "tests/test_files/manufacturers"}):
        yield

def test_get_manufacturers_json(mock_env_manufacturers_json):
    response = client.get("/manufacturer")
    assert response.status_code == 200
    assert len(response.json()) > 1 
    assert response.json()[0]['name'] == "paloalto_json"

def test_get_manufacturer_json(mock_env_manufacturers_json):
    response = client.get("/manufacturer/2")
    assert response.status_code == 200
    assert response.json()['name'] == "cisco_json"

def test_create_manufacturer_json_successful(mock_env_manufacturers_json):
    manufacturers_raw = client.get("/manufacturer")
    manufacturers =  [ Manufacturer(**p) for p in manufacturers_raw.json() ]
    last_number = (manufacturers[-1]).id
    response = client.post("/manufacturer",
    json={
        "id": last_number+1 ,
        "name": "test_manufacturer_"+str(last_number+1),
        "full_name": "ACME TEST MANUFACTURER"
        },
    )
    assert response.status_code == 200
    assert response.json()['name'] == "test_manufacturer_"+str(last_number+1)