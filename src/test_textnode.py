import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_again(self):
        node3 = TextNode("This is another test node", TextType.LINK, "https://boot.dev")
        node4 = TextNode("This is another test node", TextType.LINK, "https://boot.dev")
        self.assertEqual(node3, node4)

    def test_not_eq(self):
        node5 = TextNode("This is yet another test node", TextType.BOLD, "https://boot.dev")
        node6 = TextNode("This is yet another test node", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node5, node6)

    def test_no_url(self):
        node7 = TextNode("This is so many test nodes", TextType.CODE, None)
        node8 = TextNode("This is so many test nodes", TextType.CODE)
        self.assertEqual(node7, node8)

    def test_diff_types(self):
        node9 = TextNode("So many nodes to test", TextType.ITALIC)
        node10 = TextNode("So many nodes to test", TextType.BOLD)
        self.assertNotEqual(node9, node10)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def text_bold(self):
        node12 = TextNode("Bold me baby!", TextType.BOLD)
        html_node2 = text_node_to_html_node(node12)
        self.assertEqual(html_node2.tag, "b")
    
    def test_italic(self):
        node13 = TextNode("Make this italic", TextType.ITALIC)
        html_node3 = text_node_to_html_node(node13)
        self.assertEqual(html_node3.tag, "i")

if __name__ == "__main__":
    unittest.main()