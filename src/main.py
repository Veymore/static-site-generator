from textnode import TextNode as tn
from htmlnode import HTMLNode as hn

testnode = hn(None, None, None, {"href": "https://www.google.com", "target": "_blank"})

print(testnode.props_to_html())

print(testnode)
