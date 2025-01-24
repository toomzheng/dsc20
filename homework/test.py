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
    """
    assert isinstance(input_dict, dict)
    # check if all the keys are tuples
    assert all([isinstance(key, tuple) for key in input_dict])
    # check if all the values are lists
    assert all([isinstance(input_dict[key], list) for key in input_dict]) 
    # check if all the items in the lists are strings
    assert all([isinstance(input_dict[key][i], str) for key in input_dict \
                for i in range(len(input_dict[key]))])
    
    # add the length of the key and
    # the sum of the lengths of strings in the list for the key
    # for each key in the dictionary
    return [len(key) + sum(len(string) for string in input_dict[key]) \
            for key in input_dict]