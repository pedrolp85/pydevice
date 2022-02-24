import os

from fastapi.testclient import TestClient
from main import app
from settings import Settings, get_settings
from unittest import mock
import pytest


client = TestClient(app)


def get_settings_override_manufacturers_ini():
    return Settings(manufacturers_source="INI", manufacturers_file_source="tests/test_files/manufacturers")

def test_get_manufacturers_ini():
    app.dependency_overrides[get_settings] = get_settings_override_manufacturers_ini
    response = client.get("/manufacturer")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]['name'] == "paloalto_ini"
    app.dependency_overrides = {}

def test_get_manufacturer_ini():
    app.dependency_overrides[get_settings] = get_settings_override_manufacturers_ini
    response = client.get("/manufacturer/2")
    assert response.status_code == 200
    assert response.json()['name'] == "cisco_ini"
    app.dependency_overrides = {}