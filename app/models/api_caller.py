"""Handle the interactions with the web services used by the program."""

import os
import requests


class APIgmap:
    """Handle the interactions with Google Maps services.
    It creates an object containing the methods to interact with its API.
    """

    def __init__(self):
        self.key_back = os.environ.get('GOOGLE_API_KEY_BACK')
        self.base_url = "https://maps.googleapis.com/maps/api/geocode/json?"


    def get_location(self, question):
        """Try to get geospatial informations on a location,
        from a text describing the location.

        If successfull, the function returns a dictioanry containing:
         - the address of the location,
         - its latitude,
         - its longitude
        Otherwise, it returns an object of NoneType.
        """

        location = None

        # Try to format the attribute of the function
        try:
            cleaned_input = question.strip()
            formated_input = cleaned_input.replace(" ", "+")

        except AttributeError:
            pass

        # Build the request to the API
        else:
            params_url = {
                "address": formated_input,
                "types": "geocode",
                "key": self.key_back
                }
            response = requests.get(url=self.base_url, params=params_url)

            # Try to call the API
            try:
                results = response.json()['results'][0]
                location = {
                    'address': results['formatted_address'],
                    'latitude': results['geometry']['location']['lat'],
                    'longitude': results['geometry']['location']['lng']
                    }

            except IndexError:
                pass
        
        # Return the location, 
        # which will be empty if one the specified execeptions has been raised
        finally:
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

        # Build the request to the API
        params_url = {
            "format": "json",
            "list": "geosearch",
            "gscoord": f"{location['latitude']}|{location['longitude']}",
            "gslimit": "10",
            "gsradius": "10000",
            "action": "query"
            }
        response = requests.get(url=self.base_url, params=params_url)

        # Call the API
        results = response.json()['query']['geosearch'][0]

        # Get the page number from the response
        return results['pageid']


    def get_page_text(self, page_id):
        """Try to retrieve the first sentences in a web page on Wikipedia,
        from the page id of this web page.
        """

        # Build the request to the API
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
        response = requests.get(url=self.base_url, params=params_url)

        # Call the API
        results = response.json()['query']['pages'][f'{page_id}']

        # Get the text of the page from the response
        extract = results['extract']

        # Fetch the first paragraph from the text of the page
        return extract.splitlines()[0]
