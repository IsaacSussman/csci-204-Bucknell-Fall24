import unittest
from stack import MyStack

class TestStack(unittest.TestCase):
    # TODO: Implement your unit tests here
    # Hint: You should implement test cases for each method of MyStack class
    pass
    def test_init(self):
        temp = MyStack()
        self.assertEqual(temp._array[0], None)
        self.assertEqual(temp._array[1], None)
    
    def test_is_empty(self):
        temp = MyStack()
        self.assertEqual(temp.is_empty(), True)
        temp.push(2)
        temp.push(2)
        self.assertEqual(temp.is_empty(), False)
        temp.pop()
        self.assertEqual(temp.is_empty(), False)
    
    def test_expand(self):
        temp = MyStack()
        temp._expand()
        self.assertEqual(temp._capacity, 4)
        self.assertEqual(temp._size, 0)
        for i in temp._array._data:
            self.assertEqual(i, None)

    def test_push(self):
        temp=MyStack()
        temp.push(2)
        self.assertEqual(temp._array[0], 2)
        temp.push(2)
        self.assertEqual(temp._array[1], 2)
        temp.push(2)
        self.assertEqual(temp._capacity, 4)
        self.assertEqual(temp._array[2], 2)

    def test_pop(self):
        temp=MyStack()
        temp.push(2)
        self.assertEqual(temp._array[0], 2)
        self.assertEqual(temp.pop(), 2)
        self.assertEqual(temp.pop(), None)
        temp=MyStack()
        temp.push(2)
        self.assertEqual(temp.pop(), 2)
        temp.push(3)
        self.assertEqual(temp.pop(), 3)
        temp.push(4)
        self.assertEqual(temp.pop(), 4)
        temp.push(5)
        self.assertEqual(temp.pop(), 5)
        self.assertEqual(temp._capacity, 2)

        temp=MyStack()
        temp.push(2)
        temp.push(3)
        temp.push(4)
        temp.push(5)
        self.assertEqual(temp._capacity, 4)
        self.assertEqual(temp.pop(), 5)
        self.assertEqual(temp.pop(), 4)
        self.assertEqual(temp.pop(), 3)
        temp.push(100)
        self.assertEqual(temp.pop(), 100)





    def test_top(self):
        temp=MyStack()
        temp.push(2)
        self.assertEqual(temp.top(), 2)


if __name__ == "__main__":
    unittest.main()