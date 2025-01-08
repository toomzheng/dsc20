"""
DSC 20 Winter 2025 Lab 01
Name: TODO
PID: TODO
"""

# Question 1
def team_member_age(ages):
    """
    Checks whether at least one team member is 23 or older.
    ---
    Parameters: 
        lst: a list of positive integers, might be empty
    ---
    Returns:
        True if at least one member is 23 or older,
        False otherwise

    >>> team_member_age([19, 22, 21])
    False
    >>> team_member_age([19, 23, 15, 27])
    True
    >>> team_member_age([])
    False
    """

    i=len(ages)
    mark=0
    while mark < i:
        if ages[mark] >= 23:
            return True
        mark+=1
    return False

# Question 2
def counter_23_and_over(ages):
    """
    Counts how many people aged 23 or older are in the given list. 
    ---
    Parameters: 
        lst: a list of positive integers, might be empty
    ---
    Returns:
        The number of people whose age is 23 or older.

    >>> counter_23_and_over([])
    0
    >>> counter_23_and_over([12, 15])
    0
    >>> counter_23_and_over([12, 23, 34])
    2
    >>> counter_23_and_over([40, 15, 22])
    1
    """
# YOUR CODE GOES HERE #
    number = 0
    i=len(ages)
    mark = 0
    while mark < i:
        if ages[mark] >= 23:
            number +=1
        mark+=1
    return number

# Question 3
def company_name_one(first_name, last_name):
    """
    Concatenates the string parameters into the output string. 
    ---
    Parameters:
        first_name: first name, as a string
        last_name: last name, as a string
    ---
    Returns:
        A new string with the company's name. 

    >>> company_name_one("Marina", "Langlois")
    'Company name is Langlois a'
    >>> company_name_one("Marina", "")
    'Company name is  a'
    >>> company_name_one("THE", "best")
    'Company name is best E'
    """
    # YOUR CODE GOES HERE #
    companyName=last_name+" " +first_name[-1]
    return f"Company name is {companyName}"

# Question 4
def company_name_two(names):
    """
    Creates the name for the team by putting together first and last characters of each name. Adds a space if the input only has one character. 
    ---
    Parameters:
        names: list of names, as strings
    ---
    Returns:
        Team name as a string

    >>> names = ["Marina", "J", "Mike"]
    >>> company_name_two(names)
    'MaJ Me'

    >>> names = ["Sheldon", "Leonard", "Raj", "Howard"]
    >>> company_name_two(names)
    'SnLdRjHd'

    >>> names = ["Y", "J", "B"]
    >>> company_name_two(names)
    'Y J B '
    """
    # YOUR CODE GOES HERE #
    #iterate through names
    companyName=""
    for name in names:
        #for names when only 1 character
        if len(name) < 2:
            #set a temporary helper variable
            temp=name[0]+" "
            #concactenate temp into companyName str
            companyName+=temp
        else:
            temp=name[0]+name[-1]
            companyName+=temp
    return companyName

# Question 5.1
def new_slogan_concat(words, separator):
    """
    Creates a slogan from the words, adding a separator between them. 
    ---
    Parameters:
        words: list of words, as strings
        separator: single character 
    ---
    Returns:
        A slogan as a string

    >>> words = ["Come", "and", "see"]
    >>> new_slogan_concat(words, " ")
    'Come and see'

    >>> words = ["Work", "hard", "nap", "harder"]
    >>> new_slogan_concat(words, ".")
    'Work.hard.nap.harder'
    """
    # YOUR CODE GOES HERE #
    # begin with an empty string for the slogan #
    slogan=""
    periods=len(words)-1
    # iterate through each word in words #
    for word in words:
        if periods != 0:
            slogan+=word+separator
            periods -= 1
        else:
            slogan+=word
    return slogan

# Question 5.2
def new_slogan_join(words, separator):
    """
    Creates a slogan from the words, adding a separator between them. 
    ---
    Parameters:
        words: list of words, as strings
        separator: single character 
    ---
    Returns:
        A slogan as a string

    >>> words = ["Come", "and", "see"]
    >>> new_slogan_join(words, " ")
    'Come and see'

    >>> words = ["Work", "hard", "nap", "harder"]
    >>> new_slogan_join(words, ".")
    'Work.hard.nap.harder'
    """
    # YOUR CODE GOES HERE #
    return separator.join(words)

# Question 6.1
def idea_simple_drawing(symbol, repeat):
    """
    Creates a string of symbols 
    ---
    Parameters:
        symbol: a single character
        repeat: positive integer
    ---
    Returns:
        A string of symbols repeated a given number of times.

    >>> idea_simple_drawing("-", 4)
    '----'
    >>> idea_simple_drawing("+", 5)
    '+++++'
    >>> idea_simple_drawing("", 2)
    ''
    """
    # YOUR CODE GOES HERE #
    return symbol*repeat

# Question 6.2
def idea_longer_drawing(symbols, repeats):
    """
    Creates a string of symbols
    ---
    Parameters:
        symbols: a list of single characters
        repeat: a list of positive integers, has the same length
        as symbols list
    ---
    Returns:
        A string of symbols repeated a corresponding number of
        times.

    >>> idea_longer_drawing(['-', '+'], [4, 5])
    '----+++++'
    >>> idea_longer_drawing(['dsc', '20'], [1, 5])
    'dsc2020202020'
    >>> idea_longer_drawing([], [])
    ''
    """
    # YOUR CODE GOES HERE #
    #marker for both lists
    i=0
    drawing=""
    while i < len(symbols): # either list will work #
        drawing+=symbols[i]*repeats[i]
        i+=1
    return drawing

