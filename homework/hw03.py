"""
DSC 20 Winter 2024 Homework 03
Name: Tom Zheng
PID: A18424137
Source: GeeksforGeeks for dictionary comprehension, Claude 3.5 Sonnet for hints
on some problems (5.2, 6) though never gave direct answers
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
    Takes a list of non-empty strings and another list of non-empty positive
    integers of the same length. Returns a list of boolean values.

    Args:
        strings (list): list of non-empty strings
        numbers (list): list of positive ints

    Returns:
    list: list of boolean values. If the length of the string is longer than
    the corresponding number, return True. Else, put False in the list

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
    >>> string_lengths(["hello", "world"], [3, 6])
    [True, False]
    >>> string_lengths([], [])
    []
    >>> string_lengths(["hello", ""], [2, 3, 2])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(text, list)
    assert isinstance(nums, list)
    # when comparing for boolean, no need to use isinstance
    assert len(text) == len(nums)
    # checks if the string is a string and if it is non-empty
    assert all([isinstance(string, str) and string for string in text])
    # checks if the numbers in nums are integers and positive
    assert all([isinstance(number, int) and number > 0 for number in nums])
    return [len(text[i]) > nums[i] for i in range(len(text))]


# Question 1.3
def process_dict(input_dict):
    """
    Takes in a dictionary where keys are tuples and values are lists of strings
    Returns a list of the sum of the keys and strings for each key.

    Args:
        input_dict (dict): A dictionary with keys are tuples and values are
        lists.

    Returns:
        list: A list of ints where each integer is the sum for the length
        of the tuple (key) and the length of each of the strings in the
        list (values).


    >>> process_dict({1: ['a', 'b', 'c'], (1, 2): ['a']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['a', 0], (2, ): ['b']})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> process_dict({(1, 2): ['dsc', 'dsc20', 'dsc30'], (2,): ['b']})
    [15, 2]
    >>> process_dict({})
    []
    >>> process_dict({(1, 2): [], (3, 4): []})
    [2, 2]
    >>> process_dict({(1,): ['abcd'], (2, 3): ['ef', 'ghi']})
    [5, 7]
    """
    assert isinstance(input_dict, dict)
    # check if all the keys are tuples
    assert all([isinstance(key, tuple) for key in input_dict])
    # check if all the values are lists
    assert all([isinstance(input_dict[key], list) for key in input_dict])
    # check if all the items in the lists are strings
    assert all(
        [
            isinstance(input_dict[key][i], str)
            for key in input_dict
            for i in range(len(input_dict[key]))
        ]
    )

    # add the length of the key and
    # the sum of the lengths of strings in the list for the key
    # for each key in the dictionary
    return [
        len(key) + sum(len(string) for string in input_dict[key])\
            for key in input_dict
    ]


# Question 2
def unusual_sort(indices, items):
    """
    Sorts the list 'items' based on the order defined in indices. Outputs a 
    duple displaying what was shifted and from here
    
    Args:
        indices (list): A list of ints from 0 to n-1
        items (list): A list of elements to be sorted
    
    Returns:
        list: A list of tuples in the format (element, original index, \
            new index). Where the new index is the item's corresponding index
            in the indices list.

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
    
    >>> unusual_sort([], [])
    []
    
    >>> unusual_sort([3, 0, 1, 'two'], ["X", "Y", "Z", "W"])
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> unusual_sort([5, 0, 1], ["alpha", "beta", "gamma"])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert len(indices) == len(items)
    assert all([isinstance(index, int) for index in indices])
    assert all([index in range(0, len(items)) for index in indices])
    # check that all integers are unique. set carries an unordered collection
    # of unique items, so if there are duplicates, the length must be diff
    assert len(indices) == len(set(indices))
    return [(items[indices[i]], indices[i], i) for i in range(len(indices))]


