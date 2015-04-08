import unittest
import pep8

# A simple test using pep8 to check compliance
class TestCodeFormat(unittest.TestCase):

    def test_pep8_complicance(self):
        """Test that Docbuilder does comply with PEP8."""
        pep8style = pep8.StyleGuide(quiet=False,config_file="pep8.conf")
        result = pep8style.check_files(['docbuilder.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
