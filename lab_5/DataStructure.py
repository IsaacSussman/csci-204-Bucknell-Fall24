from __future__ import annotations
from typing import Any

class Array:
    """! The DataStructure.Array class.
    
    Defines the basic array class.
    """
    
    def __init__(self, cap: int = 10, init_val = None) -> None:
        """! The array class initializer.
        
        @param cap The capacity of the array.
        
        @param init_val The value used to initialize the array. Default is None.
        """
        
        ## The capacity of the array
        self._cap = cap
        ## The array data, stored using a Pythong list
        self._data = [init_val for _ in range(self._cap)] 
        
    def __str__(self) -> str:
        """! A string representation of the array.
        
        @return A string that represents the array.
        """
        
        s = ''
        for elm in self._data:
            s += str(elm) + ", "
        return '[' + s.rstrip().rstrip(',') + ']'
        
    def __len__(self) -> int:
        """! The array length function.
        
        @return The length/capacity of the array.
        """
        return self._cap
        
    def _boundary_check(self, index: int) -> None:
        """! Check if an index is in bound, raise an error if not.
        
        @param index The input index.
        """
        
        if index < 0 or index > self._cap:
            raise IndexError
        
    def __getitem__(self, index: int) -> Any:
        """! Get the item stored at index in the array.
        
        @param index The input index.
        
        @return The item stored at index.
        """
        
        self._boundary_check(index)
        return self._data[index]
        
    def __setitem__(self, index: int, value: Any):
        """! Store the input value at index in the array.
        
        @param index The input index.
        
        @param value The input value.
        """
        
        self._boundary_check(index)
        self._data[index] = value
                
class ArrayList:
    """! 
    The Array List

    This class implements a list using array to store a sequence of objects
    """

    def __init__(self) -> None:
        """! ArrayList initializer

        This initializer should initialize an array (_array) to have a capacity of two and the list size (_size) to zero.
        """
        # TODO: implement this method
        self._array = Array(2)
        self._size = 0


    def __len__(self) -> int:
        """! ArrayList class length function
        
        This returns the current size of the list.

        @rtype: int
        @return: Returns a total number of objects in the sequence
        """
        return self._size

    def __str__(self) -> str:
        """! ArrayList class str function

        This returns a string representation of the list formatted as `[obj at list index 0, obj at list index 1, ..., obj at list index n]` for a list of size n.

        @rtype: str
        @return: Returns a serialized string that describes the objects in the deque
        """
        # TODO: implement this method
        if self._size == 0:
            return "[]"
        str = "["
        for i in range(self._size):
            if i!=0:
                str+=", "
            str+=f"{self._array[i]}"
        return str+"]"
            

    def _expand(self) -> None:
        """! ArrayList class _expand
          
        This expands the array by doubling its capacity. Same as the one of Stack/Queue/Deque
        """
        # TODO: implement this method
        temp = self._array._data.copy()
        self._array = Array(self._array._cap*2)
        for i in range(len(temp)):
            self._array[i] = temp[i]
        
  
    def insert(self, obj: Any, idx: int) -> None:
        """! ArrayList class insert
          
        This inserts the input obj at the position indexed idx into the list. If the input list index is smaller than 0 or bigger than the list size, it should raise an exception.

        @type obj: Any
        @param obj: an input object

        @type idx: int
        @param idx: the list index to insert the input object into
        """
        # TODO: implement this method
        if idx > len(self) or idx < 0:
            raise IndexError
        if idx == len(self):
            self._expand()
        if self._array[idx] != None:
            if self._size >= self._array._cap-1:
                self._expand()
            for i in range(self._size+1, idx, -1):
                self._array[i] = self._array[i-1]
        self._array[idx] = obj
        self._size+=1
    
    def delete(self, idx: int) -> Any:
        """! ArrayList class delete
          
        This deletes the object at the index idx of the list. If the input list index is out-of-bound, it should raise an exception.

        @type idx: int
        @param idx: the list index at which to remove the object from the list
        
        @rtype: Any
        @return: Returns the deleted object
        """
        # TODO: implement this method
        if idx >= len(self) or idx < 0:
            raise IndexError
        val = self._array[idx]
        for i in range(idx, self._array._cap-1):
                self._array[i] = self._array[i+1]
        self._array[self._array._cap-1] = None
        self._size-=1
        return val


    def peek(self, idx: int) -> Any:
        """! ArrayList class peek
          
        This returns the object at the input index. Follow the slide to use the right formulat to convert list index to array index and return the right object.

        @type idx: int
        @param idx: the list index in the list where the object should return

        @rtype: Any
        @return: Returns the object at the specified index
        """
        # TODO: implement this method
        return self._array[idx]

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
    
class LinkedList:
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

    def insert(self, obj: Any, idx: int) -> None:
        """! LinkedList class insert
          
        This inserts a new node that stores the input object at the input list index into the list. 
        If the input list index is smaller than 0 or bigger than the list size, it should raise an exception.

        @type obj: Any
        @param obj: an input object

        @type idx: int
        @param idx: the position to insert the input into
        """
        # TODO: implement this method
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


l = LinkedList()
l.insert("?",0)
l.insert("you",0)
l.insert("are",0)
l.insert("how",0)
l.insert("world",0)
l.insert("hello",0)
print(l.delete(len(l)-1))
print(l.delete(0))
print(l.delete(1))
print(l)
