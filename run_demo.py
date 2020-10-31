from grandpy import app

from grandpy.static import constant
from grandpy.models.question_parser import QuestionParser
from grandpy.models.api_gmap import APIgmap
from grandpy.models.api_wiki import APIwiki


# ###### Question Parser ###### #

question_parser = QuestionParser()

user_question = """
Bonsoir Juju,  j'espère que tu as passé une belle semaine. 
Est-ce que tu pourrais m'indiquer où se trouve la tour eiffel? Merci d'avance et salutations à Mamie.
"""
print(f"user question : {user_question}")

flat_text = question_parser.flatten_text(user_question)
print(f"""flat text: 
{flat_text}""")

text_segment = question_parser.segment_text(flat_text)
print(f"text segment:  {text_segment}")

no_punctuation_text = question_parser.remove_punctuation(text_segment)
print(f"punctuation removed: {no_punctuation_text}")

filtered_text = question_parser.filter_text(no_punctuation_text)
print(f"filtered text:  {filtered_text}")

print()


# ###### API Gmap ###### #

api_gmap = APIgmap()

coordinates = api_gmap.get_location(filtered_text)
print(f"coordinates:  {coordinates}")
print(f"latitude:  {coordinates[0]}")


# ###### API Wiki ###### #

api_wiki = APIwiki()

page_id = api_wiki.get_page(coordinates[0], coordinates[1])
print(f"page number:  {page_id}")

page_extract = api_wiki.get_place(page_id)
print(f"""
page extract: 
{page_extract}""")
