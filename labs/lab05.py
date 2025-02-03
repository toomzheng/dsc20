"""
DSC 20 Winter 2025 Lab 05
Name: Tom Zheng
PID: A18424137
"""

# PRE-DEFINED FUNCTIONS
def identity(x):
    return x

def squared(x):
    return x**2

def cubed(x):
    return x**3

def root(x):
    return round(x ** 0.5, 2)

# Question 1
def vector_op(lst, func):
    """
    Applies function to each element in the list
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
    --
    Returns:
        List of transformed numbers

    >>> lst = [1, 2, 3]
    >>> vector_op(lst, squared)
    [1, 4, 9]
    >>> lst = [1, 2, 3, 5]
    >>> vector_op(lst, lambda x: -x)
    [-1, -2, -3, -5]
    >>> vector_op(lst, identity)
    [1, 2, 3, 5]
    >>> lst = [10, 20, 30]
    >>> vector_op(lst, cubed)
    [1000, 8000, 27000]
    """
    return [func(num) for num in lst]

# Question 2
def matrix_op(lsts, func):
    """
    Applies function to each element in the 2D list
    --
    Parameters:
        lsts: list of lists of numbers
        func: a function to be applied
    --
    Returns:
        List of lists of transformed numbers

    >>> lsts = [[1,2], [3,4]]
    >>> matrix_op(lsts, squared)
    [[1, 4], [9, 16]]
    >>> lsts = [[10, 20], [30, 40]]
    >>> matrix_op(lsts, lambda x: x / 10)
    [[1.0, 2.0], [3.0, 4.0]]
    >>> lsts = [[5,15], [25,35]]
    >>> matrix_op(lsts, identity)
    [[5, 15], [25, 35]]
    """
    return [vector_op(vector, func) for vector in lsts]

# Question 3
def hop_hop(lst, func):
    """
    Applies function to each element in list twice
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
    --
    Returns:
        List of transformed numbers

    >>> lst = [1,2,3]
    >>> hop_hop(lst, squared)
    [1, 16, 81]
    >>> lst = [5,6,7,8]
    >>> hop_hop(lst, lambda x:x+1)
    [7, 8, 9, 10]
    >>> lst = [10,20,30]
    >>> hop_hop(lst, cubed)
    [1000000000, 512000000000, 19683000000000]
    """
    # apply the function twice
    return [func(func(element)) for element in lst]

# Question 4
def hop_many(lst, func, iterations):
    """
    Applies function to each element in list specified number of times
    --
    Parameters:
        lst: list of numbers
        func: a function to be applied
        iterations: number of times to perform operation
    --
    Returns:
        List of transformed numbers

    >>> lst = [1,2,3]
    >>> hop_many(lst, squared, 2)
    [1, 16, 81]
    >>> hop_many(lst, squared, 3)
    [1, 256, 6561]
    >>> hop_many(lst, identity, 100)
    [1, 2, 3]
    >>> hop_many(lst, lambda x: x - 1, 4)
    [-3, -2, -1]
    """
    # set up a helper function that takes in a vector and # of iterations
    def apply_iterations(element, n):
        # do this for n amount of times
        for _ in range(n):
            # set the new vector to be the vector with function applied
            element = func(element)
        return element
    
    return [apply_iterations(element, iterations) for element in lst]

# Question 5
def grades_stats(input_lst, choice):
    """
    Calculates mean, median, or both stats for input list. `choice` is 
    1 for median, 2 for mean, and any other for both stats.
    --
    Parameters:
        input_lst: list of integers
        choice: positive integer representing each stat
    --
    Returns:
        Stats of the input list

    >>> lst = [3, 2, 1]
    >>> grades_stats(lst, 1)
    2
    >>> grades_stats(lst, 2)
    2.0
    >>> grades_stats(lst, 0)
    (2, 2.0)
    >>> lst = [1, 2, 4]
    >>> grades_stats(lst, 2)
    2.33
    >>> grades_stats(lst, -1)
    (2, 2.33)
    """
    def find_median(): # Calculate median
        if len(sorted_lst) % 2 != 0:
            return sorted_lst[len(sorted_lst)//2]
        else:
            return ((sorted_lst[len(sorted_lst)//2]\
                    + sorted_lst[len(sorted_lst)//2+1])/2)
        
    def find_mean(): # Calculate mean
        return round(sum(sorted_lst)/len(sorted_lst), 2)

    sorted_lst = sorted(input_lst)

    if choice == 1:
        return find_median()
    elif choice == 2:
        return find_mean()
    else:
        return find_median(), find_mean()

# Question 6
def calculate_final_price(original_price, category, season):
    """
    Calculates price of item after discount.
    --
    Parameters:
        original_price: number representing price of item
        category: string category of item that category discount is based on
        season: string season that seasonal discount is based on
    --
    Returns:
        The final price of item after applying potential discounts
    
    >>> calculate_final_price(120, 'electronics', 'Spring')
    108.0
    >>> calculate_final_price(45, 'clothing', 'Winter')
    30.6
    >>> calculate_final_price(100, 'appliance', 'Spring')
    100
    """
    
    def apply_category_discount(category, original_price):
        if category.lower() == 'electronics':
            return 0.9 * original_price
        elif category.lower() == 'clothing':
            return 0.8 * original_price
        elif category.lower() == 'home':
            return 0.95 * original_price
        else:
            return original_price
        
    def apply_seasonal_discount(season, price):
        if season.title() == 'Winter':
            return 0.85 * price
        elif season.title() == 'Spring':
            return price
        elif season.title() == 'Summer':
            return 0.9 * price
        elif season.title() == 'Fall':
            return 0.95 * price

    return round(
        apply_seasonal_discount(
            season, apply_category_discount(category, original_price)
            ),
            2)
