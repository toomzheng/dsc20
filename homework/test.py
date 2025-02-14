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
    # Recursively process positional arguments
    def process_positional(index):
        if index >= len(args):
            return []
        # Create a tuple for the current positional argument and then process the rest
        return [(f"positional_{index}", args[index])] + process_positional(index + 1)
    
    # Recursively process keyword arguments. We'll process the items in the order they were provided.
    def process_keyword(index, items):
        if index >= len(items):
            return []
        key, value = items[index]
        return [(f"keyword_{index}_{key}", value)] + process_keyword(index + 1, items)
    
    # Convert the kwargs into a list of items to maintain order
    keyword_items = list(kwargs.items())
    
    # Combine the results from positional and keyword processing
    return process_positional(0) + process_keyword(0, keyword_items)