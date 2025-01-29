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
