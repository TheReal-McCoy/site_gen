import unittest

# Import your HTMLNode class from the htmlnode file
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # 1. Create a node with some properties
        node = HTMLNode(
            tag="a",
            value="Boot.dev",
            props={"href": "https://www.boot.dev", "target": "_blank"}
        )
        
        # 2. Assert that props_to_html returns the expected string
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boot.dev" target="_blank"'
        )

    def test_it_again(self):
        node1 = HTMLNode("b", "Boot.dev", props={"href": "https://www.boot.dev", "target": "_blank"})
        self.assertNotEqual(node1.props_to_html(), ' href="https://www.boots.dev" target="_blank"')
    # You can add more test methods here!
    # Try testing a node with None as props, or a node with different properties.

    def third_test(self):
        node2 = HTMLNode(value="Clog.dev", props={"href": "https://www.clog.dev", "target": "_blank"})
        self.assertEqual(node2.props_to_html(), ' href="https://www.clog.dev" target="_blank"')

    def testleaf(self):
        node3 = LeafNode(tag="b", value="wowwee.com", props={"href": "https://www.wowwee.com", "target": "_blank"})
        self.assertEqual(node3.to_html(),'<b href="https://www.wowwee.com" target="_blank">wowwee.com</b>')

    def testtag(self):
        node4 = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node4.to_html(),'<p>Hello, world!</p>')

    def testnotag(self):
        node5 = LeafNode(None, value="No tag inserted")
        self.assertEqual(node5.to_html(),'No tag inserted')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()