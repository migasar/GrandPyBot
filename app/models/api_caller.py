"""Handle the interactions with the web services used by the program."""

import requests

# from app.static.credentials import GOOGLE_API_KEY
from app.static.constant import GOOGLE_API_KEY


class APIgmap:
    """Handle the interactions with Google Maps services.
    It creates an object containing the methods to interact with its API.
    """

    def __init__(self):
        self.api_key = GOOGLE_API_KEY
        self.base_url = "https://maps.googleapis.com/maps/api/geocode/json?"


    def get_location(self, question):
        """Try to get geospatial informations on a location,
        from a text describing the location.

        If successfull, the function returns a dictioanry containing:
         - the address of the location,
         - its latitude,
         - its longitude

        If the function doesn't find a location,
        it returns an object of NoneType.
        """

        location = None

        try:
            # Try to format the attribute of the function
            cleaned_input = question.strip()
            formated_input = cleaned_input.replace(" ", "+")

        except AttributeError:
            pass

        else:
            # Build the request to the API
            params_url = f"address={formated_input}&types=geocode&key={self.api_key}"
            endpoint = self.base_url + params_url

            # Call the API
            response = requests.get(endpoint)
            try:
                results = response.json()['results'][0]

                location = {
                    'address': results['formatted_address'],
                    'latitude': results['geometry']['location']['lat'],
                    'longitude': results['geometry']['location']['lng']
                }

            except:
                pass

        return location


class APIwiki:
    """Handle the interactions with Wikipedia tools to use them in our program.
    It creates an object containing the methods to interact with its API.
    """

    def __init__(self):
        self.base_url = "https://fr.wikipedia.org/w/api.php"


    def get_page_id(self, location):
        """Try to retrieve the page id of an entry on Wikipedia dedicated on a location,
        from its coordinates (latitude and longitude of location).
        """

        page_id = None
        params_url = {
            "format": "json",
            "list": "geosearch",
            "gscoord": f"{location['latitude']}|{location['longitude']}",
            "gslimit": "10",
            "gsradius": "10000",
            "action": "query"
        }

        # Build the request to the API
        response = requests.get(url=self.base_url, params=params_url)
        try:
            # Try to call the API
            results = response.json()['query']['geosearch'][0]
            page_id = results['pageid']
        except:
            pass

        return page_id


    def get_page_text(self, page_id):
        """Try to retrieve the first sentences in a web page on Wikipedia,
        from the page id of this web page.
        """

        page_extract = None
        params_url = {
            "action": "query",
            "format": "json",
            "prop": "extracts|info",
            "pageids": f"{page_id}",
            "utf8": 1,
            "exsentences": "3",
            "explaintext": 1,
            "inprop": "displaytitle|url|subjectid"
        }

        # Build the request to the API
        response = requests.get(url=self.base_url, params=params_url)
        try:
            # Try to call the API
            results = response.json()['query']['pages'][f'{page_id}']
            text_extract = results['extract']

            # Fetch the first paragraph from the text on the body of the page
            page_extract = text_extract.splitlines()[0]
        except:
            pass

        return page_extract
