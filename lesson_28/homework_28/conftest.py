import pytest
from homework_28 import get_url

base_url = "https://www.lastingdynamics.com/"


@pytest.fixture
def base_driver():
    return get_url(base_url)
