def collected_items(filepath):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> collected_items('files/ings1.txt')
    ['ice-cream', 'boba tea', 'fish']
    >>> collected_items('files/ings2.txt')
    ['shovel', 'headphones', 'bird', 'brownies']
    >>> collected_items('files/empty_trip.txt')
    []

    # Add at least 3 doctests below here #
    """
    items=[]
    position_of_item = 2
    with open(filepath, 'r') as file:
         for line in file:
              line=line.strip()
              if line:
                   parts=line.split(',')
                   items.append(parts[position_of_item])

    return items