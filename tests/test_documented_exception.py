import unittest
from documented_exception import BaseDocumentedException
from test_fixtures import DummyDocumentedException

class TestDocumentedException(unittest.TestCase):

    def test_display_lorem_on_raise_dummy_exception(self):
        try:
            raise DummyDocumentedException
        except BaseDocumentedException as error:
            print(error)
            self.assertEqual(
        """\t\n        Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
        qui officia deserunt mollit anim id est laborum.
        
	
        If this is an issue with 'documented_exception', feel free to submit report here:
        https://github.com/Ni-g-3l/documented-exception/issues/new\n    """, str(error))