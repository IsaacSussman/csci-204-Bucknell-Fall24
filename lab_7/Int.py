class Counter:
    """! The Counter class.
    
    Defines the counter class to count the key comparison
    """
    
    def __init__(self, init_val = 0) -> None:
        """! The counter class initializer.
        
        @param init_val The value used to initialize the counter value. Default is None.
        """
        
        ## The counter value
        self._val = init_val
        
    def increase(self) -> None:
        """! increase the counter value by one
        """
        self._val += 1
        
    def decrease(self) -> None:
        """! decrease the counter value by one
        """
        self._val -= 1
        
    def zero(self) -> None:
        """! set the counter value to zero
        """
        self._val = 0
        
    def get_value(self) -> int:
        """! return the counter value
        
        @return the counter value
        """
        return self._val

class Int:
    """! The Int class.
    
    Defines the integer class that advance the counter when compared
    """
    ## The current counter in use
    CURRENT_COUNTER = Counter()
    
    def __init__(self, val = 0) -> None:
        """! The integer class initializer.
        
        @param val The value used to initialize the value. Default is None.
        """
        self._val = int(val)
        
    def __str__(self) -> str:
        """! The integer class string method.
        
        @return the string representation of the integer
        """
        return str(self._val)
        
    def __gt__(self, rhs) -> bool:
        """! Greater than
        
        @return if self > rhs
        """
        Int.CURRENT_COUNTER.increase()
        return self._val > rhs._val
        
    def __lt__(self, rhs) -> bool:
        """! Less than
        
        @return if self < rhs
        """
        Int.CURRENT_COUNTER.increase()
        return self._val < rhs._val
        
    def __eq__(self, rhs) -> bool:
        """! Equal to
        
        @return if self == rhs
        """
        Int.CURRENT_COUNTER.increase()
        return self._val == rhs._val
        
    def __ge__(self, rhs) -> bool:
        """! Greater than or equal to
        
        @return if self >= rhs
        """
        Int.CURRENT_COUNTER.increase()
        return self._val >= rhs._val
        
    def __le__(self, rhs) -> bool:
        """! Less than or equal to 
        
        @return if self <= rhs
        """
        Int.CURRENT_COUNTER.increase()
        return self._val <= rhs._val
        
    def __ne__(self, rhs) -> bool:
        """! Not equal to
        
        @return if self != rhs
        """
        Int.CURRENT_COUNTER.increase()
        return self._val != rhs._val
        
    