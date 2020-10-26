from flask import Flask 


app = Flask(__name__)


from app import route
from app.models import api_gmap, api_wiki, question_parser
