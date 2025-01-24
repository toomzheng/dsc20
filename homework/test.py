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