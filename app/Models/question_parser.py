"""Handle the parsing of the text written by the user.  
Extract the significative words that could relate to a location.
"""

import re 
from unidecode import unidecode

from App.Static.constant import STOPWORD


class TextParser:
    
    def __init__(self):
        self.text = None
        self.segment = None 
        self.stopwords = [self.flatten_text(word) for word in STOPWORD]
        
    
    def flatten_text(self, wording):

        #  lower case
        wording = wording.lower()

        # strip accents
        wording = unidecode(wording)

        return wording
    

    def segment_text(self, wording):
        """Try to extract the significative words of the question from the text,
        with the use of various rational expressions"""

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
        if match is False:
            return wording
    

    def remove_punctuation(self, wording):
        # remove every punctuation from the text

        if re.search(r"[^' a-zA-Z0-9-]", wording):
            return re.sub(r"[^' a-zA-Z0-9-]", "", wording)
        
        else:
            return wording


    def filter_text(self, wording):
        # remove stopwords from the text
        
        for word in self.stopwords:
            wording = wording.replace(f' {word} ', ' ')

        return wording
