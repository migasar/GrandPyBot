import requests
from grandpy.models.question_parser import QuestionParser
from grandpy.static.credential import GOOGLE_API_KEY

from grandpy.models import api_gmap


class TestGetLocation:

    def test_get_location_format_input_properly(self):
        """
        GIVEN a string of words separated by whitespaces as attribute
        WHEN cleaned_input and formated_input are applied to the attribute
        THEN it should return a string with the same words 
            but separated by the sign + instead of whitespaces.
        """

        pass


    def test_get_location_create_endpoint_as_expected(self):
        """
        GIVEN a formated string of characters as input, 
            an 'api_key' stored as a private constant, 
            a f-string 'params_url' receiving those variables, 
            and a string 'base_url' 
        WHEN we concatenate those elements 
        THEN it should return a string endpoint usable with requests.
        """

        pass


    def test_get_location_connection_with_requests_is_ok(self):
        """
        GIVEN a string 'endpoint' built with the url and the parameters of the API 
        WHEN we use 'endpoint' as an attribute with methods of the library requests 
        THEN it should return the proper status code.
        """

        pass


    def test_get_location_method_get_requests_fetch_result_in_json(self):
        """
        GIVEN a string 'endpoint' built with the url and the parameters of the API 
        WHEN we use 'endpoint' as an attribute with the method 'get' of the library requests 
        THEN it should retrieve a result (as a JSON) from the API.
        """

        pass


    def test_get_location_return_expected_result(self):
        """
        GIVEN the method 'resquests.get' has fetched a result in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """

        pass


    def test_get_location_exception_return_result_with_null_value(self):
        """
        GIVEN the method 'resquests.get' has fetched a result in JSON
        WHEN we search in the components of the JSON, 
            but we don't find the components we want
        THEN the function silently raises an exception, 
            and return those components but with null values.
        """

        pass
