import unittest
import pep8
import os
import subprocess

global lines
lines = "Not set"

# A function to clean up after each test.
def teardown():
    if os.path.isfile("testme.py"):
        os.remove("testme.py")
    if os.path.isfile("testdocs/testme.md"):
        os.remove("testdocs/testme.md")
    if os.path.exists("testdocs"):
        os.rmdir("testdocs")
    if os.path.isfile("docs/docbuilder.py.md"):
        os.remove("docs/docbuilder.py.md")
    if os.path.isfile("docs/docbuilder.md"):
        os.remove("docs/docbuilder.md")
    if os.path.exists("docs"):
        os.rmdir("docs")
    if os.path.isfile("documents/docbuilder.py.md"):
        os.remove("documents/docbuilder.py.md")
    if os.path.exists("documents"):
        os.rmdir("documents")

# A function to test against to check for Markdown syntax:
def buildup():
    file = open("testme.py", "w+")
    file.write("# # This is a title. \n # This is a comment. \n # * This is a bullet point. \n # *This* is an italic word. \n # **This** is a bold word. \n # ***This*** is an italic and bold word. \n This should be in a code block.")
    file.close()
    subprocess.call("python docbuilder.py testme.py testme.md testdocs", shell=True)
    testfile=open('testdocs/testme.md')
    global lines
    lines = testfile.readlines()
    testfile.close()

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
            
    def test_markdown_titles(self):
        """Test that titles appear correctly when compiled to Markdown."""
        teardown()
        buildup()
        global lines
        if lines[1] == "# This is a title.\n":
            print("Titles compile correctly to Markdown.")
            pass
        else:
            print("Title failed to compile correctly to Markdown.")
            print("Expected: # This is a title.\n")
            print("Received: " + lines[1])
            assert False
        pass
    
    def test_markdown_comments(self):
        """Test that normal comments appear correctly when compiled to Markdown."""
        teardown()
        buildup()
        global lines
        if lines[3] == "This is a comment.\n":
            print("Comments compile correctly to Markdown.")
            pass
        else:
            print("Comment failed to compile correctly to Markdown.")
            print("Expected: This is a comment.\n")
            print("Received: " + lines[3])
            assert False
    
    def test_markdown_bullet_points(self):
        """Test that bullet points appear correctly when compiled to Markdown."""
        teardown()
        buildup()
        global lines
        if lines[5] == "* This is a bullet point.\n":
            print("Bullet points compile correctly to Markdown.")
            pass
        else:
            print("Bullet points fail to compile correctly to Markdown.")
            print("Expected: * This is a bullet point.\n")
            print("Received: " + lines[5])
            assert False
    
    def test_markdown_italics(self):
        """Test that italics appear correctly when compiled to Markdown."""
        teardown()
        buildup()
        global lines
        if lines[7] == "*This* is an italic word.\n":
            print("Italics compile correctly to Markdown.")
            pass
        else:
            print("Italics failed to compile correctly to Markdown.")
            print("Expected: *This* is an italic word.\n")
            print("Received: " + lines[7])
            assert False
    
    def test_markdown_bolds(self):
        """Test that bolds appear correctly when compiled to Markdown."""
        teardown()
        buildup()
        global lines
        if lines[9] == "**This** is a bold word.\n":
            print("Bold compiled correctly to Markdown.")
            pass
        else:
            print("Bold failed to compile correctly to Markdown.")
            print("Expected: **This is a bold word.\n")
            print("Recieved: " + lines[9])
            assert False
    
    def test_markdown_italics_and_bolds(self):
        """Test that words that are both bold and italic appear correctly when compiled to Markdown."""
        teardown()
        buildup()
        global lines
        if lines[11] == "***This*** is an italic and bold word.\n":
            print("Both bold and italic compiles correctly to Markdown.")
            pass
        else:
            print("Both bold and italic phrases failed to compile to Markdown.")
            print("Expected: ***This*** is an italic and bold word.\n")
            print("Received: " + lines[11])
            assert False
    
    def test_markdown_codeblocks(self):
        """Test that codeblocks are correctly compiled to Markdown."""
        teardown()
        buildup()
        global lines
        if lines[13] == "```\n":
            if lines[14] == "This should be in a code block.\n":
                if lines[15] == "```\n":
                    print("Code blocks compile correctly to Markdown.")
                    pass
                else:
                    print("Code block failed to compile to Markdown.")
                    print("Expected: ```\n")
                    print("Received: " + lines[15])
                    assert False
            else:
               print("Code block failed to compile to Markdown.")
               print("Expected: This should be in a code block.\n")
               print("Received: " + lines[14])
               assert False
        else:
            print("Code block failed to compile to Markdown.")
            print("Expected: ```\n")
            print("Received: " + lines[13])
            assert False

# Remove all test data. 
teardown()
