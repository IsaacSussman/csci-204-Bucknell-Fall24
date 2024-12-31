from typing import Callable
from matplotlib import pyplot as plt
from random import randint
from math import log

import Counter as counter

from SortingAlgorithms import merge_sort
from Array import Array

# TODO: Write your name(s) in the attribute below
yournames="Student A's name & Student B's name"

# Test algorithm
def test_algorithm(alg : Callable) -> None:
    # unsorted array of integers
    arr1 = Array(10)
    arr1[0] = 2; arr1[1] = 6; arr1[2] = 1; arr1[3] = 9; arr1[4] = 4
    arr1[5] = 0; arr1[6] = 3; arr1[7] = 5; arr1[8] = 7; arr1[9] = 8

    # sorted array of integers
    arr2 = Array(10)
    for i in range(10):
        arr2[i] = i

    # test insertion sort algorithms
    print("Look and see that both arrays become 0..9 in sorted order.")
    alg(arr1)
    print(arr1)
    alg(arr2)
    print(arr2)

def analyze_runtime(alg: Callable, plot_name : str, show_plot : bool = True) -> None :

    # get a list of sizes 2^3 .. 2^14
    sp = 11 # control the display spaces
    sizes = []
    for x in range(3, 10):
        sizes += [2**x]  # compute 2^x
    
    # create and sort random arrays of size 2^3 ...
    rand_comparisons = []
    for size in sizes:
        mylist = []
        for y in range(size):
            # a random int between 2 and 20000 inclusive
            mylist += [val for val in [randint(2, 20000)]]


        counter.reset_count()
        alg(mylist)
        rand_comparisons += [counter.get_value()]

    print("\nO() comparisons for random arrays")
    print(
        "n".ljust(sp) 
        + "Yours".ljust(sp) 
        + "n^2".ljust(sp) 
        + "(n-1)^2".ljust(sp) 
        + "n(n-1)/2".ljust(sp) 
        + "n log n".ljust(sp)
    )
    
    for i in range(len(sizes)):
        print(
            str(sizes[i]).ljust(sp) 
            + str(rand_comparisons[i]).ljust(sp) 
            + str(sizes[i]**2).ljust(sp) 
            + str((sizes[i] - 1)**2).ljust(sp) 
            + str(sizes[i] * (sizes[i] - 1) // 2).ljust(sp) 
            + str(sizes[i] * log(sizes[i], 2)).ljust(sp)
        )
    
    # create and sort already sorted array of size 2^3 ...
    sorted_comparisons = []
    for size in sizes:
        mylist = [val for val in list(range(0, size))]  # a list of numbers 0..size-1

        counter.reset_count()
        alg(mylist)
        sorted_comparisons += [counter.get_value()]

    print("\nO() comparisons for sorted arrays")
    print(
        "n".ljust(sp) 
        + "Yours".ljust(sp) 
        + "n^2".ljust(sp) 
        + "(n-1)^2".ljust(sp) 
        + "n(n-1)/2".ljust(sp) 
        + "n log n".ljust(sp)
    )
    
    for i in range(len(sizes)):
        print(
            str(sizes[i]).ljust(sp) 
            + str(sorted_comparisons[i]).ljust(sp) 
            + str(sizes[i]**2).ljust(sp) 
            + str((sizes[i] - 1)**2).ljust(sp) 
            + str(sizes[i] * (sizes[i] - 1) // 2).ljust(sp) 
            + str(sizes[i] * log(sizes[i], 2)).ljust(sp)
        )

    # create and sort already reversed array of size 2^3 ...
    reversed_comparisons = []
    for size in sizes:
        mylist = [val for val in list(range(size-1, -1, -1))]  # a list of numbers size-1..0
        
        counter.reset_count()
        alg(mylist)
        reversed_comparisons += [counter.get_value()]

    print("\nO() comparisons for reversed arrays")
    print(
        "n".ljust(sp) 
        + "Yours".ljust(sp) 
        + "n^2".ljust(sp) 
        + "(n-1)^2".ljust(sp) 
        + "n(n-1)/2".ljust(sp) 
        + "n log n".ljust(sp)
    )
    
    for i in range(len(sizes)):
        print(
            str(sizes[i]).ljust(sp) 
            + str(reversed_comparisons[i]).ljust(sp) 
            + str(sizes[i]**2).ljust(sp) 
            + str((sizes[i] - 1)**2).ljust(sp) 
            + str(sizes[i] * (sizes[i] - 1) // 2).ljust(sp) 
            + str(sizes[i] * log(sizes[i], 2)).ljust(sp)
        )

    if show_plot:
        # plot graphs
        n_sqd = []
        target = 6 if "q_sort" in plot_name else 4
        for x in sizes[:target]:
            n_sqd += [x**2]

        n_lg_n = []
        for x in sizes:
            n_lg_n += [x * log(x,2)]

        plt.plot(sizes[:target], n_sqd, '--', label="O(n^2)")
        plt.plot(sizes, n_lg_n, '--', label="O(n log n)")
        plt.plot(sizes, reversed_comparisons, 'o', label="reversed")
        plt.plot(sizes, rand_comparisons, label="random")
        plt.plot(sizes, sorted_comparisons, ':', label="sorted")
        print("Save the resulting plot as " + plot_name)
        plt.xlabel("n") # naming the x axis
        plt.ylabel("Number of comparisons") # naming the y axis
        title = "Unknown"
        if "m_sort" in plot_name: title = "Merge Sort"
        elif "q_sort" in plot_name: title = "Quick Sort"
        elif "i_sort" in plot_name: title = "Improved Quick Sort"
        plt.title(title + " by " + yournames) # giving a title to my graph
        plt.legend() # show a legend
        plt.show() # function to show the plot

if __name__ == "__main__": # this line is to avoid running main() in case main.py is imported.
    inp = input("Enter 0 to test merge sort or 1 to analyze the runtime of merge sort/\n")  

    if inp == '0':
        test_algorithm(merge_sort)

    elif inp == '1':
        analyze_runtime(merge_sort, "m_sort.jpg")

    else:
        print("Invalid input.  Be sure there are no spaces/quote marks/etc, and just enter a 0 or 1.  Rerun and try again.")