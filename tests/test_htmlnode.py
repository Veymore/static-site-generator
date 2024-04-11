import unittest

from src.htmlnode import HTMLNode, LeafNode


# MARK: TestHtmlNode
class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode(
            None, None, None, {"href": "https://www.google.com", "target": "_blank"}
        )
        actualResult = node.props_to_html()
        expectedString = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(actualResult, expectedString)

    def test_props_to_html_2(self):
        node = HTMLNode(
            "test",
            "test",
            None,
            {"h1": "za best in za west", "div": "please center me"},
        )
        actualResult = node.props_to_html()
        expectedString = ' h1="za best in za west" div="please center me"'
        self.assertEqual(actualResult, expectedString)


# MARK: TestLeafNode
class TestLeafNode(unittest.TestCase):
    def test_to_html_1(self):
        node = LeafNode("This is a paragraph of text.", "p")
        actualResult = node.to_html()
        expectedString = "<p>This is a paragraph of text.</p>"
        self.assertEqual(actualResult, expectedString)

    def test_to_html_2(self):
        node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        actualResult = node.to_html()
        expectedString = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(actualResult, expectedString)


if __name__ == "__main__":
    unittest.main()
