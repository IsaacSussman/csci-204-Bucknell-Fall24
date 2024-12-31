from Array import Array

class MyQueue:
  """Queue ADT implemented using an Array (options for bounded and unbounded).
  
  Attibutes:
  # Todo, fill in docstrings
  """

  def __init__( self, bound = None ):
    """ Queue starts out empty. If bound == None, the queue
    is unbounded. Otherwise set the capacity of the queue
    to be the integer value of bound. """
    self._array = Array(2)
    self._bound = bound
    if bound:
      self._array = Array(bound)
    self._size = 0
    self._front = 0
    self._back = 0
    

  def __len__( self ):
    """ Return the current size of the queue. """
    return self._size

  def is_empty(self):
    """ Returns true if the queue is empty, false otherwise. """
    return self._size == 0

  def _expand(self):
    """ If full and unbounded, expand the array capacity. """
    temp = self._array
    self._array = Array(len(temp)*2)
    for i in range(self._size):
      self._array[i] = temp[(i+self._front)%len(temp)]
    self._front = 0
    self._back = self._size-1 
    

  def enqueue(self, obj):
    """ If full and bounded, return -1 to indicate failure. """
    
    if len(self._array) == self._size and self._bound: #bound
      return -1
    if len(self._array) == self._size:
      self._expand()
    if self.is_empty():
      self._array[self._back] = obj
    elif not self._bound:
      
      self._back=(self._back+1)%len(self._array)
      self._array[self._back] = obj
    
    self._size+=1

    

  def dequeue(self):
    """ DeQ and return object. If empty, return None. """
    v = self._array[self._front]
    v = None if self.is_empty() else v
    self._front = (self._front + 1) % len(self._array) if v and self._size > 1 else self._front
    self._size-=0 if v is None else 1
    return v

  def front(self):
    """ Return the object that would be dequeue'd next.
        If empty, return None. """
    return self._array[self._front] if not self.is_empty() else None
  
  def __str__(self) -> str:
    """returns a string of the form front a b c back

    Returns:
        str: string representing queue
    """
    if self.is_empty():
      return ""
    s = "front "
    for i in range(self._front, self._front+self._size):
      s+= str(self._array[i%len(self._array)]) + " "
    s+="back"
    return s