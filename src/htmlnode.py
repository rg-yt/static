class HTMLNode:
  def __init__(self, tag = None, value = None, children = None, props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    if self.props == None:
      return ""
    return ''.join(f' {key}="{value}"' for key, value in self.props.items())
  
  def __repr__(self):
      return f"HTML NODE({self.tag}, {self.value}, children: {self.children}, {self.props})"
  
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props = None):
    super().__init__(tag, value, None , props)

  def to_html(self):
    if self.value == None:
      raise ValueError
    if self.tag == None:
      return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
  
  def __repr__(self):
      return f"LEAF NODE({self.tag}, {self.value}, {self.props})"
