from app import app


def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_about_page():
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200


def test_services_page():
    client = app.test_client()
    response = client.get('/services')
    assert response.status_code == 200


def test_homepage_has_arabic_content():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'\xd9\x85\xd9\x8a\xd8\xa7\xd8\x8c\xd9\x8b\xd8\xb1\xd9\x8b' in response.data
