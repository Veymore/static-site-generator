import unittest

from src.htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
