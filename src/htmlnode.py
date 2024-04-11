from typing import Self


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
        for prop in self.props.items():
            prop_to_html += f' {prop[0]}="{prop[1]}"'
        return prop_to_html

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
