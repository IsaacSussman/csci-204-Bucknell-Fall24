class Array:
    """ Basic array functionality
    len() returns the allocated capacity of the array (>= len)
    _capacity : capacity allocated instance field
    __getitem__ puts a value at an index or throws an Index.. exception
        Use like x = array[3]
    __setitem__ returns the value at an index or throws an Index.. exception
        Use like array[3] = 12
    Indices are 0..cap-1 (no negative indices)

    Do we want to constrain the content type???
    """
    def __init__(self, cap=10, item_type=int): 
        """
        Initialize a new array of items of a fixed type size cap. 
        - To set a size, use cap = integer. Defaults to 10.
        - To set an item type use item_type = desired type. Defaults to int.
        """
        self._capacity = cap
        self._list = [None]*cap
        self._type = item_type

    def __len__(self):
        """
        Returns the capacity of the array in O(1) time, where n is the cap.
        """
        pass

    def __getitem__(self, index):
        """
        Returns the value of an item at a given index. Raises an IndexError if the index is out of bounds.
        """
        pass

    def __setitem__(self, index, value):
        """
        Sets the value at a given index. 
        - Raises an IndexError if the index is out of bounds.
        - Raises a ValueError if the item is neither the given type nor None.
        """
        pass

    def get_type(self) :
        """
        Returns the type of items in the array.
        """
        pass

    def __str__(self):
        s = "["
        for item in self._list:
            s += str(item) + ","
        s = s[:-1] # remove last unwanted comma
        s += "]"
        return s

# Functions (Not Methods)
def add_first(array, letter) :
    """
    Scoots the letters in the array over to the right one space and puts the given letter at the 0th index. Note that this removes the last entry.
    - Raises an exception if the array is empty.
    """
    pass

def pointwise_sum(array1, array2) :
    """
    Returns the pointwise sum of two arrays of ints of the same length.
    - Raises an Exception if the arrays are not the same length.
    """
    pass

def extend(array) :
    """
    Returns an array that is twice the size of the input array and begins with a copy of the input array.
    """
    pass

def rotate(array) :
    """
    Rotates the items in an array.
    """
    pass