from textnode import TextType
class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	def to_html(self):
		raise NotImplementedError
	def props_to_html(self):
		if self.props is None:
			return ""
		result = ""
		for k, v in self.props.items():
			result += f' {k}="{v}"'
		return result
	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})" 
	
class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)
	def to_html(self):
		if self.value == None:
			raise ValueError("Leaf node has no value.")
		if self.tag == None:
			return self.value
		return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)
	def to_html(self):
		if self.tag is None:
			raise ValueError("Parent node is missing tag.")
		if self.children is None:
			raise ValueError("Parent node is missing children.")
		result = ""
		for child in self.children:
			result += child.to_html()
		return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'

def text_node_to_html_node(text_node):
	if text_node.text_type not in TextType:
		raise Exception("Invalid text type!")
	match (text_node.text_type):
		case TextType.TEXT:
			return LeafNode(None, text_node.text)
		case TextType.BOLD:
			return LeafNode("b", text_node.text)
		case TextType.ITALIC:
			return LeafNode("i", text_node.text)
		case TextType.CODE:
			return LeafNode("code", text_node.text)
		case TextType.LINK:
			return LeafNode("a", text_node.text, {"href": text_node.url})
		case TextType.IMAGE:
			return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})