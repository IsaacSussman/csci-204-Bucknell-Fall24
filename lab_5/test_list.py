"""
This program tests various functionality of an array list
implemented in the arraylist.py.

Assume the student has completed the array list implementation.

Xiannong Meng
2019-11-14
"""

from DataStructure import *      # import the array list implementation

def test_constructor(mode):
    '''Test the list constructor. Create and return an empty list.'''

    my_list = ArrayList() if mode == 0 else LinkedList() # create a new list
    print('A new list is created, its length should be 0 (zero), it is --> ', len(my_list))
    return my_list


def test_insert( my_list ):
    '''Test the insert method that insert a new item into the list.
       Note that the list insert() method defined takes the form
       of insert(self, item, index), i.e., an index must be given.
       the method should handle the invalid index itself, not this
       test program.'''

    items = ['hello', 'how', 'are', 'you', '?'] # some data
    for i in range(len(items)):
      print("insert '" + items[i] + "' at ",i)
      my_list.insert(items[i], i)
      print(my_list)

    # test insertion at a particular location, other elements should shift
    my_list.insert('world', 1)  

    print('Length of the list should be 6, it is --> ',len(my_list))

    # print the list using the __str__() method
    print("The list content should be [hello, world, how, are, you, ?]")
    print("It is --> ", end = '')
    print(my_list)

    return my_list   # we return the list so other functions can use it.

def test_peek( my_list ):
    '''Test the peek() method on the given list.
       Assume my_list contains proper information and is generated
       by the test_insert() method.'''

    print("The items in the list should be [hello, world, how, are, you, ?], it is --> [", end = '')
    s = ""
    for i in range(len(my_list)):
      s += my_list.peek(i)
      if i < len(my_list)-1:
        s += ", "
    print(s.rstrip() + ']')


def test_delete(my_list):
    '''Test the delete() method. The delete() method takes an index
       as the parameter and removes the item at the index'''

    # delete at normal positions
    my_list.delete(0)
    my_list.delete(1)
    n = len(my_list)
    my_list.delete(n-1)
    
    # print the content of the list
    print("The items in the list should be [world, are, you], it is --> [", end = '')
    s = ""
    for i in range(len(my_list)):
      s += my_list.peek(i)
      if i < len(my_list)-1:
        s += ", "
    print(s.rstrip() + ']')

    return my_list

def test_exception( my_list ):
    '''Test various exceptions of the list'''

    # peek exception, testing non-existing index
    try:
        print('Peek at a non-existing location should raise an exception')
        print(my_list.peek(len(my_list) + 2))
    except Exception:
        print("Caught peek error at a wrong index.")
    except:
        print("Other errors not caught by Exception when peek.")

    # delete exception, testing -1
    try:
        print('Deleting at index -1, should cause exception')
        my_list.delete(-1)
    except Exception:
        print("Caught delete error at index -1")
    except:
        print("Other errors not caught by Exception when deleting")

    # delete exception, testing n
    n = len(my_list)   # get an updated list length
    try:
        print('Deleting at index n, should cause exception')
        my_list.delete(n + 2)
    except Exception:
        print("Caught delete error at index n")
    except:
        print("Other errors not caught by Exception when deleting")

def test_list(mode):
    '''Test various operations of the list ADT in array.'''
    print('--- Test the list constructor ---')
    my_list = test_constructor(mode)
    print('--- Passed constructor test ---\n')

    print('--- Test the insert() method ---')
    my_list = test_insert( my_list )
    print('--- Passed insert() test ---\n')

    print('--- Test the peek() method ---')
    test_peek( my_list )
    print('--- Passed peek() test ---\n')

    print('--- Test the delete() method ---')
    my_list = test_delete( my_list )
    print('--- Passed delete() test ---\n')

    print('--- Test the exceptions ---')
    test_exception( my_list )
    print('--- Passed exceptions test ---\n')

# run the tests
print("Array List")
test_list(0)
print("Linked List")
test_list(1)

    
