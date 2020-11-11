import pytest
import requests

from app.models.api_caller import APIgmap, APIwiki


class MockResponse:
    """ Custom class to be the mock return value of requests.get()
    It will override the requests.Response returned from requests.get
    """

    def __init__(self):
        self.data = {

            # example of Mock syntax
            'mock_key': 'mock_response',

            # results: mock of call to Gmap API
            'results': [{
                'formatted_address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
                'geometry': {'location': {
                    'lat': 48.85837009999999, 
                    'lng': 2.2944813
                }}
            }],

            # query: mock of call to Wiki API
            'query': {
                'geosearch': [{
                    'pageid': 1359783, 
                    'title': 'Tour Eiffel', 
                    'lat': 48.858296, 
                    'lon': 2.294479
                }],
                'pages': {'1359783': {
                    'pageid': 1359783, 
                    'title': 'Tour Eiffel', 
                    'extract': 'La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.'
                }}
            }
        }


    def json(self):
        # mock json() method always returns a specific testing dictionary
        return self.data


@pytest.fixture
def mock_response(monkeypatch):
    """mock_response is a monkeypatched requests.get 
    It has been moved to a fixture to make it usable with multiple test functions
    """

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


class TestAPIgmap:

    def test_get_location_return_expected_result(self, mock_response):
        """
        GIVEN the method 'resquests.get' has fetched an object in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """

        result = APIgmap()
        expected_result = {
            'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
            'latitude': 48.85837009999999,
            'longitude': 2.2944813
        }

        assert result.get_location('tour eiffel') == expected_result


class TestAPIwiki:

    def test_get_page_id_return_expected_result(self, mock_response):
        """
        GIVEN the method 'resquests.get' has fetched an object in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """

        result = APIwiki()
        pseudo_location = {
            'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
            'latitude': 48.85837009999999,
            'longitude': 2.2944813
        }
        
        assert result.get_page_id(pseudo_location) == 1359783


    def test_get_page_text_return_expected_result(self, mock_response):
        """
        GIVEN the method 'resquests.get' has fetched an object in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """

        result = APIwiki()
        expected_result = (
            """La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, """
            """à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. """
            """Son adresse officielle est 5, avenue Anatole-France."""
        )

        assert result.get_page_text(1359783) == expected_result
