from grandpy.models.api_gmap import APIgmap


class TestAPIgmap:

    def test_get_location_fail_with_other_attribute_type_than_string(self):
        """
        GIVEN the attribute passed to the method is not a string
        WHEN the method tries to run
        THEN it raises an error.
        """
        script = APIgmap()
        assert self.script.get_location(7) == TypeError


    def test_get_location_return_expected_script(self):
        """
        GIVEN the method 'resquests.get' has fetched a script in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """
        script = APIgmap()
        assert self.script.get_location(question='tour eiffel') == 1, 3
        # 'tour eiffel' assertion should be compared 
        # to latitude and longitude of the Eiffel Tower on Google Map


    def test_get_location_exception_return_script_with_null_value(self):
        """
        GIVEN the method 'resquests.get' has fetched a script in JSON
        WHEN we search in the components of the JSON, 
            but we don't find the components we want
        THEN the function silently raises an exception, 
            and return those components but with null values.
        """
        script = APIgmap()
        assert self.script.get_location('a') is None, None
