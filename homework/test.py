def age_average(lst):
    """
    Iterate over every string in the list and convert it to an integer. Add
    all of them up and devide that by the length of the list to find the avg.
    If a number is negative, do not count it and subtract 1 from the length of 
    the list.

    >>> age_average(["20", "21", "22"])
    '21.0'
    >>> age_average(["50", "25", "30"])
    '35.0'
    >>> age_average(["40", "-999", "45"])
    '42.5'
    >>> age_average([])
    '0.0'

    # Add your own doctests below
    >>> age_average(["0", "0", "0"])
    '0.0'
    >>> age_average(["12", "43", "21"])
    '25.3'
    >>> age_average(["-12", "-999"])
    '0.0'
    >>> age_average(["33"])
    '33.0'
    """
    total_ages = 0
    total_length = 0
    #case for nonempty list
    for age in lst:
        if int(age) > 0:
            total_ages += int(age)
            total_length += 1
    # case empty list or for if all numbers are negative
    if total_length == 0:
        return "0.0"
    # round to one decimal place
    return str(round(total_ages/total_length, 1))