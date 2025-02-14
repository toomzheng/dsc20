def field_trip(age_limit, **kwargs):
    """
    Determines the number of adults needed for each group based
    on the age limit. For every three children younger than the
    specified age limit, one adult is needed.
    ---
    Parameters:
        - age_limit (int): The maximum age considered as a child.
        - **kwargs: Variable keyword arguments where each key is 
        a group ID, and the value is a list of children's ages in 
        that group.
    ---
    Returns:
        dict: A dictionary where each key is a group ID, and the 
        value is the number of adults required for that group.

    >>> field_trip(14, group1 = [1, 2, 3], group2 = [4, 5, 6, 7], \
    group3=[15, 16])
    {'group1': 1, 'group2': 2, 'group3': 0}
        
    >>> field_trip(14, group1 = [21, 3], group2 = [41, 1, 2, 24, 6], \
    group3=[30, 3, 1, 7, 88])
    {'group1': 1, 'group2': 1, 'group3': 1}
        
    >>> field_trip(100, group1 = [21, 3], group2 = [41, 1000, 2, 24, 6], \
    group3 = [3, 1, 7, 88])
    {'group1': 1, 'group2': 2, 'group3': 2}
    """
    from lab06 import number_of_adults_3
    for group in kwargs:
        ()
    return