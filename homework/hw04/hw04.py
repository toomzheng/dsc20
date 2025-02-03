"""
DSC 20 Winter 2025 Homework 04
Name: Tom Zheng
PID: A18424137
Source: Claude 3.5 Sonnet for explanations and guidance
"""

# Question 1
def place_of_birth(file_in):
    """
    Reads a file containing players' names, citise, and dates of birth. 
    Creates a dictionary and cleans up extra spaces, where the keys are 
    city names, and the values are lists of people born there.

    Args:
        file_in (str): Path to .txt file with player data

    Returns:
        dct (dict): A dictionary with keys a city names and values as lists
        of people born there.

    >>> place_of_birth('files/info_1.txt')
    {'Chicago': ['Rob'], 'New York': ['Ella'], 'New York.': ['Mary']}
    >>> place_of_birth('files/info_2.txt')
    {'Chicago': ['Rob'], 'London': ['Ezra'], 'Paris': \
['Mary'], 'paris': ['Ron', 'Harry']}
    >>> place_of_birth('files/header.txt')
    {}

    # Add at least 3 doctests below here #
    >>> place_of_birth('files/mixed_case.txt')
    {'Los Angeles': ['Jake'], 'los angeles': ['Emma']}
    >>> place_of_birth('files/trailing_spaces.txt')
    {'Boston': ['Olivia'], 'Newark': ['Mason']}
    >>> place_of_birth('files/extra_whitespace.txt')
    {'Chicago': ['Alice'], 'San Francisco': ['Bob']}
    """
    city_of_birth = {}
    with open(file_in, 'r') as file:
        next(file) # skip the first line
        for line in file:
            # strip the whitespace from the ends of each word in the list
            line_list = [word.strip() for word in line.split(',')]
            if line_list[1] not in city_of_birth:
                city_of_birth[line_list[1]] = [line_list[0]]
            else:
                city_of_birth[line_list[1]].append(line_list[0])
    return city_of_birth



# Question 2
def age_groups(file_in, file_out):
    """
    Reads a file containing players' names, cities, and dates of birth.
    Cleans up extra spaces and writes in a new file, categorizing each person
    based on age relative to 35 years.

    Args:
        file_in (str): Path to the file with players info to be read
        file_out (str): Path to the file which will be written in

    Returns:
        None: Writes the categorized data into the files.

    >>> age_groups('files/info_1.txt', 'files/age_1_out.txt')
    >>> with open('files/age_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ella,1
    Mary,-1
    
    >>> age_groups('files/info_2.txt', 'files/age_2_out.txt')
    >>> with open('files/age_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,older than 35
    Rob,-1
    Ezra,1
    Mary,1
    Ron,0
    Harry,0

    >>> age_groups('files/header.txt', 'files/empty_out.txt')
    >>> with open('files/empty_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35

    # Add at least 3 doctests below here #

    >>> age_groups('files/mixed_dates.txt', 'files/mixed_dates_out.txt')
    >>> with open('files/mixed_dates_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35
    Jake,-1
    Emma,0
    Noah,1
    
    >>> age_groups('files/extra_whitespace2.txt', \
        'files/extra_whitespace2_out.txt')
    >>> with open('files/extra_whitespace2_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35
    Alice,1
    Bob,-1
    >>> age_groups('files/edge_case_birthdays.txt', \
        'files/edge_case_birthdays_out.txt')
    >>> with open('files/edge_case_birthdays_out.txt', \
        'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35
    Liam,-1
    Sophia,-1
    Oliver,1
    """
    current_year = 2024
    required_age = 35
    date_index = 2
    year_index = 2
    name_index = 0
    # open the file to be read
    with open(file_in, 'r') as file:
        # skip the first line of reading
        next(file)
        # open the file to be written in
        with open(file_out, 'w') as f:
            # write the header
            f.write('name,older than 35')
            # loop through each line in the file being read
            for line in file:
                # strip the words for each word in a list created by commas
                new_line = [word.strip() for word in line.split(',')]
                # split the year month date by backslash and take the year 
                year = int(new_line[date_index].split('/')[year_index])
                # control flow to determine their age relative to 35.
                if current_year-year < required_age:
                    f.write(f'\n{new_line[name_index]},-1')
                elif current_year-year == required_age:
                    f.write(f'\n{new_line[name_index]},0')
                else:
                    f.write(f'\n{new_line[name_index]},1')
    return
                

