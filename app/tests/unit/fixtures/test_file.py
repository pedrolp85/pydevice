from app.repository.devices.devicesJSONfile import DevicesRepositoryJSONFile


class TestDevices:
    def test_get_device(self, mock_file, file_device_json_content) -> None:
        devices_json = DevicesRepositoryJSONFile()
        result = devices_json.get_device(1)
        assert 0


