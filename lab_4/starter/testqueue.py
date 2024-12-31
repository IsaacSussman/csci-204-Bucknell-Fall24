import unittest
from unittest.mock import patch
from queue import MyQueue

"""
Name each method beginning with test_

Here are examples of the tests you can run:
self.assertIsInstance(x, str) # variable, name of type
self.assertEqual(x, y) # tests if x == y
self.assertTrue(x) # tests if x is True
self.assertFalse(x) # tests if x is False
self.assertIn(stringToLookFor, largeString, "errorMessage if not found")

with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
    # run some codes
    self.assertEqual(fake_stdout.getvalue(), "some expected printed lines")

with self.assertRaises(ExceptionClass):
  code to run
"""
class TestQueue(unittest.TestCase):
  def test_init(self):
    temp = MyQueue()
    self.assertEqual(len(temp),0)
    self.assertEqual(str(temp),"")
    self.assertEqual(len(temp._array),2)
    self.assertIsNone(temp.front())
  
  def test_enqueue(self):
    temp = MyQueue()
    temp.enqueue("1")
    self.assertEqual(len(temp),1)
    self.assertEqual(str(temp),"front 1 back")
    self.assertEqual(len(temp._array),2)
    temp.enqueue("2")
    self.assertEqual(len(temp),2)
    temp.enqueue("3")
    temp.enqueue("4")
    self.assertEqual(str(temp),"front 1 2 3 4 back")
    self.assertEqual(len(temp._array),4)
  
  def test_dequeue(self):
    temp = MyQueue()
    self.assertEqual(temp.dequeue(),None)
    temp.enqueue("1")
    temp.enqueue("2")
    self.assertEqual(temp.dequeue(), "1")
    temp.enqueue("3")
    self.assertEqual(len(temp._array),2)
    self.assertEqual(len(temp),2)
    
    self.assertEqual(str(temp),"front 2 3 back")
    self.assertEqual(temp.dequeue(), "2")
    self.assertEqual(str(temp),"front 3 back")
    
    self.assertEqual(temp.dequeue(), "3")
    self.assertTrue(temp.is_empty())
    temp.enqueue("1")
    temp.enqueue("2")
    temp.enqueue("3")
    temp.enqueue("4")
    temp.enqueue("5")
    temp.enqueue("6")
    self.assertEqual(temp.dequeue(), "1")
    self.assertEqual(temp.dequeue(), "2")
    self.assertEqual(temp.dequeue(), "3")
    self.assertEqual(temp.dequeue(), "4")
    self.assertEqual(temp.dequeue(), "5")
    self.assertEqual(temp.dequeue(), "6")
  
  def test_len(self):
    temp = MyQueue()
    self.assertEqual(len(temp), 0)
    temp.enqueue("tehehe")
    self.assertEqual(len(temp), 1)

  def test_empty(self):
    temp = MyQueue()
    self.assertTrue(temp.is_empty())
    temp.enqueue("tehehe")
    self.assertFalse(temp.is_empty())
  
  def test_front(self):
    temp = MyQueue()
    temp.enqueue("J")
    self.assertEqual(temp.front(), "J")
    temp.enqueue("K")
    self.assertEqual(temp.front(), "J")
    temp.dequeue()
    self.assertEqual(temp.front(), "K")
  
  def test_bound(self):
    temp = MyQueue(1)
    self.assertEqual(len(temp),0)
    self.assertEqual(str(temp),"")
    self.assertEqual(len(temp._array),1)
    self.assertIsNone(temp.front())
    temp.enqueue("1")
    self.assertEqual(temp.enqueue("NOOOOOO"), -1)
    self.assertEqual(str(temp), "front 1 back")




unittest.main()