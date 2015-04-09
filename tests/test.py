import unittest
import pep8
import os
import subprocess

# A function to clean up after each test.
def teardown():
    if os.path.isfile("docs/docbuilder.py.md"):
        os.remove("docs/docbuilder.py.md")
    if os.path.isfile("docs/docbuilder.md"):
        os.remove("docs/docbuilder.md")
    if os.path.exists("docs"):
        os.rmdir("docs")

# A simple test using pep8 to check compliance
class TestCodeFormat(unittest.TestCase):

    def test_pep8_complicance(self):
        """Test that Docbuilder does comply with PEP8."""
        # Remove artefacts from previous tests.
        teardown()
        pep8style = pep8.StyleGuide(quiet=False,config_file="tests/pep8.conf")
        result = pep8style.check_files(['docbuilder.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    # A simple test to check if Docbuilder creates files and directories.                     
    def test_file_generation(self):
        """Test that Docbuilder can create it's own documentation."""
        # Remove artefacts from previous tests.
        teardown()
        # This subprocess calls docbuilder, so we can see if it's building it's own documentation.
        subprocess.call("python docbuilder.py", shell=True)
        # Test if Docbuilder can build it's own documentation.
        if os.path.isfile("docs/docbuilder.py.md"):
            print("Docbuilder successfully generated it's own documentation.")
            pass
        else:
            print("Docbuilder failed to generate it's own documentation.")
            assert False

    def test_file_guess(self):
        """Test to test that Docbuilder can guess a file name."""
        # Remove artefacts from previous tests.
        teardown()
        # This subprocess calls docbuilder.
        subprocess.call("python docbuilder.py docbuilder.py", shell=True)
        if os.path.isfile("docs/docbuilder.py.md"):
            print("Docbuilder successfully guessed a name for a file.")
            pass
        else:
            print("Docbuilder failed to guess a filename.")
            assert False
            
    def test_file_given(self):
        """Test to test that Docbuilder behaves correctly when given both a file to document, and a filename for where to place the documentation.""" 
        # Remove artefacts from previous tests.
        teardown()
        # This subprocess calls docbuilder.
        subprocess.call("python docbuilder.py docbuilder.py docbuilder.md", shell=True)
        if os.path.isfile("docs/docbuilder.md"):
            print("Docbuilder successfully created using a from name and a to name.")
            pass
        else:
            print("Docbuilder failed to build correctly when given both a from filename and a to filename.")
            assert False
            
    def test_custom_directories(self):
        """Test that Docbuilder can make custom documentation directories"""
        # Remove artefacts from previous tests.
        teardown()
        # This subprocess calls docbuilder.
        subprocess.call("python docbuilder.py docbuilder.py docbuilder.py.md documents", shell=True)
        if os.path.isfile("documents/docbuilder.py.md"):
            print("Docbuilder successfully created a custom directory.")
            pass
        else:
            print("Docbuilder failed to create a custom directory.")
            assert False