# Question 7.1
def average_rating(ratings):
    """
    Finds average where numbers lower than 3.755 get a value of a 0.

    Args:
        ratings: list of integers ranging from 1 to 5

    Returns:
        The average of the ratings rounded to the second decimal place
    
    >>> average_rating([5, 5, 5])
    5.0
    >>> average_rating([5, 5, 4])
    4.67
    >>> average_rating([4, 2, 1])
    1.33
    """
    total=0
    for rating in ratings:
        if rating < 3.75:
            rating=0
        total+=rating
        average=round(total/len(ratings), 2)
    return average

# Question 7.2
def average_rating_lists(ratings):
    """
    Finds the highest average among the inner lists.
    --
    Parameters:
        ratings: a list of list(s) of numbers ranging from 1 to 5
    --
    Returns:
        The highest average rounded to two decimal places.
    
    >>> ratings = [[1, 5, 5], [5, 5, 5]]
    >>> average_rating_lists(ratings)
    5.0

    >>> ratings = [[2.56, 4.76, 3.12], [3.1, 4.5, 5], [1.4, 4.54]]
    >>> average_rating_lists(ratings)
    3.17

    >>> average_rating_lists([])
    -1
    """
    # YOUR CODE GOES HERE #
    total=0
    lst=[]
    if len(ratings) == 0:
        return -1
    for company in ratings:
        for rating in company:
            if rating <= 3.75:
                rating = 0
            total+=rating
        average=round(total/len(company), 2)
        lst.append(average)
        #reset the total count after each company's rating is calculated
        total = 0
    return max(lst)

# Question 7.3
def average_rating_lists_index(ratings):
    """
    Finds the index of the list with the highest average. If there are 
    multiple lists with the same average, return the index of the list 
    that occurs first.
    --
    Parameters:
        ratings: a list of list(s) of numbers ranging from 1 to 5
    --
    Returns:
        The index of the list with the highest average
    
    >>> ratings = [[1, 5, 5], [5, 5, 5]]
    >>> average_rating_lists_index(ratings)
    1

    >>> ratings = [[2.56, 4.76, 3.12], [1.4, 4.54], [3.1, 4.5, 5]]
    >>> average_rating_lists_index(ratings)
    2

    >>> average_rating_lists_index([])
    -1
    """
    # YOUR CODE GOES HERE #
    total=0
    lst=[]
    if len(ratings) == 0:
        return -1
    for company in ratings:
        for rating in company:
            if rating <= 3.75:
                rating = 0
            total+=rating
        average=round(total/len(company), 2)
        lst.append(average)
        #reset the total count after each company's rating is calculated
        total = 0
    return lst.index(max(lst))

# Question 7.4
def average_rating_lists_names(ratings, names):
    """
    Finds the name of the list with the highest average, if the are 
    multiple lists with the same highest average, return the name 
    of the list that occurs first.
    --
    Parameters:
        ratings: a list of lists of numbers ranging from 1 to 5
        names: a list of strings
    --
    Returns:
        The name of the list with the highest average rating.

    >>> ratings = [[1, 5, 5], [5, 5, 5]]
    >>> names = ["team1", "team2"]
    >>> average_rating_lists_names(ratings, names)
    'team2'

    >>> ratings = [[2.56, 4.76, 3.12], [1.4, 4.54], [3.1, 4.5, 5]]
    >>> names = ["team1", "team2", "team3"]
    >>> average_rating_lists_names(ratings, names)
    'team3'

    >>> average_rating_lists_names([], [])
    ''
    """
    # YOUR CODE GOES HERE #
    total=0
    lst=[]
    if len(ratings) == 0:
        return ""
    for company in ratings:
        for rating in company:
            if rating <= 3.75:
                rating = 0
            total+=rating
        average=round(total/len(company), 2)
        lst.append(average)
        #reset the total count after each company's rating is calculated
        total = 0
    return names[lst.index(max(lst))]

# Question 8
def new_password(text, number, boolean):
    """
    Creates a password based on the given parameters: 
    text is reversed, numbers becomes either even or odd, boolean
    value is flipped.
    ---
    Parameters:
        text: a string
        number: an integer
        boolean: a boolean value 
    ---
    Returns:
        Password by concatenating altered components.

    >>> new_password(3, "is", True)
    'ERROR!'
    >>> new_password("paint", "is", False)
    'ERROR!'
    >>> new_password("paint", 40, 20)
    'ERROR!'
    >>> new_password("paint", 18, False)
    'tniap19True'
    >>> new_password("paint", 21, True)
    'tniap42False'
    """
    # YOUR CODE GOES HERE #
    #ensure all inputs are valid
    if type(text) == str and type(number) == int and type(boolean) == bool: 
        #reverse string with [::-1] (start at the last character, end at the first character, increment back by -1 each time)
        password = text[::-1]
        #change number
        if number % 2 == 0:
            number += 1
        else:
            number *= 2
        password+=str(number)
        password+=str(not boolean)
        return password
    else: 
        return 'ERROR!'
    

# Question 9
def colors_with_5(all_colors):
    """
    Finds the color names with 5 characters.
    --
    Parameters:
        all_colors: list of strings of color names
    --
    Returns:
        A list of color names fitting the criterion

    >>> all_colors = ["brown", "red", "green"]
    >>> colors_with_5(all_colors)
    ['brown', 'green']

    >>> all_colors = []
    >>> colors_with_5(all_colors)
    []

    >>> all_colors = ['red', 'blue', 'orange', 'teal']
    >>> colors_with_5(all_colors)
    []
    """
    # YOUR CODE GOES HERE #
    five_colors=[]
    for color in all_colors:
        if len(color) == 5:
            five_colors.append(color)

    return five_colors

# Question 10
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

