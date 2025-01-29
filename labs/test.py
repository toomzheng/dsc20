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