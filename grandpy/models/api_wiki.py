"""Handle the interactions with Wikipedia tools to use them in our program."""


import requests

from grandpy.models.api_gmap import APIgmap


class APIwiki:
    """An object containing the methods to interact with the API of Wikipedia."""

    def __init__(self):
        
        self.base_url = "https://fr.wikipedia.org/w/api.php"

    
    def get_page(self, latitude, longitude):
        """Try to retrieve the page id of an entry on Wikipedia dedicated on a location,
        from its coordinates (latitude and longitude).
        """

        page_id = None

        params_url = {
            "format": "json",
            "list": "geosearch",
            "gscoord": f"{latitude}|{longitude}",
            "gslimit": "10",
            "gsradius": "10000",
            "action": "query"
            }

        response = requests.get(url=self.base_url, params=params_url)

        try:
            results = response.json()['query']['geosearch'][0]
            page_id = results['pageid']
        except:
            pass

        return page_id
    

    def get_place(self, page_id):
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
            "exsentences": "2",
            "explaintext": 1,
            "inprop": "displaytitle|url|subjectid"
            }

        response = requests.get(url=self.base_url, params=params_url)
        try:
            results = response.json()['query']['pages'][f'{page_id}']
            page_extract = results['extract']
        except:
            pass

        return page_extract
