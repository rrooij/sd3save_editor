import os
import pytest

from sd3save_editor import save


@pytest.fixture
def test_save_path():
    return f'{os.path.dirname(os.path.realpath(__file__))}/SEIKEN3.srm'


@pytest.fixture
def save_data():
    sd3_save_path = f'{os.path.dirname(os.path.realpath(__file__))}/SEIKEN3.srm'
    return save.read_save(sd3_save_path)


def test_check_valid_save_true(save_data):
    assert save.check_valid_save(save_data)