# Question 3
def several_files(files_lst, file_out):
    """
    Reads multiple files containing player information, cleans data, and writes
    formatted content to a single output file.

    Args:
        files_lst (list): list of file paths with information to be read
        file_out (str): filepath of file to be written in with new info
    
    Returns:
        None: writes the processed data into the output files

    >>> lst_1 = ['files/info_1.txt','files/info_3.txt', 'files/info_4.txt']
    >>> several_files(lst_1, 'files/several_1_out.txt')
    >>> with open('files/several_1_out.txt', 'r') as outfile1:
    ...    for line in outfile1:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ella,New York,Apr 09 1970
    Mary,New York.,Jan 01 2004
    Sue,San Diego,Mar 19 2015
    Ben,London,Dec 08 1970
    Kate,Paris,Jul 13 1945

    >>> lst_2 = ['files/info_2.txt','files/header.txt']
    >>> several_files(lst_2, 'files/several_2_out.txt')
    >>> with open('files/several_2_out.txt', 'r') as outfile2:
    ...    for line in outfile2:
    ...       print(line.strip())
    name,city,DOB
    Rob,Chicago,Oct 10 2010
    Ezra,London,Apr 12 1978
    Mary,Paris,Sep 11 1975
    Ron,paris,Nov 11 1989
    Harry,paris,Dec 15 1989

    # Add at least 3 doctests below here #

    >>> lst_3 = ['files/mixed_dates.txt', 'files/edge_case_birthdays.txt']
    >>> several_files(lst_3, 'files/several_3_out.txt')
    >>> with open('files/several_3_out.txt', 'r') as outfile3:
    ...    for line in outfile3:
    ...       print(line.strip())
    name,city,DOB
    Jake,New York,Jun 15 2000
    Emma,Los Angeles,Dec 30 1989
    Noah,Chicago,May 20 1985
    Liam,Boston,Jan 01 2024
    Sophia,Miami,Jul 07 2025
    Oliver,Seattle,May 25 0

    >>> lst_4 = ['files/extra_whitespace.txt']
    >>> several_files(lst_4, 'files/several_4_out.txt')
    >>> with open('files/several_4_out.txt', 'r') as outfile4:
    ...    for line in outfile4:
    ...       print(line.strip())
    name,city,DOB
    Alice,Chicago,May 30 1985
    Bob,San Francisco,Nov 22 1990
    
    >>> lst_5 = ['files/edge_case_birthdays.txt']
    >>> several_files(lst_5, 'files/several_5_out.txt')
    >>> with open('files/several_5_out.txt', 'r') as outfile5:
    ...    for line in outfile5:
    ...       print(line.strip())
    name,city,DOB
    Liam,Boston,Jan 01 2024
    Sophia,Miami,Jul 07 2025
    Oliver,Seattle,May 25 0
    """
    # create helper dictionary
    help_dct = {'12': 'Dec', '11': 'Nov', '10': 'Oct', '9': 'Sep', \
                '8':'Aug', '7':'Jul', '6': 'Jun', '5': 'May', '4': 'Apr', \
                    '3': 'Mar', '2': 'Feb', '1': 'Jan'}
    # open file to be written
    with open(file_out, 'w') as f_out:
        # write out the header
        f_out.write('name,city,DOB')
        # open each file in files_lst to be read
        for file in files_lst:
            # open each one in read mode
            with open(file, 'r') as f:
                # skip the header
                next(f)
                # go through each line in the file
                for line in f:
                    # create a tuple from each line after cleaning
                    (name, city, dob) = [word.strip() for word in \
                                         line.split(',')]
                    # create another tuple from dob
                    (month, date, year) = dob.split('/')
                    # format the dob, and make sure months of 09 and 9 are
                    # treated the same
                    formatted = \
                        f"{help_dct[str(int(month))]} {date} {int(year)}"
                    # put the formatted dob into a new list with name and city
                    processed_line = [f"{name},{city},{formatted}"]
                    # write the new list as a line on file_out
                    f_out.write(f"\n{','.join(processed_line)}")


# Question 4
def postcards(info_list):
    """
    Generates personalized postcards for individuals whose price is strictly 
    lower than 75.

    Args:
        info_list (list): A list of tuples where each tuple contains:
            - name (str): First and last name separated by a space
            - price (int): Non-negative integer
            - age (int): Non-negative integer
            - place (str): Name of the place
    
    Returns:
        dict: A dictionary where keys are names and values are formatted 
        postcards.

    >>> postcards([
    ...     ('Yue Wang', 96, 18, 'Hoover Dam'),
    ...     ('Cleo Patra', 10, 32, 'Bellagios')
    ... ])
    {'Cleo Patra': 'cle32patra0soigalleb'}
    >>> postcards([])
    {}
    >>> postcards([
    ...     ('Mari Noh', 155, 18, 'tram'),
    ...     ('Gwen Am', 34, 54, 'Venetian'),
    ...     ('Freya Dog', 34, 1, 'The Strip')
    ... ])
    {'Gwen Am': 'gwe54am4naitenev', 'Freya Dog': 'fre1dog4pirts eht'}

    # Add at least 3 doctests below here #
    >>> postcards([
    ...     ('Leo Sky', 45, 27, 'Eiffel Tower'),
    ...     ('Anna Belle', 30, 33, 'Golden Gate')
    ... ])
    {'Leo Sky': 'leo27sky5rewot leffie', 'Anna Belle': 'ann33belle0etag \
nedlog'}
    
    >>> postcards([
    ...     ('Eve Adams', 75, 40, 'Statue of Liberty')
    ... ])
    {}
    
    >>> postcards([
    ...     ('Zo Eve', 60, 22, 'Colosseum')
    ... ])
    {'Zo Eve': 'zo22eve0muessoloc'}
    """
    assert isinstance(info_list, list), "Input must be a list."
    assert all(isinstance(item, tuple) and len(item) == 4 \
               for item in info_list)
    assert all(isinstance(item[0], str) and ' ' in item[0] \
               for item in info_list)
    assert all(isinstance(item[1], int) and item[1] >= 0 \
               for item in info_list)
    assert all(isinstance(item[2], int) and item[2] >= 0 for item in info_list)
    assert all(isinstance(item[3], str) for item in info_list)

    up_to_first_three = 3
    division_by_10_for_10s_digit = 10
    price_index = 1
    age_index = 2
    place_index = 3
    price_threshold = 75
    filtered = filter(lambda x: x[1] < price_threshold, info_list)
    postcard_tuples = map(lambda x: (
            x[0],  # full name as key
            (  # concatenate all parts for postcard value
                # first three letters of first name
                x[0].split()[0][:up_to_first_three].lower()
                # add the age
                + str(x[age_index])
                # get the last name
                + x[0].split()[1].lower()
                # get last digit of price
                + str(x[price_index] % division_by_10_for_10s_digit) 
                # reversed place
                + x[place_index][::-1].lower()
            )
        ), filtered)
    return dict(postcard_tuples)


