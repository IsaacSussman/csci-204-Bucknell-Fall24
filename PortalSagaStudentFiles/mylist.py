from __future__ import annotations
from typing import Any

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
    
class MyList:
    """! The LinkedList class

    This class implements a list using nodes to store a sequence of objects
    """

    def __init__(self) -> None:
        """! LinkedList initializer

        This initializer should initialize the head node (`_head`) and the tail node (`_tail`) to `None` and the list size (`_size`) to zero.
        """
        # TODO: implement this method
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self) -> None:
        """! LinkedList class length function

        This returns the current size of the list.

        @rtype: int
        @return: Returns a total number of objects/nodes in the sequence
        """
        # TODO: implement this method
        return self._size

    def __str__(self) -> str:
        """! LinkedList class str function
        
        This returns a string representation of the list formatted as `[obj at list index 0, obj at list index 1, ..., obj at list index n]` for a list of size n.

        @rtype: str
        @return: Returns a serialized string that describes the list of objects
        """
        # TODO: implement this method
        s = "["
        c = self._head
        flag = True
        for i in range(self._size):
            if flag:
                flag = False
            else:
                s+=", "
            s+=str(c._data if c else c)
            c=c._next


        return s+"]"

    def insert(self, obj: Any, idx: int = None) -> None:
        """! LinkedList class insert
          
        This inserts a new node that stores the input object at the input list index into the list. 
        If the input list index is smaller than 0 or bigger than the list size, it should raise an exception.

        @type obj: Any
        @param obj: an input object

        @type idx: int
        @param idx: the position to insert the input into
        """
        # TODO: implement this method
        if idx == None:
            idx = len(self)
        if len(self) < idx or idx < 0:
            raise IndexError
        if not type(obj) is Node:
            obj = Node(obj)
        c = self._head
        if c:
            if idx == 0:
                obj._next = self._head
                self._head = obj
            elif idx == self._size:
                print("last")
                self._tail._next = obj
                self._tail = obj
            else:
                trailing = None
                for i in range(idx):
                    trailing = c
                    if c._next is None:
                        raise IndexError
                    c = c._next
                    obj._next = c
                    trailing._next = obj
        else:
            c = obj
            self._head = obj
            self._tail = obj
        self._size+=1

        


    def delete(self, idx: int) -> Any:
        """! LinkedList class delete
          
        This removes the node at the input list index from the list and return the object stored in the deleting node.
        If the input list index is out-of-bound, it should raise an exception.

        @type idx: int
        @param idx: the position at which to remove the node from the list
        
        @rtype: Any
        @return: Returns the object stored in the deleted node.
        """
        # TODO: implement this method
        if len(self) <= idx or idx < 0:
            raise IndexError
        n = self._head
        if idx == 0:
            val = self._head._data
            self._head = self._head._next
            self._size-=1
            return val
        for i in range(idx-1):
            n = n._next
        val = n._next
        n._next = val._next if val else None
        self._size-=1
        return val
    
    def remove(self, data: Any):
        n = self._head
        trailing = None
        while (not n is None) and n._data != data:
            trailing = n
            n = n._next
        if n and trailing:
            trailing._next = n._next
        self._size-=1
        


    def peek(self, idx: int) -> Any:
        """! LinkedList class peek
          
        This returns the object stored in the node at the input list index.
        If the input list index is out-of-bound, it should return `None` instead.

        @type idx: int
        @param idx: the position in the list where the object should return

        @rtype: Any
        @return: Returns the object stored in the node at the specified index
        """
        # TODO: implement this method
        if idx<0 or idx>=self._size:
            return None
        n = self._head
        for i in range(idx):
            n = n._next
        val = n._next
        return n._data
    
    def count(self, data : Any):
        return str(self).count(str(data))
    
    def find(self, data: Any):
        """The run time is O(n), because it's essentially just a single for loop. The run time should be O(n)."""
        n = self._head
        c=0
        while n:
            
            if n._data == data:
                return c
            n = n._next
            c+=1
        return -1