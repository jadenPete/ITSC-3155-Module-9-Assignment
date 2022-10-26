from app import app
import pytest

@pytest.fixture(scope='module')
def test_app():
    return app.test_client()
