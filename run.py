from App import app

from App.Models import question_parser
from App.Static import constant


user_question = """
Bonsoir Juju,  j'espère que tu as passé une belle semaine. 
Est-ce que tu pourrais m'indiquer où se trouve l'alcove de la tour eiffel? Merci d'avance et salutations à Mamie.
"""

print(f"user question : {user_question}")

text_parser = question_parser.TextParser(text=user_question)


flat_text = text_parser.flatten_text(text_parser.text)
print(f"""flat text: 
{flat_text}
""")



text_segment = text_parser.segment_text(flat_text)
print(f"""text segment:  {text_segment} """)

'''
text_segment = flat_text
'''

no_punctuation_text = text_parser.remove_punctuation(text_segment)
print(f"""punctuation removed: 
{no_punctuation_text}
""")


filtered_text = text_parser.filter_text(no_punctuation_text)
print(f"""filtered text: 
{filtered_text}
""")
