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