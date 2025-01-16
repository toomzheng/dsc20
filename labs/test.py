def password_to_lounge(names_dict):
    """
    Constructs secret language based on 3 rules:
    (1) If code is even-length string, reverse name;
    (2) If code is non-negative integer, add X `#` where X is name length;
    (3) If code is negative integer, get first character of name.
    --
    Parameters:
        names_dict: dictionary of names as keys and code as values
    --
    Returns:
        A password generated based on rules above.

    >>> dict1 = {'Adrian': 'haha', 'Marina': 1, \
'Langlois': 0, 'Walter': -2}
    >>> password_to_lounge(dict1)
    'nairdA##############W'
    >>> dict2 = {'Ty': 'dsc', '': 20}
    >>> password_to_lounge(dict2)
    ''
    >>> dict3 = {'M.L.': 5, 'DSC20': 'ab'}
    >>> password_to_lounge(dict3)
    '####02CSD'
    """
    password=""
    for name in names_dict:
        if type(names_dict[name]) == str and len(names_dict[name]) % 2 == 0:
            password+=name[::-1]
        elif type(names_dict[name]) == int:
            if names_dict[name] >= 0:
                password+="#" * len(name)
            elif names_dict[name] < 0:
                password+=name[0:1]

    return password