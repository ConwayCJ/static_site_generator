from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
	def __init__(self,text,type_text,url=None):
		self.text = text
		self.type_text = type_text
		self.url = url

	def __eq__(self,node2):
		return (
			self.type_text == node2.type_text
			and self.text == node2.text
			and self.url == node2.url
		)

	def __repr__(self):
  		return f"TextNode({self.text},{self.type_text},{self.url})"

def text_node_to_html_node(text_node):
	if text_node.type == text_type_text:
		return LeafNode(None, text_node.value)
	if text_node.type == text_type_bold:
		return LeafNode("b", text_node.value)
	if text_node.type == text_type_italic:
		return LeafNode("i", text_node.value)
	if text_node.type == text_type_code:
		return LeafNode("code", text_node.value)
	if text_node.type == text_type_link:
		return LeafNode("a", text_node.value, {"href": text_node.url})
	if text_node.type == text_type_image: 
		return LeafNode("img", None, {
			"src": text_node.url,
			"alt": text_node.value,
		})
	
	raise Exception("Invalid text node.")

def split_nodes_delimiter(old_nodes, delimiter, text_type):

	raise Exception("invalid list of nodes")