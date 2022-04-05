import pytest


from flask import Flask


@pytest.fixture(scope="session")
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            yield client
