def older_than_30(ages):
    """
    Counts the number of people at least as old as 30 years

    >>> ages = [[120, -154, 245], [145, -360, -615, 306]]
    >>> older_than_30(ages)
    0
    >>> ages = [[8848], [779, 0]]
    >>> older_than_30(ages)
    2
    >>> ages = [[80, -854, 900], [45, 360, 15]]
    >>> older_than_30(ages)
    2
    """
    return sum([len([i[j]//12 for j in range(0, len(i)) if i[j]//12 >= 30]) \
            for i in ages])