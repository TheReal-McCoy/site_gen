import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_again(self):
        node3 = TextNode("This is another test node", TextType.LINKS, "https://boot.dev")
        node4 = TextNode("This is another test node", TextType.LINKS, "https://boot.dev")
        self.assertEqual(node3, node4)

    def test_not_eq(self):
        node5 = TextNode("This is yet another test node", TextType.BOLD, "https://boot.dev")
        node6 = TextNode("This is yet another test node", TextType.LINKS, "https://boot.dev")
        self.assertNotEqual(node5, node6)

    def test_no_url(self):
        node7 = TextNode("This is so many test nodes", TextType.CODE, None)
        node8 = TextNode("This is so many test nodes", TextType.CODE)
        self.assertEqual(node7, node8)

    def test_diff_types(self):
        node9 = TextNode("So many nodes to test", TextType.ITALIC)
        node10 = TextNode("So many nodes to test", TextType.BOLD)
        self.assertNotEqual(node9, node10)

if __name__ == "__main__":
    unittest.main()