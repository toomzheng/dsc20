"""
DSC 20 Winter 2025 Homework 06
Name: Tom  
PID: Zheng
Source: TODO
"""


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
    check_even = 2
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
            val = last_arg % check_even == 0
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

# Question 2
def rearrange_args(*args, **kwargs):
    """
    Combines positional and keyword arguments into a list of tuples. Then,
    labels them according to their type and index.

    Args:
        *args: Variable-length positional arguments.
        **kwargs: Variable-length keyword arguments.

    Returns:
        list: A list of tuples where each tuple has a has a 'type' 
        (positional or keyword) and the index

    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> rearrange_args(3.14, None, player1=[1, 2], player2={})
    [('positional_0', 3.14), ('positional_1', None), ('keyword_0_player1', \
[1, 2]), ('keyword_1_player2', {})]

    >>> rearrange_args()
    []

    >>> rearrange_args('test', 42)
    [('positional_0', 'test'), ('positional_1', 42)]
    """
    # to solve this problem we can use recursion by passing each args and 
    # kwargs back in separately. by using args and kwargs they're optional
    # statements for the function, so we can set up recursions for each
    # individual one. 

    # first, set up the two lists that will be combined given they both exist:
    if args and kwargs:
        pos_result = rearrange_args(*args)
        kw_result = rearrange_args(**kwargs)
        return pos_result + kw_result

    # now set up the recursion for performing operations on each one
    # individually
    if args:
        # base case when args only has one argument left
        if len(args) == 1:
            return [(f"positional_0", args[0])]
        else:
            # recursively process all other args arguments
            result = rearrange_args(*args[:-1])  # crucial to only pass args
            index = len(args) - 1
            # by going backwards, we are able to easily get the indexes
            result.append((f"positional_{index}", args[-1]))
            return result
    # set up same recursion for performing operation on each kwargs indvidually
    if kwargs:
        # convert to keys
        keys = list(kwargs.keys())
        # base case for only one keyword argument left
        if len(keys) == 1:
            key = keys[0]
            # kwargs[key] provides us the value
            return [(f"keyword_0_{key}", kwargs[key])]
        else:
            # in recursion, we can remove the last keyword argument and
            # process the rest
            last_key = keys[-1]
            last_value = kwargs[last_key]
            # now we can remove the last keyword by using the del statement
            del kwargs[last_key]
            result = rearrange_args(**kwargs) # now we pass back into rearrange
            index = len(result)
            result.append((f"keyword_{index}_{last_key}", last_value))
            return result

    return []  # basse case in case no arguments are ever provided

# Question 3.1
def count_the_password(lst, password):
    """
    Recursively checks if the password to enter HDSI is present in the list
    and counts the number of occurences

    Args:
        lst (list): List of strings (passwords) to search through.
        password (str): The target string to identify and count.

    Returns:
        int: Number of times the password appears in the list.

    
    >>> count_the_password(["cooldragon", "dragon", "gold"], "dragon")
    1
    >>> count_the_password(["DRAGON", "dragon!!"], "dragon")
    0
    >>> count_the_password([], "dragon")
    0
    >>> count_the_password(["dragon "], "dragon")
    0
    >>> count_the_password(["dragon", "likes", "recursions", "right", \
"dragon", "?"], "dragon")
    2

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> count_the_password(["", " ", "dragon"], "dragon")
    1
    >>> count_the_password(["dragon", "dragon", "dragon"], "dragon")
    3
    >>> count_the_password(["dragonn", "ndragon", "dragon"], "dragon")
    1
    """

    # base case to stop the recursion
    if lst == []:
        return 0
    elif lst[0] == password:
        # even when the has one element, slicing like this returns []
        return 1 + count_the_password(lst[1:], password)
    # do recursion even if it's not equal to the password
    else:
        # continue the loop and don't add 1 to the count
        return count_the_password(lst[1:], password)


# Question 3.2
def corrupt_password(input, to_insert):
    """
    Recursively inputs a character between each character of the input string.

    Args:
        input (str): The original string to be corrupted.
        to_insert (str): The character to be inserted between each character
        in the input.

    Returns:
        str: The new corrupted string with the inserted characters.


    >>> corrupt_password('dragon', '#')
    'd#r#a#g#o#n#'
    >>> corrupt_password('', '@')
    ''
    >>> corrupt_password('I can help', '-')
    'I- -c-a-n- -h-e-l-p-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> corrupt_password('a', '*')
    'a*'
    >>> corrupt_password('12345', '+')
    '1+2+3+4+5+'
    >>> corrupt_password('password', '')
    'password'
    """

    if input == "":
        # this gets concatenated at the end of below
        return ""
    else:
        result = input[0] + to_insert + corrupt_password(input[1:], to_insert)
    return result


