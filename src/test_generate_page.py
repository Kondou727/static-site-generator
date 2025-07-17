import unittest
import tempfile
from generate_page import extract_title

class TestGenerateSite(unittest.TestCase):
    def test_extract_site(self):
        expected = "Tolkien Fan Club"
        self.assertEqual(extract_title("./static/content/index.md"), expected)