# Question 3
def change_input(strange_list):
    """
    Takes in a list of string and decodes it by applying these transformations:
    - Each digit (0-9) multiplied by two
    - Lowercase vowels (a, e, i, o, u) are converted to UPPERCASE
    - Everything else (lowercase, spaces, punctuations, etc.) stay at the \
        same position relative to each other.
    
    Args:
        strange_list (list): A list of strings to be transformed.
    
    Returns:
        list: A list of transformed strings.

    >>> change_input(["3.14IS PIE", "11My aGe iS"])
    ['6.28IS PIE', '22My AGE IS']
    >>> change_input(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO t12O slEEp At ', '10I lIkE tO stArt wOrk bEfOrE ']
    >>> change_input("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError
    >>> change_input([""])
    ['']
    >>> change_input(["123abc", "hello"])
    ['246Abc', 'hEllO']
    >>> change_input(["!@# $%^ &*()"])
    ['!@# $%^ &*()']
    """
    assert isinstance(strange_list, list)
    assert all([isinstance(item, str) for item in strange_list])
    return [''.join(str(int(char) * 2) if char.isdigit() \
        else char.upper() if char in 'aeiou' \
            else char for char in item) for item in strange_list]


# Question 4
def change_input_even_more(strange_list):
    """
    Takes in a list of string and decodes it by applying these transformations:
    - Each digit (0-9) is moved to the end of the string and multiplied by two
    - Lowercase vowels (a, e, i, o, u) are converted to UPPERCASE
    - Everything else (lowercase, spaces, punctuations, etc.) stay at the \
        same position relative to each other.
    
    Args:
        strange_list (list): A list of strings to be transformed.
    
    Returns:
        list: A list of transformed strings.

    >>> change_input_even_more(["3.14IS PIE", "11My aGe iS"])
    ['.IS PIE628', 'My AGE IS22']
    >>> change_input_even_more(["go t6o sleep at ", \
        "5i like to start work before "])
    ['gO tO slEEp At 12', 'I lIkE tO stArt wOrk bEfOrE 10']
    >>> change_input_even_more("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError

    >>> change_input_even_more([""])
    ['']
    >>> change_input_even_more(["123abc", "hello"])
    ['Abc246', 'hEllO']
    >>> change_input_even_more("11My aGe iS")
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(strange_list, list)
    assert all([isinstance(item, str) for item in strange_list])
    # this time, we can join all of the not isdigits first, then add on the 
    # digits after
    return [''.join(char.upper() if char in 'aeiou' \
        # make sure to not write out any digits
            else char if not char.isdigit() else ''
            for char in item) \
                # now, at the end of the string do the digits
                + ''.join(str(int(char) * 2) for char in item if char.isdigit())
                for item in strange_list
                ]


# Question 5.1
def cheapest_gas(gas_stations, mileage):
    """
    Finds the reachable gas brand with the lowest price in a dictionary of 
    gas stations
    
    Args:
        gas_stations (dict): A dict where keys are gas brand names and values
        are made up of lists of tuples (distance, price)
        mileage (int): the remaning mileage of the vehicle
    
    Returns:
        str: The brand name with the lowest price among reachable stations.

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.3), (10, 5.4)] \
    }
    >>> cheapest_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_gas(gas_stations, 20)
    'Shell'
    
    >>> gas_stations = { \
            'Shell': [(5, 6.0)], \
            'Chevron': [(10, 5.0)], \
            'Arco': [(5, 5.0)] \
        }
    >>> cheapest_gas(gas_stations, 5)
    'Arco'
    
    >>> gas_stations = { \
        'Shell': [(15, 5.5)], \
        'Chevron': [(10, 5.8), (15, 5.2)], \
        'Arco': [(20, 5.0)] \
    }
    >>> cheapest_gas(gas_stations, 15)
    'Chevron'
    
    >>> gas_stations = { \
        'Shell': [(0, 3.0)], \
        'Chevron': [(0, 2.0)], \
        'Arco': [(0, 1.0)] \
    }
    >>> cheapest_gas(gas_stations, 0)
    'Arco'
    """

    # find reachable stations, and corresponding prices
    # order it so that the price comes first, so we can directly use min()
    return min([(gas_stations[station][i][1],station) \
        for station in gas_stations for i in range(len(gas_stations[station]))\
            # get the name of the station from the min tuple
            if gas_stations[station][i][0] <= mileage])[1]


# Question 5.2
def cheapest_average_gas(gas_stations, mileage):
    """
    Finds gas station within reachable stations with the lowest average price
    
    Args:
        gas_stations (dict): A dict where keys are gas brand names and values
        are made up of lists of tuples (distance, price)
        mileage (int): the remaning mileage of the vehicle
    
    Returns:
        str: The brand name with the lowest average price among reachable 
        stations.

    >>> gas_stations = { \
        'Shell': [(20, 5.2), (30, 5.3), (50, 5.6), (80, 5.3)], \
        'Chevron': [(10, 5.8), (60, 5.7)], \
        'Arco': [(20, 5.1), (10, 5.4)] \
    }
    >>> cheapest_average_gas(gas_stations, 10)
    'Arco'
    >>> cheapest_average_gas(gas_stations, 20)
    'Shell'

    >>> gas_stations = { \
            'Shell': [(5, 6.0)], \
            'Chevron': [(10, 5.0)], \
            'Arco': [(5, 5.0)] \
        }
    >>> cheapest_average_gas(gas_stations, 5)
    'Arco'
    
    >>> gas_stations = { \
        'Shell': [(15, 5.5)], \
        'Chevron': [(10, 5.8), (15, 5.2)], \
        'Arco': [(20, 5.0)] \
    }
    >>> cheapest_average_gas(gas_stations, 15)
    'Chevron'
    
    >>> gas_stations = { \
        'Shell': [(0, 3.0)], \
        'Chevron': [(0, 2.0)], \
        'Arco': [(0, 1.0)] \
    }
    >>> cheapest_average_gas(gas_stations, 0)
    'Arco'
    """
    # to be less messy, we get both key and value from dictionary
    # get the average by taking the sum of the prices in the reachable stations for each station
    return min([(sum(price for distance, price in gas_stations[station] if distance <= mileage)
                 # add up the number of that particular station within reach and divide for avg
                /sum(1 for distance, price in gas_stations[station] if distance <= mileage), station)
                # check that there is at least one station that is reachable to avoid DivisionByZero
                for station in gas_stations if any(distance <= mileage for distance, price in gas_stations[station])])[1]


# Question 6
def new_orders(orders, action, dish_name, amount):
    """
    Updates lunch orders based on given action of either 'add' or 'remove'

    Args:
        orders (dict): a dict where keys are food items (strings) and values
        are quantities (ints)
        action (str): the operation to be performed
        dish_name (str): the food to update
        amount (int): the number of the food item to update (non negative)
        
    Returns:
        dict: A dictionary with updated amounts of food items
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

    >>> orders = {'pizza': 0, 'burger': 5}
    >>> new_orders(orders, 'add', 'pizza', 10)
    {'pizza': 10, 'burger': 5}
    
    >>> orders = {'pizza': 10, 'burger': 5}
    >>> new_orders(orders, 'add', 'salad', 3)
    Traceback (most recent call last):
    ...
    AssertionError
    
    >>> orders = {'pizza': 10, 'burger': 5}
    >>> new_orders(orders, 'remove', 'pizza', 0)
    {'pizza': 10, 'burger': 5}
    """
    # check that orders is a dictionary
    assert isinstance(orders, dict)
    # check that the order contains food keys and int values
    assert all([isinstance(key, str) and isinstance(value, int) \
        and value >= 0 for key, value in orders.items()])
    # check that ths action is appropriate
    assert action in ["add", "remove"]
    # check the dish name is string
    assert isinstance(dish_name, str)
    # check that amount is non negative
    assert isinstance(amount, int) and amount >= 0
    # ensure that the dish name already exists in orders
    assert dish_name in orders
    # return a dictionary
    return {
        # add amount of the action is to add
        key: (value + amount if key == dish_name and action == 'add' else\
            # otherwise remove the amount and ensure it stays 0 minimum
            max(0, value - amount) if key == dish_name and action == 'remove'\
            # otherwise if the dish name is not the key, don't change the value
            else value) for key in orders for value in [orders[key]]}
