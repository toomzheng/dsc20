def problem_1(int_lst, mult_factor):
    """
    Multiply each element in a list by `mult_factor`
    ---
    Parameters:
        int_lst: a list of integers 
        mult_factor: an integer
    ---
    Returns:
        a new list where each element in the original list is 
        multiplied by mult_factor

    >>> problem_1([1, 3, 5], 3)
    [3, 9, 15]
    >>> problem_1([1, 3, 5], 0)
    [0, 0, 0]
    >>> problem_1([], -10)
    []
    """
    f=lambda x: x*mult_factor
    return f(int_lst)