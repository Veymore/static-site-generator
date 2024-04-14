import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_props_to_html_3(self):
        node = HTMLNode(None, None, None, None)
        actualResult = node.props_to_html()
        expectedString = ""
        self.assertEqual(actualResult, expectedString)

    def test_repr(self):
        node = HTMLNode(None, None, None, None)
        actualResult = node
        expectedString = f"HTMLNode(None, None, None, None)"
        self.assertEqual(str(actualResult), expectedString)

    def test_call_to_html(self):
        node = HTMLNode(None, None, None, None)
        self.assertRaises(NotImplementedError, node.to_html)


# MARK: TestLeafNode
class TestLeafNode(unittest.TestCase):
    def test_to_html_1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        actualResult = node.to_html()
        expectedString = "<p>This is a paragraph of text.</p>"
        self.assertEqual(actualResult, expectedString)

    def test_to_html_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        actualResult = node.to_html()
        expectedString = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(actualResult, expectedString)

    def test_no_value(self):
        self.assertRaises(ValueError, LeafNode, None, None, None)


# MARK: TestParentNode
class TestParentNode(unittest.TestCase):
    # test unit example
    def test_to_html_1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        actualResult = node.to_html()
        expectedString = (
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        self.assertEqual(actualResult, expectedString)

    # tests complicated setup, links, font awesome class import
    def test_to_html_2(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("h1", "The best chapter of my life"),
                        LeafNode(
                            "a",
                            "see for yourself.",
                            {"href": "https://awesomechapters.gg/the-best-yet.htm"},
                        ),
                    ],
                ),
                LeafNode("i", "placeholder", {"class": "fa-solid fa-user"}),
            ],
        )
        actualResult = node.to_html()
        expectedString = '<div><p><h1>The best chapter of my life</h1><a href="https://awesomechapters.gg/the-best-yet.htm">see for yourself.</a></p><i class="fa-solid fa-user">placeholder</i></div>'
        self.assertEqual(actualResult, expectedString)

    # tests deep linear recursion pattern
    def test_to_html_3(self):
        node = ParentNode(
            "h1",
            [
                ParentNode(
                    "div",
                    [
                        ParentNode(
                            "h2",
                            [
                                ParentNode(
                                    "div",
                                    [
                                        ParentNode(
                                            "h3",
                                            [
                                                LeafNode(
                                                    "div",
                                                    "Hidden Div Technique activated",
                                                    {"centered": "hopefully"},
                                                )
                                            ],
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                )
            ],
        )
        actualResult = node.to_html()
        expectedString = '<h1><div><h2><div><h3><div centered="hopefully">Hidden Div Technique activated</div></h3></div></h2></div></h1>'
        self.assertEqual(actualResult, expectedString)

    # tests recursion on later child positions, None as String, unordered lists, CSS style values in tag
    def test_to_html_4(self):
        node = ParentNode(
            "div",
            [
                LeafNode("h1", "EXTRABLATT, EXTRABLATT", {"style": "color:red;"}),
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "actually"),
                        LeafNode("li", "None"),
                        LeafNode("li", "important"),
                        LeafNode("li", "!"),
                    ],
                ),
            ],
        )
        actualResult = node.to_html()
        expectedString = '<div><h1 style="color:red;">EXTRABLATT, EXTRABLATT</h1><ul><li>actually</li><li>None</li><li>important</li><li>!</li></ul></div>'
        self.assertEqual(actualResult, expectedString)

    def test_no_children(self):
        self.assertRaises(ValueError, ParentNode, "test", None, {"test": "test"})

    def test_no_tag(self):
        self.assertRaises(ValueError, ParentNode, None, "test", {"test": "test"})


if __name__ == "__main__":
    unittest.main()
