import pytest
import requests


@pytest.fixture(scope='session')
def s():
    """create Session"""
    return requests.session()
