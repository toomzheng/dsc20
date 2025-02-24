"""
DSC 20 Winter 2025, Lab 07
Name: Tom Zheng
PID: A18424137
Source: n/a
"""

# Question 1
def max_recursion(tup):
    """
    Find the maximum element in a tuple recursively.

    Args:
        tup (tuple): a tuple of integers
    Returns:
        The maximum number

    >>> max_recursion((1,2,3,4))
    4
    >>> max_recursion((13,2,3,4))
    13
    >>> max_recursion((13,2,33,4))
    33
    """
    # base case if the tuple is empty
    if len(tup) == 1:
        return tup[0]
    # find the max of the rest of the tuple
    max = max_recursion(tup[1:])

    # compare the first element with the max of the rest and return the largest
    return tup[0] if tup[0] > max else max

"""
1, 2, 3, 4 would go in
it would recurse until 0 is returned
then it goes to 4 which is bigger than 0 so 4 is returned
then it goest to 3 which is less than 4 so 4 is returned
and so on
"""


# Question 2
def max_or_min_recursion(tup, find_max = True):
    """
    Find the maximum or minimum element in a tuple recursively.

    Args:
        tup (tuple): a tuple of integers
        find_max (bool): whether to find max or min
    Returns:
        The maximum or minimum number

    >>> max_or_min_recursion((1,2,3,4))
    4
    >>> max_or_min_recursion((13,2,3,4), False)
    2
    >>> max_or_min_recursion((13,2,33,-4), True)
    33
    """
    # from question 1:
    if len(tup) == 1:
        return tup[0]
    
    max_or_min = max_or_min_recursion(tup[1:], find_max)
    

    if find_max:
        return tup[0] if tup[0] > max_or_min else max_or_min
    
    return tup[0] if tup[0] < max_or_min else max_or_min


# Question 3
def find_winner(record, find_max = True):
    """
    Find the team with highest or lowest score recursively.

    Args:
        record (list): a list of tuples, where the first element in each tuple 
        is the team's name and the second element is the team's score
        find_max (bool): whether to find team with max or min score
    Returns:
        The team with highest or lowest score, and returns first if there is
        a tie

    >>> find_winner([('Red',23),('Green', 49), ('Blue', 32)])
    'Green'
    >>> find_winner([('UCSD', 12.88),('SDSU', 15)], find_max=False)
    'UCSD'
    >>> find_winner([('Panda', 10), ('Koala', 10), ('Hippo', 5)], find_max=True)
    'Panda'
    """

    if len(record) == 1:
        return record[0][0]

    # current team and score
    team, score = record[0]

    # find rest of the candidates
    rest = find_winner(record[1:], find_max)

    # the next score
    next_score = record[1][1]

    if find_max:
        return team if score >= next_score else rest
    return team if score <= next_score else rest


# Question 4
def from_list_to_dict(lst):
    """
    Converts a list of tuples into a dictionary recursively.

    Args:
        lst (list): a list of tuples, where the first element is the team name 
        (key) and second element is their score (value)
    Returns:
        A dictionary with each team name as keys and their score as values

    >>> lst = [(1,2),(3,4),(5,6)]
    >>> from_list_to_dict(lst)
    {1: 2, 3: 4, 5: 6}

    >>> lst = [("one",1),("two",2)]
    >>> from_list_to_dict(lst)
    {'one': 1, 'two': 2}

    >>> lst = []
    >>> from_list_to_dict(lst)
    {}
    """
    if not lst:
        return {}

    if len(lst) == 1:
        return {lst[0][0]: lst[0][1]}
    
    # create a dictionary
    init_dict = {lst[0][0]: lst[0][1]}

    rest = from_list_to_dict(lst[1:])

    # add each of the previously created dictionaries to init_dict
    init_dict.update(rest)
    
    return init_dict

# Question 5
class Mascot:
    """ 
    Creates a simple Mascot class with 1 class attribute (type)
    and 3 instance attributes (color, nickname, event)
    >>> mascot1 = Mascot("blue and white", "Shark", "West Athletic Conference")
    >>> Mascot.brings
    'Luck'
    >>> mascot1.color
    'blue and white'
    >>> mascot1.sing_song("Baby Shark")
    "Shark sings 'Baby Shark' at West Athletic Conference"
    >>> mascot1.change_nickname("Doo Doo")
    >>> mascot1.nickname
    'Doo Doo'
    >>> mascot1.event
    'West Athletic Conference'


    >>> mascot2 = Mascot('green', 'Stanford Tree',\
'Collegiate Football Conference')
    >>> Mascot.brings
    'Luck'
    >>> mascot2.color
    'green'
    >>> mascot2.sing_song("Deck the Halls")
    "Stanford Tree sings 'Deck the Halls' at Collegiate Football Conference"
    >>> mascot2.change_nickname("The Tree")
    >>> mascot2.nickname
    'The Tree'
    """
    # shared across all instances
    brings = 'Luck'
   
 # Initializer (Constructor) / Instance Attributes
    def __init__(self, color, nickname, event):
        self.color = color
        self.nickname = nickname
        self.event = event


    def sing_song(self, song):
        return f"{self.nickname} sings '{song}' at {self.event}"


    def change_nickname (self, new_name):
        # update the nickname
        self.nickname = new_name


# Question 6
class Game:
    """
    Creates a class with 1 class attribute and two class methods

    >>> Game.mascot
    'King Triton'
    >>> Game.starts()
    'Saturday, November 2'
    >>> Game.ends()
    'Sunday, November 17'
    """

    mascot = 'King Triton'

    @classmethod
    def starts(cls):
        return 'Saturday, November 2'
    
    @classmethod
    def ends(cls):
        return 'Sunday, November 17'
