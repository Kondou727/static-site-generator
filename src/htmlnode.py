class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	def to_html(self):
		raise NotImplementedError
	def props_to_html(self):
		result = ""
		for k, v in self.props.items():
			result += f' {k}="{v}"'
		return result
	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" 
	
class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)
	def to_html(self):
		if self.value == None:
			raise ValueError("Leaf node has no value.")
		if self.tag == None:
			return self.value
		if self.props == None:
			return f'<{self.tag}>{self.value}</{self.tag}>'
		return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
	