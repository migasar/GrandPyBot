"""Handle the parsing of the texts receievd and sent to the front-end."""

import re
import random
from unidecode import unidecode

from app.static.constant import STOPWORD, WESTWORLD_QUOTES
from app.models.api_caller import APIgmap, APIwiki


class QuestionParser:
    """Handle the parsing of the text written by the user.
    Extract the significative words that could relate to a location.
    """

    def __init__(self):
        self.stopwords = [self.flatten_text(word) for word in STOPWORD]


    def flatten_text(self, wording):
        """Normalize the characters of a text,
        by ensuring that the whole string is in lowercase,
        and by striping every accent in it.
        """

        # Ensure that the attribute in a string
        wording = str(wording)
        # Lower cases
        wording = wording.lower()
        # Strip accents
        wording = unidecode(wording)

        return wording


    def segment_text(self, wording):
        """Try to extract the significative words of the question from the text,
        with the use of various rational expressions.
        """

        # List of rational expressions used to search the text
        regex = [
            r"((adresse|chemin|direction|itineraire|trajet)( \b\w+\b))(?P<segment>[\w '-]+)",
            r"(ou (est|sont|(se \b\w+\b)))(?P<segment>[\w '-]+)",
            r"((indiqu|localis|position|trouv|situ)\w*)(?P<segment>[\w '-]+)"
            ]

        # Search the text with each rational expression, and stop at the first match
        match = None
        for expression in regex:
            if re.search(expression, wording):
                match = re.search(expression, wording)
                return match.group('segment')

        # Return whole text, if the rational expressions gave no result
        if match is None:
            return wording


    def remove_punctuation(self, wording):
        """Remove every punctuation from the text."""

        try:
            re.search(r"[^' a-zA-Z0-9-]", wording)
        except TypeError:
            pass
        else:
            if re.search(r"[^' a-zA-Z0-9-]", wording):
                wording = re.sub(r"[^' a-zA-Z0-9-]", "", wording)

        return wording


    def filter_text(self, wording):
        """Remove stopwords from the text."""

        try:
            for word in self.stopwords:
                wording = wording.replace(f' {word} ', ' ')
        except AttributeError:
            pass

        return wording


    def parsing_flow(self, text):
        """Apply all the functions of the parser on the string, in a staged process.
          -  put every characters of the string in lowercase, and strip every accent
          -  try to extract the significative words of the string, with regex
          -  remove the punctuation in the string
          -  remove a list of stopwords from the string
        """

        flow_funcs = [
            self.flatten_text,
            self.segment_text,
            self.remove_punctuation,
            self.filter_text
            ]

        # Chain the call to the functions in the list
        for func in flow_funcs:
            text = func(text)

        return text


class AnswerBuilder:
    """Build the bot reply to the user question.
    Retrieve the elements to formulate a response,
    and send back the elements of the response, stacked in a dictionary.
    """

    def __init__(self):
        self.botquotes = WESTWORLD_QUOTES
        self.api_gmap = APIgmap()
        self.api_wiki = APIwiki()


    def spot_response(self, query):
        """Chain the calls to the API of Gmap and Wikipedia,
        to get all the geospatial elements of the bot response.
        """

        # Try to find the coordinates of a location related to the text
        gmap_spot = self.api_gmap.get_location(query)

        # Test if gmap_spot spotted a location, 
        # before fetching a text on the location
        if gmap_spot is None:
            # If there is no location based on the query,
            # then call the function with null parameters
            return self.stack_response()

        # If a location has been spotted, try to extract a sample text
        # from a related page on Wikipedia
        else:
            # Search for the id number of a page related to the location
            wiki_page = self.api_wiki.get_page_id(gmap_spot)
            # Get the first sentences of the text in the body of the page
            wiki_extract = self.api_wiki.get_page_text(wiki_page)

            # Create a dictionary with all the elements found with the API
            return self.stack_response(
                spotted=True, 
                extract=wiki_extract, 
                location=gmap_spot
                )


    def stack_response(self, spotted=False, extract=None, location=None):
        """Pile all the informations retrieved from the queries in a single object."""

        # Create a dictionary with certain elements, if a location was found
        if spotted is True:
            response_elements = {
                'context': random.choice(self.botquotes['success']),
                'reply': random.choice(self.botquotes['reply']),
                'extract': extract,
                'address': location['address'],
                'latitude': location['latitude'],
                'longitude': location['longitude'],
                'spotted': spotted
                }

        # Create a dictionary with other elements, otherwise
        else:
            response_elements = {
                'context': random.choice(self.botquotes['failure']),
                'reply': random.choice(self.botquotes['reply']),
                'extract': extract,
                'address': None,
                'latitude': None,
                'longitude': None,
                'spotted': spotted
                }

        return response_elements
