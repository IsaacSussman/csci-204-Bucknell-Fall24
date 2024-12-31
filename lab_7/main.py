from random import randint
from math import log
from typing import Callable
from Int import Int, Counter
from Array import Array
from matplotlib import pyplot as plt
from SortingAlgorithms import selection_sort, insertion_sort

# TODO: Write your name(s) in the attribute below
yournames="Student A's name & Student B's name"

def test_algorithm(alg: Callable) -> None:
    # unsorted array of integers
    arr1 = Array(10)
    arr1[0] = Int(2); arr1[1] = Int(6); arr1[2] = Int(1); arr1[3] = Int(9); arr1[4] = Int(4)
    arr1[5] = Int(0); arr1[6] = Int(3); arr1[7] = Int(5); arr1[8] = Int(7); arr1[9] = Int(8)
    # sorted array of integers
    arr2 = Array(10)
    for i in range(10):
        arr2[i] = Int(i)
    # test insertion sort algorithms
    print("Look and see that both arrays become 0..9 in sorted order.")
    print(alg(arr1))
    print(alg(arr2))

def analyze_runtime(alg: Callable, plot_name: str, show_plot:bool = True) -> None:
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
            mylist += [Int(val) for val in [randint(2, 20000)]]
        Int.CURRENT_COUNTER.zero()
        alg(mylist)
        rand_comparisons += [Int.CURRENT_COUNTER.get_value()]
    print("\nO() comparisons for random arrays")
    print("n".ljust(sp) + "Yours".ljust(sp) + "n^2".ljust(sp) + "(n-1)^2".ljust(sp) + "n(n-1)/2".ljust(sp))
    for i in range(len(sizes)):
        print(str(sizes[i]).ljust(sp) + str(rand_comparisons[i]).ljust(sp) + str(sizes[i]**2).ljust(sp) + str((sizes[i] - 1)**2).ljust(sp) + str(sizes[i] * (sizes[i] - 1) // 2).ljust(sp))
    
    # create and sort already sorted array of size 2^3 ...
    sorted_comparisons = []
    for size in sizes:
        mylist = [Int(val) for val in list(range(0, size))]  # a list of numbers 0..size-1
        Int.CURRENT_COUNTER.zero()
        alg(mylist)
        sorted_comparisons += [Int.CURRENT_COUNTER.get_value()]
    print("\nO() comparisons for sorted arrays")
    print("n".ljust(sp) + "Yours".ljust(sp) + "n^2".ljust(sp) + "(n-1)^2".ljust(sp) + "n(n-1)/2".ljust(sp))
    for i in range(len(sizes)):
        print(str(sizes[i]).ljust(sp) + str(sorted_comparisons[i]).ljust(sp) + str(sizes[i]**2).ljust(sp) + str((sizes[i] - 1)**2).ljust(sp) + str(sizes[i] * (sizes[i] - 1) // 2).ljust(sp))

    # create and sort already reversed array of size 2^3 ...
    reversed_comparisons = []
    for size in sizes:
        mylist = [Int(val) for val in list(range(size-1, -1, -1))]  # a list of numbers size-1..0
        Int.CURRENT_COUNTER.zero()
        alg(mylist)
        reversed_comparisons += [Int.CURRENT_COUNTER.get_value()]
    print("\nO() comparisons for reversed arrays")
    print("n".ljust(sp) + "Yours".ljust(sp) + "n^2".ljust(sp) + "(n-1)^2".ljust(sp) + "n(n-1)/2".ljust(sp))
    for i in range(len(sizes)):
        print(str(sizes[i]).ljust(sp) + str(reversed_comparisons[i]).ljust(sp) + str(sizes[i]**2).ljust(sp) + str((sizes[i] - 1)**2).ljust(sp) + str(sizes[i] * (sizes[i] - 1) // 2).ljust(sp))

    if show_plot:
        # plot graphs
        n_sqd = []
        for x in sizes[:7]:
            n_sqd += [x**2]
        n_lg_n = []
        for x in sizes:
            n_lg_n += [x * log(x,2)]
        plt.plot(sizes[:7], n_sqd, '--', label="O(n^2)")
        plt.plot(sizes, n_lg_n, '--', label="O(n log n)")
        plt.plot(sizes, reversed_comparisons, 'o', label="reversed")
        plt.plot(sizes, rand_comparisons, label="random")
        plt.plot(sizes, sorted_comparisons, ':', label="sorted")
        print("Save the resulting plot as " + plot_name)
        plt.xlabel("n") # naming the x axis
        plt.ylabel("Number of comparisons") # naming the y axis
        title = "Unknown"
        if "s_sort" in plot_name: title = "Selection Sort"
        elif "i_sort" in plot_name: title = "Insertion Sort"
        plt.title(title + " by " + yournames) # giving a title to my graph
        plt.legend() # show a legend
        plt.show() # function to show the plot

if __name__ == "__main__": # this line is to avoid running main() in case main.py is imported.
    run_mode = input(
"""
Enter one of the numbers to the left to execute the command on the right.
0: test selection sort
1: test insertion sort
2: analyze selection sort
3: analyze insertion sort
Enter a number below:
"""
    )
    if run_mode[0] == '0': test_algorithm(selection_sort)
    elif run_mode[0] == '1': test_algorithm(insertion_sort)
    elif run_mode[0] == '2': analyze_runtime(selection_sort, "s_sort.jpg")
    elif run_mode[0] == '3': analyze_runtime(insertion_sort, "i_sort.jpg")
    else : print("\nDid not recognize command.\n")
            
        