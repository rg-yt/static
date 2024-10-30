from textnode import *

def main():
  node = TextNode("texting", NodeType.BOLD, "https://www.boot.dev")
  node2 = TextNode("testing", NodeType.ITALIC)
  print(node)
  print(node2)
  print(node.__eq__(node2))
  

main()