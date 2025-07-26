import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_equality(self):
        node1 = HTMLNode("div", "Hello", None, {"class": "greeting"})
        node2 = HTMLNode("div", "Hello", None, {"class": "greeting"})
        self.assertEqual(node1, node2)

    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_attribute_values(self):
        node = HTMLNode("div", "Test content")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Test content")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = HTMLNode("p", "Content", None, {"class": "primary"})
        self.assertEqual(
            repr(node),
            "HTMLNode(p, Content, None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()