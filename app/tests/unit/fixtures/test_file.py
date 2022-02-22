from repository.devices.DevicesRepositoryJSONFile import DevicesRepositoryJSONFile


# class TestFileInput:
#     def test_get_lines(self, mock_file, file_lines) -> None:
#         file_input = FileInput("some_path.txt")
#         result = list(file_input.get_lines())
#         assert result == file_lines

class TestDevices:
    def test_get_device(self, mock_file, file_device_json_content) -> None:
        devices_json = DevicesRepositoryJSONFile()
        result = devices_json.get_device(1)
        assert result == file_lines


# class TestReversFileInput:
#     def test_get_lines(self, mock_file, reverse_file_lines) -> None:
#         file_input = ReverseFileInput("some_path.txt")
#         result = list(file_input.get_lines())
#         assert result == reverse_file_lines