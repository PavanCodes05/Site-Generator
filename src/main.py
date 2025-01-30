from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    dummy = LeafNode("p", "This is a paragraph")
    print(dummy)
    print(dummy.to_html())
main()