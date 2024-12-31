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

class LinkedStack:
    """! The LinkedList class

    This class implements a list using nodes to store a sequence of objects
    """

    def __init__(self) -> None:
        """! LinkedList initializer

        This initializer should initialize the head node (`_top`) and the tail node (`_tail`) to `None` and the list size (`_size`) to zero.
        """
        # TODO: implement this method
        self._top = None
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
        if self._top == None:
            return "empty stack"
        s = "top --> "
        c = self._top
        flag = True
        for i in range(self._size):
            if flag:
                flag = False
            else:
                s+=" "
            s+=str(c._data if c else c)
            c=c._next


        return s

    def push(self, obj: Any) -> None:
        """ O(1). The push method contains four assignments, a conditional (containing a single boolean expression), and a constructor that only contains assignment. These are all O(1) operations that are independent of input length, added because they are in sequence so 1 + 1 + ... + 1 thus in all (including the worst) cases the runtime complexity is constant, so O(1). """

        if not type(obj) is Node:
            obj = Node(obj)
        obj._next = self._top
        self._top = obj
            
        self._size+=1
        

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
        return None if not self._top else self._top._data

    def pop(self) -> Any:
        """! LinkedList class delete
          
        This removes the node at the input list index from the list and return the object stored in the deleting node.
        If the input list index is out-of-bound, it should raise an exception.

        @type idx: int
        @param idx: the position at which to remove the node from the list
        
        @rtype: Any
        @return: Returns the object stored in the deleted node.
        """
        if not self._top:
            return None
        val = self._top._data
        self._top = self._top._next
        self._size-=1
        return val