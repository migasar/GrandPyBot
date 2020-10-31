from grandpy.models.question_parser import QuestionParser


def test_flatten_text_function_lower_cases_and_strip_accents_of_input():
    """
    GIVEN a string of words as attribute (which we received from the user input)
    WHEN we apply the method lower() to the string
    THEN it should return a string with the same characters but without uppercase.
    """

    result = QuestionParser()
    text = "Foô Bàr"

    assert result.flatten_text(text) == "foo bar"


def test_segment_text_function_catch_expected_occurence():
    """
    GIVEN a specified regular expression and a string of words 
    WHEN we use the regular expression to search in the string of words
    THEN it returns the expected occurence 
        which is extracted from the string of words.
    """

    result = QuestionParser()
    text = """
            Bonsoir Arnold, es-tu sorti de ton long sommeil sans reves? 
            Saurais-tu ou se trouve la sortie du labyrinthe? 
            """

    assert result.segment_text(text) == " la sortie du labyrinthe"


def test_remove_punctuation_function_strip_punctuations_in_text():
    """
    GIVEN a string of words containing some punctuations
    WHEN the function is applied to the string 
    THEN it returns a modified version of the string without punctuations.
    """

    result = QuestionParser()
    text = "Hello, world!"
    
    assert result.remove_punctuation(text) == "Hello world"


def test_filter_text_function_replace_stopword_with_whitespace():
    """
    GIVEN a list of stopwords and a string of words 
        containing some of those stopwords
    WHEN the function is applied on the string of words 
        to search occurences of one of the stopwords
    THEN it returns the string of words modified 
        by replacing any occurence of a stopword with a whitespace.
    """

    result = QuestionParser()
    text = "ces jeux violents auront une fin violente"

    assert result.filter_text(text) == "ces jeux violents fin violente"
