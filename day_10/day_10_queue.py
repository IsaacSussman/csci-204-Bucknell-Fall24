from day_7_8_array import Array
from day_9_stack import ArrayStack

# FOR FREE
class Queue :
    def __init__(self) -> None:
        self._items = []
        self._length = 0

    def dequeue(self) :
        """Remove and return first itm in queue."""
        if self._length > 0 :
            self._items = self._items[:self._length]
            self._length -= 1
        else :
            raise Exception("Queue Underflow")
        return self._items[self._length]
    
    def enqueue(self, item) :
        """Adds item to the front of the queue."""
        self._items = [item] + self._items
        self._length += 1

    def peek(self) :
        """Returns the first item in the queue without removing it."""
        if self._length > 0 :
            return self._items[self._length - 1]
        else :
            return None
    
    def get_length(self) :
        """Returns the length of the queue."""
        return self._length
    
    def __str__(self) -> str:
        """Converts queue to readable string."""
        string_rep = "--> "
        for i in range(self._length) :
            string_rep += str(self._items[i]) + " "
        string_rep += " -->"
        return string_rep
# -------------------------------
# -------------------------------

# Work Here V 
def queue_reverse(q: Queue) :
    """Reverses a given queue and returns the result."""
    s = ArrayStack(q.get_length(),type(q.peek()))
    for i in range(q.get_length()):
        s.push(q.dequeue())
    q2 = Queue()
    for i in range(len(s._items)):
        q2.enqueue(s.pop())
    return q2





# Bonus
class SlowQueue :
    def __init__(self, capacity=10) -> None:
        # Do not touch this
        self._queue_items = ArrayStack(capacity)
        self._helper_stack = ArrayStack(capacity)
        self._length = 0
        # ---
    
    def dequeue(self) :
        """Remove and return first item in queue."""
        i = self._queue_items.pop()
        self._length -= 1
        return i
    
    def enqueue(self, item) :
        """Adds item to the front of the queue."""
        for i in range(self._length):
            self._helper_stack.push(self._queue_items.pop())
        self._queue_items.push(item)
        for i in range(self._length):
            self._queue_items.push(self._helper_stack.pop())
        self._length+=1
        

    def peek(self) :
        """Returns the first item in the queue without removing it."""
        i = self._queue_items.pop()
        self._queue_items.push(i)
        return i
    
    def get_length(self) :
        """Returns the length of the queue."""
        return self._length
    
    def __str__(self) -> str:
        """Converts queue to readable string."""
        string_rep = "--> "
        for i in range(self._length) :
            string_rep += str(self._queue_items._items[i]) + " "
        string_rep += " -->"
        return string_rep

q = SlowQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
print(q.dequeue(), end=" -> ")
print(q.dequeue(), end=" -> ")
print(q.dequeue(), end=" -> ")
print(q.dequeue(), end=" -> ")
print(q.dequeue(), end="")