"""
DSC 20 Winter 2024 Homework 03
Name: Tom Zheng
PID: A18424137
Source: TODO
"""
# Question 1.1
def operate_nums(lst):
    """
    Takes in a list of integers and returns a new list of integers. The new
    list will have doubled all odd integers and tripled all even integers.

    Args:
        lst (list): A list of integers
    
    Returns:
        list: A list where odd integers are doubled and even integers are 
        tripled

    >>> operate_nums([1, 2, 3, 's'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3.1, -2, 0, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> operate_nums([2, 3, -2, 0, 5])
    [6, 6, -6, 0, 10]

    >>> operate_nums([])
    []

    >>> operate_nums([1, -3, -4, 7])
    [2, -6, -12, 14]

    >>> operate_nums(1)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # check if the list is a list
    assert isinstance(lst, list)
    # check that all of the numbers in the list are integers
    assert all([isinstance(num, int) for num in lst])
    return [num * 2 if num % 2 != 0 else num * 3 for num in lst]

# Question 1.2
def string_lengths(text, nums):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> string_lengths(['a', 'b', 'c'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['', 'abc'], [1, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['a', 'b'], [-1, 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> string_lengths(['abc', 'abcd', 'abcde'], [2, 5, 5])
    [True, False, False]
    """
    # YOUR CODE GOES HERE #
    return

# Question 1.3
def process_dict(input_dict):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    
    >>> process_dict({1: ['a', 'b', 'c'], (1, 2): ['a']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['a', 0], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['dsc', 'dsc20', 'dsc30'], (2,): \
    ['b']})
    [15, 2]
    """
    # YOUR CODE GOES HERE #
    return

# Question 2
def unusual_sort(indices, items):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> unusual_sort([0, 4, 2, 3, 1], \
        ["zero", "four", "two", "three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), \
('three', 3, 3), ('four', 1, 4)]

    >>> unusual_sort([0.0, 4.0, 2.0, 3.0, 1.0], \
    ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3, 0], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> unusual_sort([0, 4, 2, 3], \
        ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #
    return

# Question 3
def change_input(strange_list):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> change_input(["3.14IS PIE", "11My aGe iS"])
    ['6.28IS PIE', '22My AGE IS']
    >>> change_input(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO t12O slEEp At ', '10I lIkE tO stArt wOrk bEfOrE ']
    >>> change_input("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # YOUR CODE GOES HERE #
    return

# Question 4
def change_input_even_more(strange_list):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> change_input_even_more(["3.14IS PIE", "11My aGe iS"])
    ['.IS PIE628', 'My AGE IS22']
    >>> change_input_even_more(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO tO slEEp At 12', 'I lIkE tO stArt wOrk bEfOrE 10']
    >>> change_input_even_more("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return

# Question 5.1
def cheapest_gas(gas_stations, mileage):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.3), (10, 5.4)] \
    }
    >>> cheapest_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_gas(gas_stations, 20)
    'Shell'

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return

# Question 5.2
def cheapest_average_gas(gas_stations, mileage):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.1), (10, 5.4)] \
    }
    >>> cheapest_average_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_average_gas(gas_stations, 20)
    'Shell'

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return

# Question 6
def new_orders(orders, action, dish_name, amount):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> orders = {'pizza': 10, 'burger': 5}
    >>> new_orders(orders, 'add', 'pizza', 5)
    {'pizza': 15, 'burger': 5}

    >>> new_orders(orders, 'remove', 'burger', 3)
    {'pizza': 10, 'burger': 2}

    >>> new_orders(orders, 'remove', 'pizza', 15)
    {'pizza': 0, 'burger': 5}

    >>> new_orders([], 'remove', 'burger', 3)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return
