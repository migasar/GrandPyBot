from app import app

from app.models.question_parser import QuestionParser
from app.static import constant


question_parser = QuestionParser()

user_question = """
Bonsoir Juju,  j'espère que tu as passé une belle semaine. 
Est-ce que tu pourrais m'indiquer où se trouve l'alcove de la tour eiffel? Merci d'avance et salutations à Mamie.
"""
print(f"user question : {user_question}")

flat_text = question_parser.flatten_text(user_question)
print(f"""flat text: 
{flat_text}
""")

text_segment = question_parser.segment_text(flat_text)
print(f"""text segment:  {text_segment} """)

no_punctuation_text = question_parser.remove_punctuation(text_segment)
print(f"""punctuation removed: 
{no_punctuation_text}
""")

filtered_text = question_parser.filter_text(no_punctuation_text)
print(f"""filtered text: 
{filtered_text}
""")
