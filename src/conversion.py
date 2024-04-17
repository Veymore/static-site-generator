from textnode import TextNode
from htmlnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case "text":
            # This should become a LeafNode with no tag, just a raw text value.
            return LeafNode(None, text_node.text)
        case "bold":
            # This should become a LeafNode with a "b" tag and the text
            return LeafNode("b", text_node.text)
        case "italic":
            # "i" tag, text
            return LeafNode("i", text_node.text)
        case "code":
            # "code" tag, text
            return LeafNode("code", text_node.text)
        case "link":
            # "a" tag, anchor text, and "href" prop
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            # "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("TextNode does not have a valid text type.")
