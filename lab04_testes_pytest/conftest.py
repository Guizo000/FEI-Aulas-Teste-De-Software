import pytest

@pytest.fixture
def valores():
    return {
        "valor_menor": 50,
        "valor_maior": 100
    }