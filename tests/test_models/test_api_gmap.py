from grandpy.models.api_gmap import APIgmap


def test_get_location_return_expected_script():
    """
    GIVEN the method 'resquests.get' has fetched a script in JSON
    WHEN we search in the components of the JSON
    THEN we find the specified components and return their values.
    """

    script = APIgmap()
    assert script.get_location(
        question='tour eiffel') == (48.85837009999999, 2.2944813)
