from flask import render_template, jsonify, request

from grandpy import app
from grandpy.models import query_parser


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    """Route to the async methods of the program (AJAX)."""
    
    # Retrieve the user question from the front-end
    user_text = request.form["userText"]

    # Parse the user query to extract keywords
    question_parser = query_parser.QuestionParser()
    user_query = question_parser.parsing_flow(user_text)

    # Try to spot a location from the text of the user query
    answer_builder = query_parser.AnswerBuilder()
    response = answer_builder.spot_response(user_query)

    return jsonify(response)
