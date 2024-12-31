from __future__ import annotations
from typing import Any
from mylist import MyList

class Node:
    """! The DataStructure.Node class.
    
    This class implements a node that store an object and a link to the next node
    """
    
    def __init__(self, data: Any, next_node: Node = None) -> None:
        """! The node class initializer.
        
        @param data The input data to be stored in the node.
        
        @param next_node The next node that the current node is pointing to. Default is None.
        """
        ## The data that is stored in the node
        self._data = data
        ## The next node that the current node is pointing to
        self._next = next_node
    
    def __str__(self) -> str:
        return str(self._data+", "+str(self._next))

class LinkedQueue(MyList):
    def __str__(self) -> str:
        """! LinkedList class str function
        
        This returns a string representation of the list formatted as `[obj at list index 0, obj at list index 1, ..., obj at list index n]` for a list of size n.

        @rtype: str
        @return: Returns a serialized string that describes the list of objects
        """
        # TODO: implement this method
        s = "front --> "
        c = self._head
        flag = True
        for i in range(self._size):
            if flag:
                flag = False
            else:
                s+=" "
            s+=str(c._data if c else c)
            c=c._next


        return s+" <-- back"
    
    def enqueue(self, obj: Any) -> None:
        """O(1). Adding something at the head is always the same number of steps."""

        # TODO: implement this method
        if not type(obj) is Node:
            obj = Node(obj)
        c = self._head
        if c:
            if 0 == 0:
                obj._next = self._head
                self._head = obj
        else:
            c = obj
            self._head = obj
            self._tail = obj
        self._size+=1
    
    def dequeue(self):
        """O(n). To link the 2nd to last node to None, you need to iterate through once."""
        # TODO: implement this method
        if len(self) <= 0:
            raise IndexError
        n = self._head
        if len(self)-1 <= 0:
            val = self._head._data
            self._head = self._head._next
            self._size-=1
            return val
        for i in range(len(self)-2):
            n = n._next
        val = n._next
        n._next = val._next if val else None
        self._tail = n
        self._size-=1
        return val

    def peek(self) -> Any:
        """! LinkedList class peek
          
        This returns the object stored in the node at the input list index.
        If the input list index is out-of-bound, it should return `None` instead.

        @type idx: int
        @param idx: the position in the list where the object should return

        @rtype: Any
        @return: Returns the object stored in the node at the specified index
        """
        # TODO: implement this method
        if 0>=self._size:
            return None
        return self._tail._data