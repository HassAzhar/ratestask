from http import HTTPStatus


def test_wrong_date_format(client):
    response = client.get('/rates?date_from=01-01-2016&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"')
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_missing_params(client):
    response = client.get('/rates?date_from=01-01-2016&origin=CNSGH&destination=north_europe_main"')
    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_db_tolerance(client):
    response = client.get('/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH\'&destination=north_europe_main')
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response = client.get('/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main')
    assert response.status_code == HTTPStatus.OK

def test_correct_response_size(client):
    response = client.get('/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main')
    assert response.status_code == HTTPStatus.OK
    assert len(response.json) == 9