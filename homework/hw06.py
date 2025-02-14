"""
DSC 20 Winter 2025 Homework 06
Name: Tom  
PID: Zheng
Source: TODO
"""

#Question 1
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
    """
    result = {}

    def helper(inputs):
        # base case -- if no input, return the result
        if not inputs:
            return result
        else:
            # initialize first_arg variable
            first_arg = inputs[0]
            # handle each type
            # ADD A CHECK FOR BOOLS AS THEY ARE CONSIDERED INTS
            if isinstance(first_arg, bool):
                key = "garbage"
                val = first_arg
            elif isinstance(first_arg, int):
                key = "int"
                val = first_arg % 2 == 0
            elif isinstance(first_arg, float):
                key = "float"
                val = abs(first_arg) if first_arg < 0 else int(first_arg)
            elif isinstance(first_arg, str):
                key = "str"
                val = "".join(first_arg[i] for i in range(0, len(first_arg), 2))
            elif isinstance(first_arg, list):
                key = "list"
                val = len(first_arg)
            else:
                key = "garbage"
                val = first_arg

            # add current arg to result
            if key in result:
                result[key].append(val)
            else:
                result[key] = [val]

            # apply recursion
            helper(inputs[1:])

    # call recursive function
    helper(args)
    return result

#Question 2
def rearrange_args(*args, **kwargs):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # YOUR CODE GOES HERE # 

#Question 3.1
def count_the_password(lst, password):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    # YOUR CODE GOES HERE # 

#Question 3.2  
def corrupt_password(input, to_insert):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> corrupt_password('dragon', '#')
    'd#r#a#g#o#n#'
    >>> corrupt_password('', '@')
    ''
    >>> corrupt_password('I can help', '-')
    'I- -c-a-n- -h-e-l-p-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # YOUR CODE GOES HERE # 

# Question 3.3
def outsmart_dragon(lst, password, to_insert):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    # YOUR CODE GOES HERE # 

#Question4
def corrupt_with_vowels(input):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # YOUR CODE GOES HERE # 

#Question 5
def where_to_go(point1, point2, separator):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # YOUR CODE GOES HERE # 