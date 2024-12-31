"""
The Counter module is a shared module between the main.py file and the SortingAlgorithms file.
It implements a counter, which simply starts at 0, and it can be incremented using the increment() method below.
You will implement merge_sort in your SortingAlgorithm.py file, and use the increment() method below to indicate to the analysis function in main.py that a comparison has been made.
"""

global COMPARISON_COUNTER
COMPARISON_COUNTER = 0

# Call this when a comparison is made
def increment() :
    """!
    Increments COMPARISON_COUNTER
    """
    global COMPARISON_COUNTER
    COMPARISON_COUNTER = COMPARISON_COUNTER + 1

def get_value() :
    """!
    Returns the value of COMPARISON_COUNTER.
    """
    return COMPARISON_COUNTER

def reset_count() :
    """!
    Resets the value of COMPARISON_COUNTER.
    """
    global COMPARISON_COUNTER
    COMPARISON_COUNTER = 0