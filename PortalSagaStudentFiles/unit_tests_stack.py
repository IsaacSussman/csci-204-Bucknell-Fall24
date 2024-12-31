from stack import *
import unittest

class TestStack(unittest.TestCase):
    def testInit(self):
        l = LinkedStack()
        self.assertIsNone(l._top)
        self.assertEqual(l._size, 0)
    
    def test_push_only(self):
        l = LinkedStack()
        l.push("help")
        self.assertEqual(l._size, 1)
        self.assertEqual(str(l), "top --> help")

    def test_push(self):
        l = LinkedStack()
        l.push("help")
        l.push("hel")
        l.push("he")
        self.assertEqual(l._size, 3)
        self.assertEqual(str(l), "top --> he hel help")
    
    def test_peek_empty(self):
        l = LinkedStack()
        self.assertIsNone(l.peek())
        self.assertIsNone(l._top)
        self.assertEqual(l._size, 0)
    
    def test_peek(self):
        l = LinkedStack()
        l.push("help")
        l.push("hel")
        l.push("he")
        self.assertEqual(l.peek(), "he")
        self.assertEqual(l._size, 3)
        self.assertEqual(str(l), "top --> he hel help")
    
    def test_pop_empty(self):
        l = LinkedStack()
        self.assertIsNone(l.pop())
        self.assertIsNone(l._top)
        self.assertEqual(l._size, 0)
    
    def test_pop(self):
        l = LinkedStack()
        l.push("help")
        l.push("hel")
        l.push("he")
        self.assertEqual(l.pop(), "he")
        self.assertEqual(l._size, 2)
        self.assertEqual(str(l), "top --> hel help")
    



if __name__ == '__main__':
    unittest.main()