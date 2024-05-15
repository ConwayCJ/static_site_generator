import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_valid_url(self):
        node = TextNode("This is a text node","italic","https://google.com")
        self.assertTrue(node.url is not None)
    def test_secure_url(self):
        node = TextNode("This is a text node","italic","https://google.com")
        self.assertTrue("https://" in node.url)

if __name__ == "__main__":
    unittest.main()
