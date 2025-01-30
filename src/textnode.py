from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type:TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eg__(self, obj1, obj2):
        return (obj1.text == obj2.text and
                obj1.text_type == obj2.text_type and 
                obj1.url == obj2.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"