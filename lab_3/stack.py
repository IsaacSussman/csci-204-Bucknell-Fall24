""" CSCI204 Stack lab
Last Modified by: Isaac Sussman and Ethan Zeh, September 2024
"""

from Array import Array

class MyStack:
  """ Implement this Stack ADT using an Array to hold elements.
  """

  def __init__(self):
    """ Initialize an empty stack.
    Initial capacity should be 2, size should be zero, all items in the array should be None. """
    self._capacity = 2
    self._size = 0
    self._array = Array(self._capacity)

  def is_empty( self ):
    """ Is the stack empty?
    Return:
      True if the stack is empty; False otherwise. """
    return self._size == 0

  def _expand(self):
    """ Stack is full, expand the capacity. """
    self._capacity *= 2
    temp = Array(self._capacity)
    for i in range(len(self._array)):
      temp[i] = self._array[i]
    self._array = temp

      
  def push( self, item ):
    """ Push the item onto the top of the stack. 
    Parameters:
      item; item to add to top of stack.
    Return: None."""
    if self._size == self._capacity:
      self._expand()
    self._array[self._size] = item
    self._size += 1

  def pop( self ):
    """ Pop the top item off the stack (i.e., remove from stack) and return it. 
    Parameters:
      self, instance of MyStack.
    Return:
      item; item at the top of the stack.
    """
    if self._size == 0:
      return None
    self._size-=1
    temp = self._array[self._size]
    return temp

  def top( self ):
    """ Return the top item on the stack (does not change the stack). 
    Parameters:
    self, instance of MyStack.
    Return:
    item; item at the top of the stack.
    """
    if self._size == 0:
      return None
    return self._array[self._size-1]

