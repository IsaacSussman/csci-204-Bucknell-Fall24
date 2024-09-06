# Test function 0: Sum
def self_sum(n) :
    """
    Add n to itself
    """
    return n + n

# Test function 1: Triangular Sum
def triangular_sum(n) :
    """
    Add up 1 + 2 + 3 + ... + n
    """
    sum_up = 0
    for i in range(1, n+1) :
        sum_up += i

    return sum_up

# Test function 2: The Parabolic Triangular Sum
def parabolic_sum(n) : 
    """
    Add up 1 + (1 + 2) + (1 + 2 + 3) + ... + (1 + 2 + 3 + ... + n)
    """
    sum_up = 0
    for i in range(1, n+1) :
        for j in range(1, i + 1) :
            sum_up += j

    return sum_up

# Test function 3: The Big Sum
def big_sum(n) :
    """
    Add up 1 + 2 + 4 + 8 + ... + 2^n
    """
    sum_up = 0
    for i in range(2 ** n) :
        sum_up += i
    
    return sum_up