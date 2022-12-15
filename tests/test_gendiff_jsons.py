import pytest
from gendiff.modules.gendiff import generate_diff
from gendiff.utils.file_utils import load_jsons


@pytest.fixture
def json_expected(dir_):
    path = f'tests/fixtures/jsons/{dir_}/expected_diff'
    with open(file=path, mode='r') as file:
        expected = file.readlines()
        expected = str.join('', expected)
        return expected


@pytest.fixture
def json_files(dir_):
    path1 = f'tests/fixtures/jsons/{dir_}/file1.json'
    path2 = f'tests/fixtures/jsons/{dir_}/file2.json'
    return load_jsons(path1, path2)


@pytest.mark.parametrize(argvalues=['simple_jsons', 'deep_jsons'], argnames='dir_')
def test_gendiff(json_files, json_expected):
    assert generate_diff(*json_files, format_='stylish') == json_expected
