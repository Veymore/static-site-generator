from typing import Self
from src.htmlnode import LeafNode


# MARK: TextNode
class TextNode:
    # constructor
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        # The text content of the node:
        self.text = text
        # The type of text this node contains, which is just a string like "bold" or "italic":
        self.text_type = text_type
        # The URL of the link or image, if the text is a link. Default to None if nothing is passed in:
        self.url = url

    # compare with = is True when all properties match.
    def __eq__(self, other: Self) -> bool:
        if type(other) != TextNode:
            return False
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True

    # return String representation of the object
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


# MARK: TNtoHTML
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


# MARK: SplitNodesDelim
def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: str
) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            break
        text_blocks = node.text.split(delimiter)
        if len(text_blocks) % 2 == 0:
            raise Exception(f"Invalid markdown. {node = }")
        for index, text_block in enumerate(text_blocks):
            if index == 0 or index % 2 == 0:
                new_nodes.append(TextNode(text_block, "text"))
            else:
                new_nodes.append(TextNode(text_block, text_type))
    return new_nodes
