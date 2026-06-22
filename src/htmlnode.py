
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

