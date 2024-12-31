from Array import Array
from copy import deepcopy
import Counter as counter
import random

""" 
Task 1: Implement Merge Sort
Task 2: Place a call to counter.implement() so that it counts all the key comparisons.

"""
def print_arrays(array, first_a, last_a, left, first_l, last_l, right, first_r, last_r):
      # last is exclusive
      s = ""
      for i in range(first_a, last_a):
            s += str(array[i]) + " "
      s += '\t'
      for i in range(first_l, last_l):
            s += str(left[i]) + " "
      s += '\t'
      for i in range(first_r, last_r):
            s += str(right[i]) + " "
      print(s)

def merge_sort(array: Array) -> Array:
      """! Perform merge sort to sort the input array of integers."""
      ### Implement the algorithm below
      # Feel free to add any helper functions as needed
      # Note that: array MUST BE sorted by the end of this function!
      """ PSEUDOCODE:
            if array length <= 1: return array
            else:
            middle = you calculate it
            # Warning: unlike Python lists, 
            # Array does not allow slicing.
            left array = copy array[0:middle]
            right array = copy array[middle+1:end]
            left array = mergesort(left array)
            right array = mergesort(right array)
            merge(array, left array, right array)
            return array
      """
      if len(array)<= 1:
            return array
      else:
            #mid = (len(array)-1)//2
            left = Array(len(array)//2)
            right = Array(len(array)-len(left))
            for i in range(len(left)):
                  left[i] = array[i]
            for i in range(len(right)):
                  right[i] = array[len(left)+i]

            left = merge_sort(left)
            right = merge_sort(right)

            array = merge(array, left, right)

            return array

def merge(array: Array, left: Array, right: Array):
      ### Implement the algorithm below
      # Feel free to add any helper functions as needed
      # Note that: array MUST CONTAIN the merged array! This function DOES NOT return anything.
      """ PSEUDOCODE:
            # overwrite array while merging
            li = ri = ai = 0
            while both lists have contents
                  if left[li] < right[ri]:
                        array[ai] = left[li]
                        li += 1
                  else:
                        array[ai] = right[ri]
                        ri += 1
                  ai += 1

            while left has contents
            array[ai] = left[li]
            li += 1
            ai += 1

            while right has contents
            array[ai] = right[ri]
            ri += 1
            ai += 1
      """
      li = 0
      ri = 0 
      ai = 0
      while li< len(left) and ri < len(right):
            counter.increment()
            if left[li] < right[ri]:
                  array[ai] = left[li]
                  li +=1
            else:
                  array[ai] = right[ri]
                  ri += 1
            ai+=1
            
      while li < len(left):
            array[ai] = left[li]
            li += 1
            ai += 1

      while ri < len(right):
            array[ai] = right[ri]
            ri += 1
            ai += 1
      return array



        
