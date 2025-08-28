import pytest

BASE = ""

@pytest.fixture(scope="session")
def base_url():
    return "https://cf-automation-airline-api.onrender.com"