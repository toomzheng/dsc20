# Question 4
def swap_lists(alist1, alist2):
    """
    Swaps all the elements between two lists in place.

    Args:
        alist1 (list): first list to be swapped
        alist2 (list): second list to be swapped

    Returns:
        None: this function modifies both lists in place

    >>> list1 = [1, 2]
    >>> list2 = [3, 4]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [3, 4]
    >>> print(list2)
    [1, 2]

    >>> list1 = [4, 2, 6, 8, 90, 45]
    >>> list2 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 41, 65, 43, 4, 17]
    >>> print(list2)
    [4, 2, 6, 8, 90, 45]

    # Add at least 3 doctests below here #
    >>> list1 = []  
    >>> list2 = []
    >>> swap_lists(list1, list2)
    >>> print(list1)
    []
    >>> print(list2)
    []

    >>> list1 = ["a", True, None, 3.14]  
    >>> list2 = [[], {}, (), 42]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [[], {}, (), 42]
    >>> print(list2)
    ['a', True, None, 3.14]

    >>> list1 = [1, 1, 1] 
    >>> list2 = [1, 1, 1]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [1, 1, 1]
    >>> print(list2)
    [1, 1, 1]
    """
    i = 0
    for i in range(len(alist1)):
        alist1[i], alist2[i] = alist2[i], alist1[i]
        i+=1