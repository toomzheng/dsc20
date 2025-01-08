def total_for_painting(prices):
    """
    Calculates the total price of paintings given a string of 
    integers.
    --
    Parameters:
        prices: a string of postive integers
    --
    Returns:
        An integer representing the total of the integers
    >>> prices = "10 20 30 3"
    >>> total_for_painting(prices)
    63

    >>> prices = "1 2 -3"
    >>> total_for_painting(prices)
    0

    >>> prices = ""
    >>> total_for_painting(prices)
    0
    """
    # YOUR CODE GOES HERE #
    listed_prices=prices.split()
    total = 0
    for price in listed_prices:
        price=int(price)
        total += price
    return total
