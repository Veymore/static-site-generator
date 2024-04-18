import unittest

from src.htmlnode import LeafNode
from src.textnode import TextNode, text_node_to_html_node, split_nodes_delimiter


# MARK: TextNode
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


# MARK: TNtoHTML
class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is normal text", "text")
        actualResult = text_node_to_html_node(node)
        expectedResult = LeafNode(None, "This is normal text")
        self.assertEqual(actualResult, expectedResult)

    def test_bold(self):
        node = TextNode("This is bold text", "bold")
        actualResult = text_node_to_html_node(node)
        expectedResult = LeafNode("b", "This is bold text")
        self.assertEqual(actualResult, expectedResult)

    def test_italic(self):
        node = TextNode("This is italic text", "italic")
        actualResult = text_node_to_html_node(node)
        expectedResult = LeafNode("i", "This is italic text")
        self.assertEqual(actualResult, expectedResult)

    def test_code(self):
        node = TextNode("This is code text", "code")
        actualResult = text_node_to_html_node(node)
        expectedResult = LeafNode("code", "This is code text")
        self.assertEqual(actualResult, expectedResult)

    def test_link(self):
        node = TextNode(
            "Click here for free unittests", "link", "https://get.rickrolled.gg"
        )
        actualResult = text_node_to_html_node(node)
        expectedResult = LeafNode(
            "a", "Click here for free unittests", {"href": "https://get.rickrolled.gg"}
        )
        self.assertEqual(actualResult, expectedResult)

    def test_image(self):
        node = TextNode(
            "This is an image", "image", "https://images.pictureexamples.gg/kekw.png"
        )
        actualResult = text_node_to_html_node(node)
        expectedResult = LeafNode(
            "img",
            "",
            {
                "src": "https://images.pictureexamples.gg/kekw.png",
                "alt": "This is an image",
            },
        )
        self.assertEqual(actualResult, expectedResult)

    def test_unknown(self):
        node = TextNode("This is next level text", "next_level")
        self.assertRaises(Exception, text_node_to_html_node, node)


# MARK: SplitNodesDelim
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        expectedResult = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, expectedResult)

    def test_bold(self):
        node = TextNode("This is text with a **bolded** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        expectedResult = [
            TextNode("This is text with a ", "text"),
            TextNode("bolded", "bold"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, expectedResult)

    def test_italic(self):
        node = TextNode("This is text with an *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        expectedResult = [
            TextNode("This is text with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word", "text"),
        ]
        self.assertEqual(new_nodes, expectedResult)

    def test_not_textnode(self):
        node = TextNode("bolded", "bold")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        expectedResult = [TextNode("bolded", "bold")]
        self.assertEqual(new_nodes, expectedResult)

    def test_invalid_markdown(self):
        node = TextNode("This is text with a **bolded word", "text")
        self.assertRaises(Exception, split_nodes_delimiter, [node], "**", "bold")

    def test_nested(self):
        node = TextNode("This is an *italic and **bold** word*.", "text")
        new_nodes = new_nodes = split_nodes_delimiter([node], "**", "bold")
        expectedResult = [
            TextNode("This is an *italic and ", "text"),
            TextNode("bold", "bold"),
            TextNode(" word*.", "text"),
        ]
        self.assertEqual(new_nodes, expectedResult)


if __name__ == "__main__":
    unittest.main()
