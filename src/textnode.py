from typing import Self

class TextNode:
    #constructor
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        #The text content of the node:
        self.text = text
        #The type of text this node contains, which is just a string like "bold" or "italic":
        self.text_type = text_type
        #The URL of the link or image, if the text is a link. Default to None if nothing is passed in:
        self.url = url

    #compare with = is True when all properties match.
    def __eq__(self, other: Self) -> bool:
        if self.text is not other.text:
            return False
        if self.text_type is not other.text_type:
            return False
        if self.url is not other.url:
            return False
        return True
    
    #return String representation of the object
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
