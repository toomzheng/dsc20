# Question 1
def randomize(*args):
    """ 
    Organizes a series of arguments into a dictionary with keys being the type
    of the argument and values determined by specific transformation rules
    to each type. 

    If the type is a:
        string: keep the characters at the even indices of the string, 
        i.e. (0th, 2nd, 4th, 6th index and so on…)
        int: if even cast to True, if odd cast to False.
        float: if negative, convert to equivalent positive value, if 
        non-negative, change it into int by cutting off everything after 
        the decimal.
        list: use its length as a value for a corresponding dictionary list.
        Anything else: key is 'garbage', and use unchanged arguments as values
        for a corresponding dictionary list.

    Args:
        *args: A variable-length argument list containing elements of various
        types.

    Returns:
        dict: A dictionary where keys are data types and values are 
        lists of transformed items done according to the rules

    >>> randomize(1, 2.3, False, 'DSC20')
    {'int': [False], 'float': [2], 'garbage': [False], 'str': ['DC0']}
    >>> randomize(True, 4, 'ABC', -9.8, [1,2,3], 'a', False)
    {'garbage': [True, False], 'int': [True], 'str': ['AC', 'a']\
, 'float': [9.8], 'list': [3]}
    >>> randomize(False, True, 'DS', True, 'abc', -3.2, 5, {'a': 1}, -2, ' .')
    {'garbage': [False, True, True, {'a': 1}], 'str': ['D', 'ac', ' ']\
, 'float': [3.2], 'int': [False, True]}
    >>> randomize()
    {}
    >>> randomize(True)
    {'garbage': [True]}

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> randomize(0, -10, '', 3.14159, [0])
    {'int': [True, True], 'str': [''], 'float': [3], 'list': [1]}

    >>> randomize({'key': 'value'}, [1, 2], 'longstring', 17.89, -4)
    {'garbage': [{'key': 'value'}], 'list': [2], 'str': ['lnsrn'], \
'float': [17], 'int': [True]}

    >>> randomize(" ", 42, None, -3.14, [1, 2, 3, 4])
    {'str': [' '], 'int': [True], 'garbage': [None], 'float': [3.14], \
'list': [4]}
    """
    # base case -- if no input, return the result
    if not args:
        return {}

    else:
        # initialize last_arg variable - we will be doing recursion beginning
        # from the last element
        last_arg = args[-1]
        # handle each type
        # ADD A CHECK FOR BOOLS AS THEY ARE CONSIDERED INTS
        if isinstance(last_arg, bool):
            key = "garbage"
            val = last_arg
        elif isinstance(last_arg, int):
            key = "int"
            val = last_arg % 2 == 0
        elif isinstance(last_arg, float):
            key = "float"
            val = abs(last_arg) if last_arg < 0 else int(last_arg)
        elif isinstance(last_arg, str):
            key = "str"
            val = "".join(last_arg[i] for i in range(0, len(last_arg), 2))
        elif isinstance(last_arg, list):
            key = "list"
            val = len(last_arg)
        else:
            key = "garbage"
            val = last_arg

        # assign the recursion to a variable so we can use it in a dict later
        # we are operating backwards on the entire recursion, so we remove
        # from the end
        rest_dict = randomize(*args[:-1])

        # add current arg to result
        if key in rest_dict:
            # we add the rest_dict[key] value before as we are operating back
            rest_dict[key] = rest_dict[key] + [val]
        else:
            rest_dict[key] = [val]
        return rest_dict
