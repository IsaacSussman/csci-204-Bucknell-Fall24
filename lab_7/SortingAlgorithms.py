from Array import Array

""" Task 1: Implement Selection Sort """
def selection_sort(in_arr: Array) -> Array:
    """! Perform selection sort to sort the input array of integers.
    
    Repeatedly
      Select the smallest thing in the unsorted section by
        Set temp = first unsorted thing
        repeat from the left to right of the unsorted section
          if stuff < temp
            Set temp = stuff
      Set/append temp to the sorted section
    Until everything is sorted
                 
    Remark: You can avoid using `temp` if you do swapping.
                 
    Note: If you implement an in-place version, simply return in_arr. Otherwise, return your resulting array.
    """
    temp = None
    for i in range(len(in_arr)):
      temp
    return in_arr
        

""" Task 2: Implement Insertion Sort """
def insertion_sort(in_arr: Array) -> Array:
    """! Perform insertion sort to sort the input array of integers.
    
    Repeatedly
      Set temp = first unsorted thing
      Insert it into place in the sorted section by
        repeat from right to left of the sorted section
          if temp <= stuff
              move stuff to the right one spot
          else 
              put temp in empty place
              break to get out of the loop
    Until everything is sorted
              
    Remark: You can avoid using `temp` if you do swapping.
              
    Note: If you implement an in-place version, simply return in_arr. Otherwise, return your resulting array.
    """
    return in_arr