import unittest
import pep8
import os

# A simple test using pep8 to check compliance
class TestCodeFormat(unittest.TestCase):

    def test_pep8_complicance(self):
        """Test that Docbuilder does comply with PEP8."""
        pep8style = pep8.StyleGuide(quiet=False,config_file="tests/pep8.conf")
        result = pep8style.check_files(['docbuilder.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    # A simple test to check if Docbuilder creates files and directories.                     
    def test_file_generation(self):
        """Test that Docbuilder can create it's own documentation."""
        # This subprocess calls docbuilder, so we can see if it's building it's own documentation.
        subprocess.call("python ../docbuilder.py", shell=True)
        # Test if Docbuilder can build it's own documentation.
        if os.path.isfile("docs/docbuilder.py.md):
            print("Docbuilder successfully generated it's own documentation.")
            pass
        else:
            print("Docbuilder failed to generate it's own documentation.")
            assert False
