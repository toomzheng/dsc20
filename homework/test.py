def supervision_teams(team, company_name):
    """
    Initialize two lists where one will hold the values of the first team
    and the other the values of the second team. Iterate through team separating
    the even indices and the odd indices. Then, add company_name in at the
    respective indices for ecah list.
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> supervision_teams(["p1", "p2", "p3"], "Marina")
    (['Marina', 'p1', 'p3'], ['p2', 'Marina'])
    >>> supervision_teams(["p1"], "Marina")
    (['Marina', 'p1'], ['Marina'])
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "Marina")
    (['Marina', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'Marina'])

    # Add your own doctests below
    >>> supervision_teams([""], "")
    (['', ''], [''])
    >>> supervision_teams(["p1", ""], "Tom")
    (['Tom', 'p1'], ['', 'Tom'])
    >>> supervision_teams([],'')
    ([''], [''])
    """
    # YOUR CODE GOES HERE #
    team1 = []
    team2 = []
    i=0
    for name in team:
        if i % 2 == 0 or i == 0:
            team1.append(name)
            i+=1
        else: 
            team2.append(name)
            i+=1
    
    team1.insert(0, company_name)
    team2.append(company_name)
    return (team1, team2)