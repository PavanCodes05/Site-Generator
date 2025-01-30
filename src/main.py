from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    dummy = HTMLNode("p", "This is a paragraph", None, {"href": "https://somewhere.com", "src": "Hello this is the page"})
    print(dummy)

main()