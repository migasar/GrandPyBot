from grandpy.models.api_wiki import APIwiki


class TestAPIwikiGetPlace:

    def test_get_place_fail_with_other_attribute_type_than_integer(self):
        """
        GIVEN the attribute passed to the method is not an integer
        WHEN the method tries to run
        THEN it raises an error.
        """
        script = APIwiki()
        assert script.get_place('foo') == TypeError


    def test_get_place_return_expected_script(self):
        """
        GIVEN the method 'resquests.get' has fetched a script in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """
        script = APIwiki()
        assert script.get_place(1, 3) == 141576


    def test_get_place_exception_return_script_with_null_value(self):
        """
        GIVEN the method 'resquests.get' has fetched a script in JSON
        WHEN we search in the components of the JSON, 
            but we don't find the components we want
        THEN the function silently raises an exception, 
            and return those components but with null values.
        """
        script = APIwiki()
        assert script.get_place(None, None) is None


class TestAPIwikiGetPage:

    def test_get_page_fail_with_other_attribute_type_than_integer(self):
        """
        GIVEN the attribute passed to the method is not an integer
        WHEN the method tries to run
        THEN it raises an error.
        """
        script = APIwiki()
        assert script.get_page('foo') == TypeError


    def test_get_page_return_expected_script(self):
        """
        GIVEN the method 'resquests.get' has fetched a script in JSON
        WHEN we search in the components of the JSON
        THEN we find the specified components and return their values.
        """
        script = APIwiki()
        assert script.get_page(141576) == "Lorem Ipsum ..."


    def test_get_page_exception_return_script_with_null_value(self):
        """
        GIVEN the method 'resquests.get' has fetched a script in JSON
        WHEN we search in the components of the JSON, 
            but we don't find the components we want
        THEN the function silently raises an exception, 
            and return those components but with null values.
        """
        script = APIwiki()
        assert script.get_page(None) is None
