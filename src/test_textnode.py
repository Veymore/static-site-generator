import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_uneq_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_uneq_different_texttype(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_uneq_different_url(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://example.com")
        self.assertNotEqual(node, node2)

    def test_uneq_compare_with_different_type(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        string = "This is a text node"
        self.assertNotEqual(node, string)

if __name__ == "__main__":
    unittest.main()