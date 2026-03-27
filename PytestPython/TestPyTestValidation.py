#fixture
import pytest
@pytest.fixture(scope="function")
def preWork():
    print("I Setup browser instance")


def test_initialCheck(preWork):
    print("This is First Test")

def test_secondCheck(preWork):
    print("This is Second Test")