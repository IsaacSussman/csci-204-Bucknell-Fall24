"""
In-Class Exercise 4: Algorithm Analysis 1 (The Knapsack Problem)
Date: September 2, 2024

* Make sure you submit this file as "day_3_knapsack.py"

----------------------------------------------------------
Authors:
-
- 
----------------------------------------------------------

End Product: Program that implements the greedy and exhaustive knapsack algorithms. 
"""

def greedy_knapsack_algorithm(W, snack_weights:list):
    knapsack = [0]
    while sum(knapsack) != W and len(snack_weights) != 0:
        for i in range()
    return False


# Below is the exhaustive knapsack algorithm (using some help from a Python textbook)
def exhaustive_knapsack_algorithm(W, snack_weights) :
    # Compute the list of all combinations
    combinations = gen_power_set(snack_weights)
    
    # Test each combination
    for combination in combinations :
        if sum(combination) == W :
            return True
        
    return False

"""
The following two functions come from the ebook "Introduction to Computation and Programming Using Python", by John V. Guttag
"""
def get_binary_rep(n, num_digits) :
    result = ""
    while n > 0 :
        result = str(n%2) + result
        n = n//2
    if len(result) <= num_digits :
        for i in range(num_digits - len(result)) :
            result = "0" + result
    
    return result

def gen_power_set(items):
    powerset = []
    
    for i in range(2 ** len(items)) :
        bin_str = get_binary_rep(i, len(items))
        subset = []
    
        for j in range(len(items)):
            if bin_str[j] == "1" :
                subset.append(items[j])
        powerset.append(subset)
            
    return powerset
""""""

print(exhaustive_knapsack_algorithm(7   , [3, 5]))