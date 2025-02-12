class HTMLNode:
  def __init__(self,tag=None,value=None,children=None,props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")

  def props_to_html(self):
    if self.props is None:
      return ""

    props_html = ""
    for prop in self.props:
      props_html += f' {prop}="{self.props[prop]}"'
    return props_html
    # str = ""
    # for prop in self.props:
    #   str += prop + self.props[prop] + " "
    # return str.strip()
  
  def __repr__(self):
    print(f"""
    Tag: {self.tag}
    Value: {self.value}
    Children: {self.children}
    props: {self.props}
    """)

class LeafNode(HTMLNode):
  def __init__(self,tag,value, props=None):
    super().__init__(tag,value,None,props)

  def to_html(self):
    if not self.value:
      raise ValueError("All leaf nodes require a value.")

    if self.tag == None:
      return self.value
    else:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"
  
class ParentNode(HTMLNode):
  def __init__(self,tag,children,props=None):
    super().__init__(tag,None,children,props)
  
  def to_html(self):
    if self.tag is None:
      raise ValueError("Parent nodes require a HTML tag. (ex. <div></div>)")
    if self.children is None:
      raise ValueError("Parent nodes require at least one child node.")

    str_rep = ""

    for child in self.children:
      str_rep += child.to_html()

    return f"<{self.tag}{self.props_to_html()}>{str_rep}</{self.tag}>"
  
  def __repr__(self):
    return f"ParentNode({self.tag}, children: {self.children}, {self.props})"