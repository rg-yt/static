import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
  #HTML NODE TEST
  
  def test_to_html_props(self):
    node = HTMLNode(
      "div",
      "Hello, world!",
      None,
      {"class": "greeting", "href": "https://boot.dev"},
    )
    self.assertEqual(
      node.props_to_html(),
      ' class="greeting" href="https://boot.dev"',
    )

  def test_values(self):
    node = HTMLNode(
        "div",
        "I wish I could read",
    )
    self.assertEqual(
        node.tag,
        "div",
    )
    self.assertEqual(
        node.value,
        "I wish I could read",
    )
    self.assertEqual(
        node.children,
        None,
    )
    self.assertEqual(
        node.props,
        None,
    )

  def test_repr(self):
    node = HTMLNode(
        "p",
        "What a strange world",
        None,
        {"class": "primary"},
    )
    self.assertEqual(
        node.__repr__(),
        "HTML NODE(p, What a strange world, children: None, {'class': 'primary'})",
      )

  #LEAF NODES TEST

  def test_to_html_no_children(self):
    node = LeafNode("p", "Hello, world!", {'class': 'primary'})
    self.assertEqual(node.to_html(), '<p class="primary">Hello, world!</p>')

  def test_to_html_no_tag(self):
    node = LeafNode(None, "Hello, world!")
    self.assertEqual(node.to_html(), "Hello, world!")

  #PARENT NODE TEST

  def test_to_html_parent_with_children(self):
    node = ParentNode(
      "p",
      [
          LeafNode("b", "Bold text"),
          LeafNode(None, "Normal text"),
          LeafNode("i", "italic text"),
          LeafNode(None, "Normal text"),
      ],
    )
    self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


if __name__ == "__main__":
  unittest.main()