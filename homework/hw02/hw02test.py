def valid_pairs(keys, values):
    """
    Take in two lists of keys and values for a dictionary. Validates if each 
    item in key is a possible dictionary key. 

    Parameters:
        keys (list): A list of potential dictionary keys.
        values (list): A list of corresponding values.

    Returns:
        key_value_pairs (list of tuple): A list of key-value pairs where keys 
        are valid dictionary keys. If a key is invalid, it is replaced with the
        tuple ('not valid',).

    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = [1, "fun", [2], (1,), {}]
    >>> values = [1, {}, (1,), "island", [2]]
    >>> valid_pairs(keys, values)
    [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), ('not valid',)]

    >>> keys =[]
    >>> values =[]
    >>> valid_pairs(keys, values)
    []

    # Add at least 3 doctests below here #
    >>> keys = ["valid", 42, True, (1, 2), [3, 4]]
    >>> values = [10, "answer", False, "tuple", "list"]
    >>> valid_pairs(keys, values)
    [('valid', 10), (42, 'answer'), (True, False), ((1, 2), 'tuple'), \
('not valid',)]

    >>> keys = ["key", None, {}, "another", (3.14,)]
    >>> values = ["value", "no value", "dict", "more", "pi"]
    >>> valid_pairs(keys, values)
    [('key', 'value'), ('not valid',), ('not valid',), ('another', 'more'), \
((3.14,), 'pi')]

    >>> keys = [(1, 2), "ok", 5.5, [], "done"]
    >>> values = ["tuple", "string", "float", "list", "end"]
    >>> valid_pairs(keys, values)
    [((1, 2), 'tuple'), ('ok', 'string'), (5.5, 'float'), ('not valid',), \
('done', 'end')]

    """
    # initialize output list
    key_value_pairs=[]
    # initialize counter
    i=0
    # dictionary keys must be immutable
    while i < len(keys):
        # check if each item in key is a possible dictionary key
        if type(keys[i]) in [int, float, str, bool, tuple]:
            # if yes, add the key with corresponding value in a tuple
            key_value_pairs.append((keys[i], values[i]))
            # otherwise, add the 'not valid' tuple
        else:
            key_value_pairs.append(('not valid',))
        # iterate counter
        i+=1

    return key_value_pairs