
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_string = ""
        if self.props == None:
            return ""
        else:
            for k in self.props:
                v = self.props[k]
                html_string += f' {k}="{v}"'
        return html_string
    
    def __repr__(self):
        return(f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode: {self.tag}, {self.value}, {self.props}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("message")
        if self.children == None:
            raise ValueError("different message")
        else:
            result = ""
            for child in self.children:
                hchild = child.to_html()
                result += hchild
            return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"