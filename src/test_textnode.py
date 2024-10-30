import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_still_eq(self):
    node = TextNode("",TextType.CODE, None)
    node2 = TextNode("", TextType.CODE, None)
    self.assertEqual(node, node2)

  def not_eq(self):
    node = TextNode("This is this",TextType.BOLD, None)
    node2 = TextNode("This is not that", TextType.CODE, None)
    self.assertNotEqual(node, node2)

if __name__ == "__main__":
  unittest.main()
