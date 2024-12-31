from day_7_8_array import *

class ArrayStack :
    def __init__(self, capacity, type=int):
        self._top = 0
        self._items = Array(capacity, type)

    def push(self, item) :
        """Pushes an item onto the stack."""
        if not item:
            raise Exception("Can't enter None")
        elif self._top==self._items.__len__():
            raise Exception("Stack is full")
        self._items.__setitem__(self._top,item)
        self._top+=1
        return item

    def pop(self) :
        """Removes and returns the item on top of the stack."""
        if self._top==0:
            raise Exception("Stack is empty")
        self._top-=1
        temp=self._items.__getitem__(self._top)
        self._items.__setitem__(self._top, None)
        return temp

    def get_top(self) :
        """Returns the index of the height of the stack."""
        return self._top
    
    def expand(self) :
        """Doubles the capacity of the stack. Uses the expand(array) function from day_7_8array."""
        temp=Array(self._items.__len__()*2)
        for i in range(self._items.__len__()):
            temp.__setitem__(i,self._items.__getitem__(i))
        self._items=temp

def is_empty(stack) :
    """Returns True if the stack is empty, False otherwise."""
    if stack.get_top()!=0:
        return False
    test=True
    for i in range(stack._items.__len__()):
        if stack._items.__getitem__(i)!=None:
            test=False
    return test

def is_balanced(par_string) :
    """Takes in a string of parentheses. Returns True if the string is balanced, and False otherwise."""
    list=par_string.split(" ")
    stack=ArrayStack(len(list),str)
    for i in list:
        if i=="(":
            stack.push("(")
        else:
            try:
                stack.pop()
            except:
                return False
    if is_empty(stack):
        return True
    return False

# Bonus stuff
def recursive_sum(n) :
    """Mysterious function."""
    if n == 0 :
        return 0
    else : 
        return n + recursive_sum(n-1)

def collatz(n) :
    """Even more mysterious function."""
    if n == 1:
        return 1
    elif n % 2 == 0 :
        return collatz(n // 2)
    else :
        return collatz(3 * n + 1)

if __name__ == "__main__" :
    test=ArrayStack(10)
    print(test.push(7))
    print(test.pop())
    print(test.get_top())
    test.expand()
    print(is_empty(test))

    bad1="("
    bad2="( ( )"
    bad3=") ( ( ) ( )"
    bad4="( ) ( ) ( ) ( ( ) ( ( ) ( ) )"
    good1="( )"
    good2="( ( ) )"
    good3="( ) ( )"
    good4="( ) ( ) ( ) ( ( ) ) ( ( ) ( ) )"
    print(is_balanced(bad1))
    print(is_balanced(bad2))
    print(is_balanced(bad3))
    print(is_balanced(bad4))
    print(is_balanced(good1))
    print(is_balanced(good2))
    print(is_balanced(good3))
    print(is_balanced(good4))