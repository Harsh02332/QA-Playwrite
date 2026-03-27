#fixture
import pytest
@pytest.fixture(scope="module")
def preWork():
    print("I Setup Module instance")


def test_initialCheck(preWork):
    print("This is First Test")

def test_secondCheck(preSetupWork):
    print("This is Second Test")