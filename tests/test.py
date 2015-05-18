import unittest
import pep8
import os
import subprocess

global lines
lines = "Not set"

# A function to clean up after each test.
def teardown():
    if os.path.isfile("docs/docbuilder.md"):
        os.remove("docs/docbuilder.md")
    for root, dirs, files in os.walk("documents", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    for root, dirs, files in os.walk("testdocs", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

# A function to test against to check for Markdown syntax:
def buildup():
    file = open("testme.py", "w+")
    file.write("# # This is a title. \n # This is a comment. \n # * This is a bullet point. \n # *This* is an italic word. \n # **This** is a bold word. \n # ***This*** is an italic and bold word. \n print('This should be in a code block.')\n    print('This is an indented code block.')")
    file.close()
    subprocess.call("python docbuilder.py -i testme.py -o testme -d testdocs -q", shell=True)
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
        subprocess.call("python docbuilder.py -q", shell=True)
        # Test if Docbuilder can build it's own documentation.
        if os.path.isfile("docs/docbuilder.md"):
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
        subprocess.call("python docbuilder.py -i docbuilder.py -q", shell=True)
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
        subprocess.call("python docbuilder.py -i docbuilder.py -o docbuilder -q", shell=True)
        if os.path.isfile("docs/docbuilder.md"):
            print("Docbuilder successfully created using a from name and a to name.")
            pass
        else:
            print("Docbuilder failed to build correctly when given both a from filename and a to filename.")
            assert False
            
    def test_from_absolute_path(self):
        """Test to test Docbuilder behaves when given a file from an absolute path."""
        # Not yet implemented.
        pass
    
    def test_to_absolute_path(self):
        """Test to test Docbuilder behaves when writing to an absolute path."""
        # Not yet implemented.
        pass
            
    def test_custom_directories(self):
        """Test that Docbuilder can make custom documentation directories"""
        # Remove artefacts from previous tests.
        teardown()
        # This subprocess calls docbuilder.
        subprocess.call("python docbuilder.py -i docbuilder.py -o docbuilder.py --directory documents -q", shell=True)
        if os.path.isfile("documents/docbuilder.py.md"):
            print("Docbuilder successfully created a custom directory.")
            pass
        else:
            print("Docbuilder failed to create a custom directory.")
            assert False
            
    def test_custom_directory_flag(self):
        """Test that Docbuilder can make custom coumentation directories when using the -d flag"""
        # Remove artefacts from previous tests.
        teardown()
        # This subprocess calls docbuilder.
        subprocess.call("python docbuilder.py -i docbuilder.py -o docbuilder.py -d documents -q", shell=True)
        if os.path.isfile("documents/docbuilder.py.md"):
            print("Docbuilder successfully read the -d flag.")
            pass
        else:
            print("Docbuilder failed to create a custom directory based on the -d flag.")
            assert False
            
    def test_relative_path_input(self):
        """Test that Docbuilder will build correctly when given a nested folder input."""
        # Remove artefacts from previous tests.
        teardown()
        # This subprocess calls docbuilder.
        subprocess.call("python docbuilder.py -i examples/helloworld.pylit -o helloworld -d documents -q", shell=True)
        if os.path.isfile("documents/helloworld.md"):
            print("Docbuilder successfully built from a relative path.")
            pass
        else:
            print("Docbuilder failed to build from a relative path.")
            assert False
    
    def test_markdown_indent(self):
    """Test that Docbuilder can build indented Markdown."""
    # Remove artefacts from previous tests.
    #teardown()
    #subprocess.call("python docbuilder.py -i tests/testIndent.py -o testIndent -d testdocs -q")
    # NOT YET IMPLEMENTED
        
    def test_markdown_titles(self):
        """Test that titles appear correctly when compiled to Markdown."""
        teardown()
        buildup()
        global lines
        if lines[0] == "# This is a title.\n":
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
        if lines[2] == "This is a comment.\n":
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
        if lines[4] == "* This is a bullet point.\n":
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
        if lines[6] == "*This* is an italic word.\n":
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
        if lines[8] == "**This** is a bold word.\n":
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
        if lines[10] == "***This*** is an italic and bold word.\n":
            print("Both bold and italic compiles correctly to Markdown.")
            pass
        else:
            print("Both bold and italic phrases failed to compile to Markdown.")
            print("Expected: ***This*** is an italic and bold word.\n")
            print("Received: " + lines[10])
            assert False
    
    def test_markdown_codeblocks(self):
        """Test that codeblocks are correctly compiled to Markdown."""
        teardown()
        buildup()
        global lines
        if lines[13] == "```\n":
            if lines[14] == " print('This should be in a code block.')\n":
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
               print("Expected:  print('This should be in a code block.')\n")
               print("Received: " + lines[14])
               assert False
        else:
            print("Code block failed to compile to Markdown.")
            print("Expected: ```\n")
            print("Received: " + lines[12])
            assert False

    def test_markdown_indented_code_block(self):
        """Test to see if code blocks indent correctly when compiled to Markdown"""
        # This test has not yet been written.
        teardown()
        buildup()
        global lines
        if lines[17] == "```\n":
            if lines[18] == "    print('This is an indented code block.')\n":
                if lines[19] == "```\n":
                    print("Code blocks with indentation compile correctly to Markdown.")
                    pass
                else:
                    print("Indented code block failed to compile to Markdown.")
                    print("Expected: ```\n")
                    print("Received: " + lines[19])
                    assert False
            else:
                print("Indented code block failed to compile to Markdown.")
                print("Expected:     print('This is an indented code block.')\n")
                print("Recieved: " + lines[18])
                assert False
        else:
            print("Indented code block failed to compile to Markdown.")
            print("Expected: ```\n")
            print("Received: " + lines[17])
            assert False

# Remove all test data. 
teardown()
