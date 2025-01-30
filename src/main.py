from textnode import TextType, TextNode

def main():
    dummy = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    print(dummy)

main()