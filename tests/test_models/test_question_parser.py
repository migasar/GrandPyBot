import pytest 


from grandpy.models import question_parser


class TestFlattenText:

    def test_flatten_text_function_lower_cases_of_input(self):
        """
        GIVEN a string of words as attribute 
            (which we received from the user input)
        WHEN we apply the method lower() to the string
        THEN it should return a string 
            with the same characters but without uppercase.
        """

        script = question_parser.QuestionParser
        assert script.flatten_text("Foo Bar") == "foo bar"



    def test_flatten_text_function_strip_accents_of_input(self):
        """
        GIVEN a string of words as attribute 
        WHEN we apply a method to the string to remove accents
        THEN it should return a string 
            with the same characters but without accents.
        """

        script = question_parser.QuestionParser
        assert script.flatten_text("açôcàr") == "acocar"


    def test_flatten_text_function_used_on_stopwords_from_constant(self):
        """
        GIVEN a list of words retrieved from the constants
        WHEN we apply the function 'flatten_text' to the list of words
        THEN it return a modified version of this list 
            by striping any accent on the characters 
            and formating them in lowercase.
        """

        script = question_parser.QuestionParser
        assert script.flatten_text(['Foô', 'Bàr']) == ['foo', 'bar']


class TestSegmentText:

    def test_segment_text_function_regex1_catch_expected_occurence(self):
        """
        GIVEN a specified regular expression and a string of words 
        WHEN we use the regular expression to search in the string of words
        THEN it returns the expected occurence 
            which is extracted from the string of words.
        """

        pass


    def test_segment_text_function_regex1_let_pass_irrelevant_occurence(self):
        """
        GIVEN a specified regular expression and a string of words 
        WHEN we use the regular expression to search in the string of words
        THEN it doesn't return a match 
            if the expected occurence is not in the string of words.
        """

        pass

    def test_segment_text_function_regex2_catch_expected_occurence(self):
        """
        GIVEN a specified regular expression and a string of words 
        WHEN we use the regular expression to search in the string of words
        THEN it returns the expected occurence 
            which is extracted from the string of words.
        """

        pass


    def test_segment_text_function_regex2_let_pass_irrelevant_occurence(self):
        """
        GIVEN a specified regular expression and a string of words 
        WHEN we use the regular expression to search in the string of words
        THEN it doesn't return a match 
            if the expected occurence is not in the string of words.
        """

        pass

    def test_segment_text_function_regex3_catch_expected_occurence(self):
        """
        GIVEN a specified regular expression and a string of words 
        WHEN we use the regular expression to search in the string of words
        THEN it returns the expected occurence 
            which is extracted from the string of words.
        """

        pass


    def test_segment_text_function_regex3_let_pass_irrelevant_occurence(self):
        """
        GIVEN a specified regular expression and a string of words 
        WHEN we use the regular expression to search in the string of words
        THEN it doesn't return a match 
            if the expected occurence is not in the string of words.
        """

        pass


    def test_segment_text_function_return_initial_argument_without_modification(self):
        """
        GIVEN none of the regular expressions in the list 'regex' found a match
        WHEN we search them in a string of words
        THEN the string of words is returned unchanged.
        """
        pass


    def test_segment_text_function_regex_list_respect_order_when_fetching_occurence(self):
        """
        GIVEN each of the regular expressions in the list 'regex' is used 
            to search a match in a string of words
        WHEN more than one of the regular expressions has an occurence 
            in the list of words
        THEN the function returns only the first match 
            from the first regular expression who found an occurence.
        """

        pass


class TestRemovePunctuation:

    def test_remove_punctuation_function_find_every_punctuation_in_text(self):
        """
        GIVEN a string of words containing some punctuations
        WHEN the function search for punctuations in the string 
        THEN it find them.
        """

        pass


    def test_remove_punctuation_function_strip_punctuations_in_text(self):
        """
        GIVEN a string of words containing some punctuations
        WHEN the function is applied to the string 
        THEN it removes punctuations.
        """

        pass


    def test_remove_punctuation_function_return_formated_result_if_suited(self):
        """
        GIVEN a string of words containing some punctuations
        WHEN the function is applied to the string 
        THEN it returns a modified version of the string without punctuations.
        """

        pass


    def test_remove_punctuation_function_return_unchanged_input_if_suited(self):
        """
        GIVEN a string of words containing no punctuations
        WHEN the function is applied to the string 
        THEN it returns the initial string of words with no modification.
        """

        pass


class TestFilterText:

    def test_filter_text_function_replace_stopword_with_whitespace(self):
        """
        GIVEN a list of stopwords 
            and a string of words containing some of those stopwords
        WHEN the function is applied on the string of words 
            to search occurences of one of the stopwords
        THEN it returns the string of words modified 
            by replacing any occurence of a stopword with a whitespace.
        """

        pass


    def test_filter_text_function_maintain_text_without_stopword(self):
        """
        GIVEN a list of stopwords 
            and a string of words containing none of the stopwords
        WHEN the function is applied on the string of words 
            to search occurences of one of the stopwords
        THEN it returns the string of words unchanged.
        """

        pass