# Question 3.3
def outsmart_dragon(lst, password, to_insert):
    """
    Recurses over a list of strings, corrupting all strings except the password
    by adding a specified character after each character.

    Args:
        lst (list): A list of passwords (strings) to process
        password (str): The password string to exclude from corruption.
        to_insert (str): The character to insert between characters for
        corruption.

    Returns:
        list: A list of processed strings, with the password untouched and
        all other strings corrupted.

    >>> outsmart_dragon(['dragon'], 'dragon','#')
    ['dragon']
    >>> outsmart_dragon([], 'dragon','@')
    []
    >>> outsmart_dragon(['help me', 'dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'dragon']
    >>> outsmart_dragon(['help me', 'dear dragon'], 'dragon','-')
    ['h-e-l-p- -m-e-', 'd-e-a-r- -d-r-a-g-o-n-']
    >>> outsmart_dragon(['DrAgOn', 'Dragon'], 'dragon','-')
    ['D-r-A-g-O-n-', 'D-r-a-g-o-n-']

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> outsmart_dragon(['', 'dragon'], 'dragon','*')
    ['', 'dragon']
    >>> outsmart_dragon(['dragon', 'drag on'], 'dragon','+')
    ['dragon', 'd+r+a+g+ +o+n+']
    >>> outsmart_dragon(['password123', 'dragon', ''], 'dragon','!')
    ['p!a!s!s!w!o!r!d!1!2!3!', 'dragon', '']
    """

    # string corrupter that performs an action when the passed in lst is a str
    if isinstance(lst, str):
        # base case: empty string
        if lst == "":
            return ""
        # recursively build corrupted string
        return lst[0] + to_insert \
            + outsmart_dragon(lst[1:], password, to_insert)

    # list checker that goes through the list checking each element
    # base case: empty list
    if not lst:
        return []

    # check the first element each time
    first = lst[0]
    # if it matches the password
    if first == password:
        # DON'T corupt
        return [first] + outsmart_dragon(lst[1:], password, to_insert)
    else:
        # otherwise, if it doesn't, feed this back into the function but as
        # a str, to trigger the string corrupter.
        corrupted = outsmart_dragon(first, password, to_insert)
        # once corrupted, we come back to recursing over the original list
        return [corrupted] + outsmart_dragon(lst[1:], password, to_insert)


# Question4
def corrupt_with_vowels(input):
    """
    Recursively removes vowels over a string input

    Args:
        input (str): a string of input

    Returns:
        str: the input string with the vowels removed

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> corrupt_with_vowels('')
    ''
    >>> corrupt_with_vowels('a a a a a a a ')
    '       '
    >>> corrupt_with_vowels('0192830')
    '0192830'
    """
    new_word = ""
    if input == "":
        # this gets concatenated at the end of below
        return ""
    elif input[0].lower() not in "aeiou":
        return new_word + input[0] + corrupt_with_vowels(input[1:])
    else:
        return corrupt_with_vowels(input[1:])


# Question 5
def where_to_go(point1, point2, separator):
    """
    Returns a string with all integers in between point1 and point2
    (both inclusive) separated by the given separator. The criteria for the
    order of the output string is as follows:

    When point1 < point2, then the numbers in the string are in ascending \
        order.
    When point1 > point2, then the numbers in the string are in descending \
        order.
    When point1 == point2, just return the string representation of the bound \
        itself.

    Args:
        point1 (int): one integer bound
        point2 (int): second integer bound
        separator (str): string to separate in between characters with

    Returns:
        string: a string with all integers between point1 and point2
        separated by the separator and ordered based on the criteria


    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> where_to_go(-30, -35, '-')
    '-30--31--32--33--34--35'
    >>> where_to_go(10, 8, 'left')
    '10left9left8'
    >>> where_to_go(3, 3, ', ')
    '3'
    """
    if point1 < point2:
        return str(point1) + separator \
            + where_to_go(point1 + 1, point2, separator)
    elif point1 > point2:
        return str(point1) + separator \
            + where_to_go(point1 - 1, point2, separator)
    else:
        return str(point1)
