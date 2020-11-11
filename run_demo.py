from grandpy import app

from grandpy.static import constant
from grandpy.models import api_caller, query_parser

# from grandpy.models.query_parser import QuestionParser
# from grandpy.models.api_caller import APIgmap, APIwiki


# ###### Question Parser ###### #

question_parser = query_parser.QuestionParser()

user_question_ = "@"

user_question = """
Bonsoir Juju,  j'espère que tu as passé une belle semaine. 
Est-ce que tu pourrais m'indiquer où se trouve la tour eiffel? Merci d'avance et salutations à Mamie.
"""
print(f"user question : {user_question}")

flat_text = question_parser.flatten_text(user_question)
print(f"flat text: {flat_text}")

text_segment = question_parser.segment_text(flat_text)
print(f"text segment:  {text_segment}")

no_punctuation_text = question_parser.remove_punctuation(text_segment)
print(f"punctuation removed: {no_punctuation_text}")

filtered_text = question_parser.filter_text(no_punctuation_text)
print(f"filtered text:  {filtered_text}")

print()


# ###### API Gmap ###### #

api_gmap = api_caller.APIgmap()

coordinates = api_gmap.get_location(filtered_text)
print(f"coordinates:  {coordinates}")
print(f"latitude:  {coordinates['latitude']}")

def none_coordinates(coordinate):
    if coordinate is None:
        print("coordinates null")
    elif type(coordinate['latitude']) and type(coordinate['longitude']) is float:
        print("floating coordinates")
    else:
        print("coordinates is not None type")

none_coordinates(coordinates)


# ###### API Wiki ###### #

api_wiki = api_caller.APIwiki()

page_id = api_wiki.get_page_id(coordinates)
print(f"page number:  {page_id}")

page_extract = api_wiki.get_page_text(page_id)
print("page extract:")
print(page_extract)
print()
print("TEST Page Extract: ")
print(
    """La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, """
    """à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. """
    """Son adresse officielle est 5, avenue Anatole-France."""
)
print()
    

user_text = """
Bonsoir Juju,  j'espère que tu as passé une belle semaine. 
Est-ce que tu pourrais m'indiquer où se trouve le musée du louvres? Merci d'avance et salutations à Mamie.
"""
user_text_ = "tour eiffel"

print(f"user text : {user_text}")

question_parser = query_parser.QuestionParser()
answer_piler = query_parser.AnswerBuilder()
api_gmap = api_caller.APIgmap()
api_wiki = api_caller.APIwiki()

# parse the user query to extract keywords
user_query = question_parser.flatten_text(user_text)
user_query = question_parser.segment_text(user_query)
user_query = question_parser.remove_punctuation(user_query)
user_query = question_parser.filter_text(user_query)
