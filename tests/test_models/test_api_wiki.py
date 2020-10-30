from grandpy.models.api_wiki import APIwiki


def test_get_page_return_expected_script():
    """
    GIVEN the method 'resquests.get' has fetched a script in JSON
    WHEN we search in the components of the JSON
    THEN we find the specified components and return their values.
    """

    script = APIwiki()
    assert script.get_page(48.85837009999999, 2.2944813) == 1359783


def test_get_place_return_expected_script():
    """
    GIVEN the method 'resquests.get' has fetched a script in JSON
    WHEN we search in the components of the JSON
    THEN we find the specified components and return their values.
    """

    script = APIwiki()
    assert script.get_place(1359783) == (
        """La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, """
        """à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. """
        """Son adresse officielle est 5, avenue Anatole-France."""
    )
