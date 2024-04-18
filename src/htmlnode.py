from typing import Self


# MARK: HTMLNode
class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list[Self] = None,
        props: dict[str, str] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> NotImplementedError:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        prop_to_html = ""
        if self.props == None:
            return ""
        for prop in self.props.items():
            prop_to_html += f' {prop[0]}="{prop[1]}"'
        return prop_to_html

    # compare with = is True when all properties match.
    def __eq__(self, other: Self) -> bool:
        if type(other) != type(self):
            return False
        if self.tag != other.tag:
            return False
        if self.value != other.value:
            return False
        if self.children != other.children:
            return False
        if self.props != other.props:
            return False
        return True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"


# MARK: LeafNode
class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        props: dict[str, str] = None,
    ) -> None:
        if value == None:
            raise ValueError("Value is none. All LeafNodes require a value.")
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.tag == None:
            return self.value
        if self.props != None:
            rendered_props = self.props_to_html()
        else:
            rendered_props = ""
        return f"<{self.tag}{rendered_props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str = None,
        children: list[HTMLNode] = None,
        props: dict[str, str] = None,
    ) -> None:
        if tag == None:
            raise ValueError("ParentNode needs to have a tag assigned.")
        if children == None:
            raise ValueError("ParentNode needs to have children.")
        super().__init__(tag, None, children, props)

    def to_html(self):
        rendered_props = self.props_to_html()
        rendered_children = ""
        if self.children is not None:
            for child in self.children:
                rendered_child = child.to_html()
                rendered_children += rendered_child
        return f"<{self.tag}{rendered_props}>{rendered_children}</{self.tag}>"
