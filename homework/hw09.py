"""
DSC 20 Winter 2025 Homework 09
Name: Tom Zheng
PID: A18424137
Source: N/A
"""

# Question 1
def question_1():
    """
    1 if a method mutates an object 
	0 otherwise

	>>> answer = question_1()
	>>> len(answer) == 10
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer])
	False
    """
    return [0, 0, 0, 1, 1, 0, 0, 1, 0, 1]


# Question 2
def question_2():
    """
    1 if a method is in place
	0 otherwise

	>>> answer = question_2()
	>>> len(answer)==5
	True
	>>> any([True if (i!=0 and i!=1) else False for i in answer ])
	False
    """
    return [1, 1, 1, 0, 0]


# Question 3
def reverse_list(lst):
    """ 
    Reverses the elements of a list in-place. The original list is mutated 
    directly. This is done by swapping the elements from both ends until the 
    list is reversed.

    Args:
        lst (list): the list to be reversed. 

    Returns:
        None: the function modifies the list in place and does not return \
            anything.

    >>> x = [3, 2, 4, 5]
    >>> reverse_list(x)
    >>> x
    [5, 4, 2, 3]
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]

    # Add at least 3 doctests below here #
    >>> x = [1, 1, 1, 1]
    >>> reverse_list(x)
    >>> x
    [1, 1, 1, 1]

    >>> x = [1, 2, 2, 1]  
    >>> reverse_list(x)
    >>> x
    [1, 2, 2, 1]

    >>> x = [-1, 0, None, "string", [1,2]] 
    >>> reverse_list(x)
    >>> x
    [[1, 2], 'string', None, 0, -1]

    >>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    >>> reverse_list(x)
    >>> x
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    increment = 1
    if lst:
        left, right = 0, len(lst)-1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += increment
            right -= increment


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
    increment = 1
    for i in range(len(alist1)):
        alist1[i], alist2[i] = alist2[i], alist1[i]
        i += increment