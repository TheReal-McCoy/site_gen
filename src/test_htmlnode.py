import unittest

# Import your HTMLNode class from the htmlnode file
from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()