# Question 5
def win_or_lose(initial_scores, operations):
    """
    Applies a sequence of operations on a given list of integers which 
    represent the scores of teams in competition

    Args:
        lst (list): A list of ints representing initial scores
        operations (list): A list of tuples containing operations and values
    
    Returns:
        list or str: Transformed list after applying the operations or possibly
        a final string for game over


    >>> lst = [1, 12, 123, 1234, 12345, 123456]
    >>> operations_1 = [('advance', 5), ('lost', 3), ('tie', 4)]
    >>> win_or_lose(lst, operations_1)
    [14, 125, 1236, 12347, 123458]

    >>> operations_2 = [('lost', 200), ('eliminate', 'Team ')]
    >>> win_or_lose(lst, operations_2)
    ['Team lost', 'Team lost', 'Team lost', 'Team won', 'Team won', 'Team won']

    # Add at least 3 doctests below here #
    >>> lst_5 = [50, 100, 150]
    >>> operations_5 = [('lost', 20), ('advance', 10), ('tie', 60)]
    >>> win_or_lose(lst_5, operations_5)
    [90, 140]
    
    >>> lst_6 = [3, 7, 14, 21, 28]
    >>> operations_6 = [('tie', 10), ('win', 'Final Score: ')]
    >>> win_or_lose(lst_6, operations_6)
    'Final Score: 63'
    
    >>> lst_7 = [200, 400, 600]
    >>> operations_7 = [('lost', 500), ('eliminate', 'Game Over: ')]
    >>> win_or_lose(lst_7, operations_7)
    ['Game Over: lost', 'Game Over: lost', 'Game Over: won']
    
    >>> lst_8 = [10, 20, 30]
    >>> operations_8 = [('tie', 50)]
    >>> win_or_lose(lst_8, operations_8)
    []

    >>> lst_9 = []
    >>> operations_9 = [('tie', 50)]
    >>> win_or_lose(lst_9, operations_9)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> lst_10 = [21, 12039, 123812931823189231]
    >>> operations_10 = [(50)]
    >>> win_or_lose(lst_10, operations_10)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    # check lst is a list
    assert isinstance(initial_scores, list) 
    # check all values in list are integers
    assert all(isinstance(i, int) for i in  initial_scores)
    # make sure list isn't empty
    assert len(initial_scores) > 0
    # make sure operations is a list
    assert isinstance(operations, list) 
    # make sure that all items in operations are tuples and are of length 2
    assert all(isinstance(op, tuple) and len(op) == 2 for op in operations)
    # check all operations are valid
    valid_operations = {'advance', 'lost', 'tie', 'eliminate', 'win'}
    assert all(op[0] in valid_operations for op in operations)
    # ensure all operations are either strings or ints
    assert all(isinstance(op[1], (int, str)) for op in operations)
    commands = {
            # maps amount onto every value (x) in list
            'advance': lambda initial_scores, amount: list(map(\
                lambda x: x + amount, initial_scores)), 
            # maps -amount onto every value (x) in list
            'lost': lambda  initial_scores, amount: \
                list(map(lambda x: x - amount, initial_scores)),
            # filters out the values in list that aren't greater than threshold
            'tie': lambda   initial_scores, threshold: list(filter(\
                lambda x: x >= threshold, initial_scores)),
            # add the symbol given and won or less depending on x
            'eliminate':  lambda initial_scores, symbol: list(\
                map(lambda x: symbol\
                    + ('won' if x > 0 else 'lost'), initial_scores)),
            # computes sum of all numbers in initial_scores and adds to msg
            'win': lambda initial_scores, message: message \
                + str(sum(initial_scores)),
    }
    # iterates through tuples in operation
    for operation, value in operations:
        # goes through each value in operations list
        initial_scores = commands[operation](initial_scores, value)
    return  initial_scores
