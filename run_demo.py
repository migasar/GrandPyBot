from grandpy import app

from grandpy.static import constant
# from grandpy.models.query_parser import QuestionParser
# from grandpy.models.api_caller import APIgmap, APIwiki
from grandpy.models import api_caller, query_parser



# ###### Question Parser ###### #


# comments

    # question_parser = QuestionParser()

    # user_question_ = "@"

    # user_question = """
    # Bonsoir Juju,  j'espère que tu as passé une belle semaine. 
    # Est-ce que tu pourrais m'indiquer où se trouve la tour eiffel? Merci d'avance et salutations à Mamie.
    # """
    # print(f"user question : {user_question}")

    # flat_text = question_parser.flatten_text(user_question)
    # print(f"flat text: {flat_text}")

    # text_segment = question_parser.segment_text(flat_text)
    # print(f"text segment:  {text_segment}")

    # no_punctuation_text = question_parser.remove_punctuation(text_segment)
    # print(f"punctuation removed: {no_punctuation_text}")

    # filtered_text = question_parser.filter_text(no_punctuation_text)
    # print(f"filtered text:  {filtered_text}")

    # print()


    # # ###### API Gmap ###### #

    # api_gmap = APIgmap()

    # coordinates = api_gmap.get_location(filtered_text)
    # print(f"coordinates:  {coordinates}")
    # print(f"latitude:  {coordinates[0]}")

    # def none_coordinates(coordinate):
    #     if not coordinate[0] or coordinate[1]:
    #         print("coordinates null")
    #     elif type(coordinate[0]) and type(coordinate[1]) is float:
    #         print("floating coordinates")
    #     else:
    #         print("coordinates is not None type")

    # none_coordinates(coordinates)


    # # ###### API Wiki ###### #

    # api_wiki = APIwiki()

    # page_id = api_wiki.get_page_id(coordinates[0], coordinates[1])
    # print(f"page number:  {page_id}")

    # page_extract = api_wiki.get_page_text(page_id)
    # print(f"""
    # page extract: 
    # {page_extract}""")


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

# try to find coordinates of a location related to the keywords
gmap_spot = api_gmap.get_location(user_query)

# test if gmap_spot spotted a location, before fetching a text on the location
if gmap_spot[0]:
    # location spotted
    wiki_page = api_wiki.get_page_id(gmap_spot[0], gmap_spot[1])
    wiki_extract = api_wiki.get_page_text(wiki_page)
    bot_reply = answer_piler.stack_response(
        spotted=True,
        extract=wiki_extract,
        coordinates=gmap_spot
    )

else:
    # no location based on the query
    bot_reply = answer_piler.stack_response()

# return jsonify(bot_reply)
print(f"bot reply: {bot_reply}")
