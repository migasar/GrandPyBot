import requests
from grandpy.models.api_gmap import APIgmap

from grandpy.models import api_wiki 


class TestGetPlace:

    def test_get_place_format_input_properly(self):
        """
        GIVEN 2 integers (latitude and longitude) given as attribute 
        WHEN we concatenate them in the string 'params_url' 
        THEN it returns a string usable as parameters with the API
        """

        pass


    def test_get_place_connection_with_requests_is_ok(self):
        """
        GIVEN a string 'base_url' and a string 'params_url' 
            formated with viable attributes
        WHEN we use those attributes with methods of the library requests 
        THEN it should return the proper status code.
        """

        pass


    def test_get_place_method_get_requests_fetch_result_in_json(self):
        """
        GIVEN a string 'base_url' and a string 'params_url' 
            formated with viable attributes
        WHEN we use those attributes with the method 'get' of the library requests 
        THEN it should retrieve a result (as a JSON) from the API.
        """

        pass


    def test_get_place_return_expected_result(self):
        """
        GIVEN the method 'resquests.get' has fetched a result in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """

        pass


    def test_get_place_exception_return_result_with_null_value(self):
        """
        GIVEN the method 'resquests.get' has fetched a result in JSON
        WHEN we search in the components of the JSON, 
            but we don't find the components we want
        THEN the function silently raises an exception, 
            and return those components but with null values.
        """

        pass


class TestGetPage:

    def test_get_page_format_input_properly(self):
        """
        GIVEN an (page_id) given as attribute 
        WHEN we concatenate it in the string 'params_url' 
        THEN it returns a string usable as parameters with the API
        """

        pass


    def test_get_page_connection_with_requests_is_ok(self):
        """
        GIVEN a string 'base_url' and a string 'params_url' 
            formated with viable attributes
        WHEN we use those attributes with methods of the library requests 
        THEN it should return the proper status code.
        """

        pass


    def test_get_page_method_get_requests_fetch_result_in_json(self):
        """
        GIVEN a string 'base_url' and a string 'params_url' 
            formated with viable attributes
        WHEN we use those attributes with the method 'get' of the library requests 
        THEN it should retrieve a result (as a JSON) from the API.
        """

        pass


    def test_get_page_return_expected_result(self):
        """
        GIVEN the method 'resquests.get' has fetched a result in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """

        pass


    def test_get_page_exception_return_result_with_null_value(self):
        """
        GIVEN the method 'resquests.get' has fetched a result in JSON
        WHEN we search in the components of the JSON, 
            but we don't find the components we want
        THEN the function silently raises an exception, 
            and return those components but with null values.
        """

        pass
