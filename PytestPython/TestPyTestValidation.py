#fixture
import pytest
@pytest.fixture
def preWork():
    print("I Setup browser instance")


def test_initialCheck(preWork):
    print("This is First Test")
