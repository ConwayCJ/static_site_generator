from textnode import TextNode
from htmlnode import LeafNode
def main():
	print("hello world")
	node = TextNode("This is a text node",
                	"bold",
                	"https://www.boot.dev")
	print(node.__repr__())

	def text_node_to_html_node(text_node):
		text_type_text = "text"
		text_type_bold = "bold"
		text_type_italic = "italic"
		text_type_code = "code"
		text_type_link = "link"
		text_type_image = "image"

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

  
main()