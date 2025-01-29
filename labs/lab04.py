"""
DSC 20 Winter 2025 Lab 04
Name: Tom Zheng
PID: A18424137
"""

# Question 1.1
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
    # map the lambda function onto every integer in int_lst
    return list(map(lambda x: x*mult_factor, int_lst))


# Question 1.2
def problem_2(int_lst, factor):
    """
    Returns a list where each number has the factor
    ---
    Parameters:
        int_lst: a list of integers 
        factor: a positive integer
    ---
    Returns:
        a new list, where each element from a given list 
        has a given factor

    >>> problem_2([1, 3, 5], 3)
    [3]
    >>> problem_2([1, 3, 5], 1)
    [1, 3, 5]
    >>> problem_2([], 10)
    []
    >>> problem_2([1, 3, 4, 6, 5], 2)
    [4, 6]
    """
    # filter through every value in the list, and return it if it is a "factor"
    return list(filter(lambda x:x % factor == 0, int_lst))


# Question 1.3
def problem_3(int_lst, factor):
    """
    Returns a list where each number has the factor, or None if not
    ---
    Parameters:
        int_lst: a list of integers 
        factor: a positive integer
    ---
    Returns:
        a list, where each element from a given list has a given factor, 
        and if that's not the case, replace it with None

    >>> problem_3([1, 3, 5], 3)
    [None, 3, None]
    >>> problem_3([1, 3, 5], 1)
    [1, 3, 5]
    >>> problem_3([], 10)
    []
    >>> problem_3([1, 3, 4, 6, 5], 2)
    [None, None, 4, 6, None]
    """
    return list(map(lambda x: x if x % factor == 0 else None, int_lst))


# Question 1.4
def problem_4(lst):
    """
    Remove the None from the list
    ---
    Parameters:
        lst: a list of integers and/or None values
    ---
    Returns:
        a list that contains only the integers

    >>> problem_4([None, 3, None])
    [3]
    >>> problem_4([None, None, 4, 6, None])
    [4, 6]
    >>> problem_4([0, 1, 2, 3, 4, None])
    [0, 1, 2, 3, 4]
    >>> problem_4([])
    []
    """
    # can't use None because 0 is None
    # filter(None, lst) means that 0 is not checked explicitly
    # None is falsey, and 0 is falsey as well. 
    return list(filter(lambda x: x != None, lst))


# Question 2.1
def forming_teams_1(teams, limit):
    """
    Returns a list with team names with enough people, or `Need more players`
    ---
    Parameters:
        teams: a dictionary where 
            - the keys are strings (team names) 
            - the values are lists of strings (representing team members)
        limit: a non-negative integer which specifies the allowed team size
    ---
    Returns:
        a list of team names that have enough members to practice, 
        or the string 'Need more players' if a team size does not 
        meet the required size

    >>> teams = {"team1": ["A", "B", "C"], "team2": ["D", "E"]}
    >>> forming_teams_1(teams, 3)
    ['team1', 'Need more players']
    >>> forming_teams_1(teams, 4)
    ['Need more players', 'Need more players']
    >>> forming_teams_1(teams, 0)
    ['team1', 'team2']
    >>> forming_teams_1({}, 3)
    []
    """
    # filter for teams where the size is greater than 3
    return list(map(lambda x: x if len(teams[x])>=limit \
                    else 'Need more players', teams))


# Question 2.2
def forming_teams_2(teams, limit):
    """
    Returns a list with only team names with enough people
    ---
    Parameters:
        teams: a dictionary where 
            - the keys are strings (team names) 
            - the values are lists of strings (representing team members)
        limit: a non-negative integer which specifies the allowed team size
    ---
    Returns:
        a list containing only the keys of the teams that have enough 
        members to practice

    >>> teams = {"team1": ["A", "B", "C"], "team2": ["D", "E"]}
    >>> forming_teams_2(teams, 3)
    ['team1']
    >>> forming_teams_2(teams, 4)
    []
    >>> forming_teams_2(teams, 0)
    ['team1', 'team2']
    >>> forming_teams_2({}, 3)
    []
    """
    return list(filter(lambda x: len(teams[x]) >= limit, teams))


# Question 3.1
def next_round_1(teams, threshold):
    """
    Returns the teams advancing to next round based on if score is at least
    `next_round`, along with their score multipled by 25, in a list of tuples
    ---
    Parameters:
        teams: a dictionary where 
            - the keys are strings (team names)
            - the values are integers (the team's corresponding score) 
        threshold: an integer representing the minimum score required 
        to advance
    ---
    Returns:
        a list of tuples: each tuple should contain the name of a team that 
        advances to the next round as the first element, and their score 
        multiplied by 25 as the second element

    >>> next_round_1({"team1": 10, "team2": 20}, 10)
    [('team1', 250), ('team2', 500)]
    >>> next_round_1({"team1": 36, "team2": 4}, 10)
    [('team1', 900)]
    >>> next_round_1({"team1": 5, "team2": 14}, 20)
    []
    >>> next_round_1({}, 3)
    []
    """
    # map the points * 25 onto all valid team scores, and make it a tuple.
    return list(map(lambda x: (x, teams[x] * 25), \
                    # filter through all valid teams
                    list(filter(lambda x: teams[x] >= threshold, teams))))


# Question 3.2
def next_round_2(teams, threshold):
    """
    Returns the teams advancing to next round and number of their scores
    that could make them advance
    ---
    Parameters:
        teams: a dictionary where 
            - the keys are strings (team names) 
            - the values are lists of integers (the team's corresponding
            scores)
        threshold: an integer representing the score required to advance
    ---
    Returns:
        a list of tuples: each tuple should contain the name of a team that
        advances to the next round as the first element, and the number of
        their scores that meet or exceed the required threshold as the
        second element

    >>> next_round_2({"team1": [5, 10, 15], "team2": [20]}, 10)
    [('team1', 2), ('team2', 1)]
    >>> next_round_2({"team1": [], "team2": [36, 4, 20, 0]}, 10)
    [('team1', 0), ('team2', 2)]
    >>> next_round_2({}, 3)
    []
    """
    # count out the number of valid scores for each one 
    return list(
        map(
            lambda x: (x, len(list(filter\
                            # filter out for the valid scores for each team
                            (lambda x: x >=threshold, teams[x])))), teams
            )
        )


# Question 3.3
def next_round_3(teams, results):
    """
    Finds the teams that advance: ('qualified', 'advanced', 'winner'), returns
    a list of tuples with team name and result
    ---
    Parameters:
        teams: a list of strings with team names
        results: a list of strings with the result for each team
    ---
    Returns:
        a list of tuples for only the teams that have advanced to the next
        round; in each tuple, the first element should be the team's name,
        and the second element should be their result, both as strings

    >>> next_round_3(['team1', 'team2', 'team3'], ['qualified', 'out', 'winner'])
    [('team1', 'qualified'), ('team3', 'winner')]
    >>> next_round_3(['team1', 'team2'], ['eliminated', 'out'])
    []
    >>> next_round_3(['team1', 'team2'], ['eliminated', 'advanced'])
    [('team2', 'advanced')]
    >>> next_round_3([], [])
    []
    """
    # zip will turn teams and results into matching tuples
    # see which results are valid
    return list(filter(lambda x: x[1] in \
                       ['qualified', 'winner', 'advanced'], \
                        zip(teams, results)))
