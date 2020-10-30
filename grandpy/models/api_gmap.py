"""Handle the interactions with Google Maps services to use them in our program."""


import requests 

from grandpy.models.question_parser import QuestionParser
from grandpy.static.credential import GOOGLE_API_KEY


class APIgmap:
    """An object containing the methods to interact with the API of Google Maps services."""

    def __init__(self):
        
        self.api_key = GOOGLE_API_KEY
        self.base_url = "https://maps.googleapis.com/maps/api/geocode/json?"


    def get_location(self, question):
        """Try to retrieve the latitude and longitude of a location, 
        from a text describing the location.
        """

        latitude, longitude = None, None

        cleaned_input = question.strip()
        formated_input = cleaned_input.replace(" ", "+")

        params_url = f"input={formated_input}&types=geocode&key={self.api_key}"
        endpoint = self.base_url + params_url

        r = requests.get(endpoint)
        try:
            results: r.json['results'][0]
            latitude = results['geometry']['location']['lat']
            longitude = results['geometry']['location']['lng']
        except:
            pass

        return latitude, longitude
