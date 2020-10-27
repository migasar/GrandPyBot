from flask import Flask 


app = Flask(__name__)


from grandpy import route
from grandpy.models import api_gmap, api_wiki, question_parser
