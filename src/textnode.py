from enum import Enum

class NodeType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic" 
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
      self.text = text
      self.text_type = text_type.value
      self.url = url

    def __eq__(self, other_node):
      if self.text != other_node.text:
        return False
      if self.text_type != other_node.text_type:
        return False
      if self.url != other_node.url:
        return False
      return True
      
    def __repr__(self):
      return f"TEXT NODE({self.text}, {self.text_type}, {self.url})"

