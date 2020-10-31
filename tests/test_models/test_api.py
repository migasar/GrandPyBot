import pytest
import requests

from grandpy.models.api_gmap import APIgmap
from grandpy.models.api_wiki import APIwiki


class MockResponse:
    """ Custom class to be the mock return value of requests.get()
    It will override the requests.Response returned from requests.get
    """

    def __init__(self):
        self.data = {
            'mock_key': 'mock_response',
            'results': [
                {
                    'geometry': {
                        'location': {'lat': 48.85837009999999, 'lng': 2.2944813},
                    }
                }
            ],
            'query': {
                'geosearch': [
                    {
                        'pageid': 1359783,
                        'title': 'Tour Eiffel',
                        'lat': 48.858296,
                        'lon': 2.294479
                    }
                ],
                'pages': {
                    '1359783': {
                        'pageid': 1359783,
                        'title': 'Tour Eiffel',
                        'extract': 'La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.'
                    }
                }
            }
        }

    def json(self):
        # mock json() method always returns a specific testing dictionary
        return self.data


@pytest.fixture
def mock_response(monkeypatch):
    """mock_response is a monkeypatched requests.get 
    It was moved to a fixture to make it usable multiple times
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
        assert result.get_location('tour eiffel') == (48.85837009999999, 2.2944813)


class TestAPIwiki:

    def test_get_page_return_expected_result(self, mock_response):
        """
        GIVEN the method 'resquests.get' has fetched an object in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """

        result = APIwiki()
        assert result.get_page(48.85837009999999, 2.2944813) == 1359783


    def test_get_place_return_expected_result(self, mock_response):
        """
        GIVEN the method 'resquests.get' has fetched an object in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """

        result = APIwiki()
        assert result.get_place(1359783) == (
            """La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, """
            """à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. """
            """Son adresse officielle est 5, avenue Anatole-France."""
        )
