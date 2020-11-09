"""Handle the parsing of the texts receievd and sent to the front-end."""

import re 
import random
from unidecode import unidecode

from grandpy.static.constant import STOPWORD, WESTWORLD_QUOTES
from grandpy.models.api_caller import APIgmap, APIwiki


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

        # ensure that the attribute in a string
        wording = str(wording)
        # lower case
        wording = wording.lower()
        # strip accents
        wording = unidecode(wording)
        
        return wording


    def segment_text(self, wording):
        """Try to extract the significative words of the question from the text,
        with the use of various rational expressions.
        """

        # list of rational expressions used to search the text
        regex = [
            r"((adresse|chemin|direction|itineraire|trajet)( \b\w+\b))(?P<segment>[\w '-]+)",
            r"(ou (est|sont|(se \b\w+\b)))(?P<segment>[\w '-]+)",
            r"((indiqu|localis|position|trouv|situ)\w*)(?P<segment>[\w '-]+)"
        ]

        # search the text with each rational expression, and stop at the first match
        match = None
        for expression in regex:
            if re.search(expression, wording):
                match = re.search(expression, wording)
                return match.group('segment')

        # return whole text, if the rational expressions gave no result
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
        """Apply all the functions of the parser to the string, in a staged process.
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

        # try to find the coordinates of a location related to the text
        gmap_spot = self.api_gmap.get_location(query)

        # test if gmap_spot spotted a location, before fetching a text on the location
        if gmap_spot[0]:

            # if the location was spotted, we try to extract a sample text 
            # from a page on Wikipedia related to the location
            wiki_page = self.api_wiki.get_page_id(gmap_spot[0], gmap_spot[1])
            wiki_extract = self.api_wiki.get_page_text(wiki_page)

            # we append in a dictionary all the elements found with the API calls 
            bot_response = self.stack_response(
                spotted=True,
                extract=wiki_extract,
                coordinates=gmap_spot
        )

        else:
            # no location based on the query
            bot_response = self.stack_response()
        
        return bot_response


    def stack_response(self, spotted=False, extract=None, coordinates=None):
        """Pile all the informations retrieved from the queries in a single object."""

        response_elements = {
            'context': None,
            'reply': random.choice(self.botquotes['reply']),
            'extract': extract,
            'latitude': None,
            'longitude': None,
            'spotted': spotted
        }

        # if none of the attributes is false or empty
        if spotted and extract and coordinates[0]:
            response_elements['context'] = random.choice(self.botquotes['success'])
            response_elements['latitude'] = coordinates[0]
            response_elements['longitude'] = coordinates[1]

        else:
            response_elements['context'] = random.choice(self.botquotes['failure'])

        return response_elements
