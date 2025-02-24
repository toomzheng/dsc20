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