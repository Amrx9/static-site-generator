import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    class TestTextNodeToHTMLNode(unittest.TestCase):
        def test_text_node_to_html_node(self):
            node = TextNode("Hello, world!", TextType.TEXT)
            html_node = node.text_node_to_html_node()
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "Hello, world!")

            node = TextNode("Bold text", TextType.BOLD)
            html_node = node.text_node_to_html_node()
            self.assertEqual(html_node.tag, "b")
            self.assertEqual(html_node.value, "Bold text")

            node = TextNode("Click me", TextType.LINK, "https://example.com")
            html_node = node.text_node_to_html_node()
            self.assertEqual(html_node.tag, "a")
            self.assertEqual(html_node.value, "Click me")
            self.assertEqual(html_node.props, {"href": "https://example.com"})

            node = TextNode("Image alt text", TextType.IMAGE, "image.jpg")
            html_node = node.text_node_to_html_node()
            self.assertEqual(html_node.tag, "img")
            self.assertEqual(html_node.value, "")
            self.assertEqual(html_node.props, {"src": "image.jpg", "alt": "Image alt text"})


            with self.assertRaises(ValueError):
                node = TextNode("text", "invalid_type")
                node.text_node_to_html_node()


if __name__ == "__main__":
    unittest.main()