"""
DSC 20 Winter 2024 Homework 02
Name: Tom Zheng
PID: A18424137
Source: Google, Geeks4Geeks, Python Documentation, Claude 3.5 Sonnet (for \
    clarification and comprehension)
"""

# Question 1
def name_mapping(given_names, preferred_names):
    """
    Takes in two lists of names, given and preferred, then matches them into
    tuples outputed in a list. If there are not enough given names,
    the given names section is replaced by 'NO NAME PROVIDED'. Additionally,
    check if any of the strings in the lists are empty. If yes, demonstrate
    that in the tuple output.

    Parameters:
        given_names (list of str): The list of given names.
        preferred_names (list of str): The list of preferred names.

    Returns:
        mapped_names (list of tuple): A list of tuples where each tuple 
        contains a given name and a preferred name.

    >>> given_names = ['Amanda', 'Jeffrey', 'Richard']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('Richard', 'Rick')]

    >>> given_names = ['Amanda', 'Jeffrey']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('Amanda', 'Mandy'), ('Jeffrey', 'Jeff'), ('NO NAME PROVIDED', 'Rick')]

    >>> given_names = []
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('NO NAME PROVIDED', 'Mandy'), ('NO NAME PROVIDED', 'Jeff'), \
('NO NAME PROVIDED', 'Rick')]

    # Add at least 3 doctests below here #
    >>> given_names = ['', '', '']
    >>> preferred_names = ['Mandy', 'Jeff', 'Rick']
    >>> name_mapping(given_names, preferred_names)
    [('EMPTY STR', 'Mandy'), ('EMPTY STR', 'Jeff'), ('EMPTY STR', 'Rick')]

    >>> given_names = ['', '', 'Richard']
    >>> preferred_names = ['', 'Jeff', '']
    >>> name_mapping(given_names, preferred_names)
    [('EMPTY STR', 'EMPTY STR'), ('EMPTY STR', 'Jeff'), \
('Richard', 'EMPTY STR')]

    >>> given_names = []
    >>> preferred_names = []
    >>> name_mapping(given_names, preferred_names)
    []
    """
    mapped_names=[]
    i=0
    # check for empty strings in given names
    while i<len(given_names):
        if given_names[i] == '':
            given_names[i] = 'EMPTY STR'
        i+=1
    # reset index
    i=0
    # check for empty strings in preferred names
    while i<len(preferred_names):
        if preferred_names[i] == '':
            preferred_names[i] = 'EMPTY STR'
        i+=1
    # reset index
    i=0
    # iterate through the longest list (will always be preferred_names)
    while i<len(preferred_names):
        # if they are equal in len, just put the respective items into tuples
        if len(given_names) == len(preferred_names):
            mapped_names.append((given_names[i], preferred_names[i]))
            i+=1
        # if there aren't enough given names
        elif len(given_names) < len(preferred_names):
        # while index is still in the range of given_names, put in tuples
            if i<len(given_names):
                mapped_names.append((given_names[i], preferred_names[i]))
                i+=1
            # after index out of range, add 'NO NAME PROVIDED' to given_names
            elif i>=len(given_names):
                mapped_names.append(('NO NAME PROVIDED', preferred_names[i]))
                i+=1
    return mapped_names


# Question 2
def valid_pairs(keys, values):
    """
    Take in two lists of keys and values for a dictionary. Validates if each 
    item in key is a possible dictionary key. 

    Parameters:
        keys (list): A list of potential dictionary keys.
        values (list): A list of corresponding values.

    Returns:
        key_value_pairs (list of tuple): A list of key-value pairs where keys 
        are valid dictionary keys. If a key is invalid, it is replaced with the
        tuple ('not valid',).

    >>> keys = ["fun", ["not so much"]]
    >>> values = [("learning",), 6]
    >>> valid_pairs(keys, values)
    [('fun', ('learning',)), ('not valid',)]

    >>> keys = [1, "fun", [2], (1,), {}]
    >>> values = [1, {}, (1,), "island", [2]]
    >>> valid_pairs(keys, values)
    [(1, 1), ('fun', {}), ('not valid',), ((1,), 'island'), ('not valid',)]

    >>> keys =[]
    >>> values =[]
    >>> valid_pairs(keys, values)
    []

    # Add at least 3 doctests below here #
    >>> keys = ["valid", 42, True, (1, 2), [3, 4]]
    >>> values = [10, "answer", False, "tuple", "list"]
    >>> valid_pairs(keys, values)
    [('valid', 10), (42, 'answer'), (True, False), ((1, 2), 'tuple'), \
('not valid',)]

    >>> keys = ["key", None, {}, "another", (3.14,)]
    >>> values = ["value", "no value", "dict", "more", "pi"]
    >>> valid_pairs(keys, values)
    [('key', 'value'), ('not valid',), ('not valid',), ('another', 'more'), \
((3.14,), 'pi')]

    >>> keys = [(1, 2), "ok", 5.5, [], "done"]
    >>> values = ["tuple", "string", "float", "list", "end"]
    >>> valid_pairs(keys, values)
    [((1, 2), 'tuple'), ('ok', 'string'), (5.5, 'float'), ('not valid',), \
('done', 'end')]

    """
    # initialize output list
    key_value_pairs=[]
    # initialize counter
    i=0
    # dictionary keys must be immutable
    while i < len(keys):
        # check if each item in key is a possible dictionary key
        if type(keys[i]) in [int, float, str, bool, tuple]:
            # if yes, add the key with corresponding value in a tuple
            key_value_pairs.append((keys[i], values[i]))
            # otherwise, add the 'not valid' tuple
        else:
            key_value_pairs.append(('not valid',))
        # iterate counter
        i+=1

    return key_value_pairs


# Question 3
def dict_of_names(name_tuples):
    """
    Takes a list of tuples where each tuple contains a full name and a 
    nickname, and returns a dictionary where the keys are full names, and the 
    values are lists of associated nicknames.

    Parameters:
    name_tuples (list): A list of tuples, where each tuple has two strings -
                        a full name and a nickname.

    Returns:
    name_dict (dictionary): A dictionary where keys are full names, and values 
    are lists of nicknames.

    >>> dict_of_names([('Richard', 'Rick'),
    ... ('Roxanne', 'Rose'), ('Roxanne', 'Ann'),
    ... ('Richard', 'Ricky'), ('Roxanne', 'Roxie'),
    ... ('Mitchell', 'Mitch')])
    {'Richard': ['Rick', 'Ricky'], 'Roxanne': ['Rose', 'Ann', 'Roxie'], \
'Mitchell': ['Mitch']}

    >>> dict_of_names([('Melissa', 'Lisa'),
    ... ('Isabel', 'Bella'), ('NO NAME PROVIDED', 'Faith')])
    {'Melissa': ['Lisa'], 'Isabel': ['Bella'], \
'NO NAME PROVIDED': ['Faith']}

    >>> dict_of_names([('NO NAME PROVIDED', 'Derrick'), \
    ('NO NAME PROVIDED', 'Jacob')])
    {'NO NAME PROVIDED': ['Derrick', 'Jacob']}

    # Add at least 3 doctests below here #

    >>> dict_of_names([('NO NAME PROVIDED', 'Derrick'), \
    ('NO NAME PROVIDED', 'Jacob')])
    {'NO NAME PROVIDED': ['Derrick', 'Jacob']}

    >>> dict_of_names([('Alice', 'Ali'), ('Alice', 'Lace')])
    {'Alice': ['Ali', 'Lace']}

    >>> dict_of_names([])
    {}

    >>> dict_of_names([('Bob', 'Bobby'), ('Bob', 'Bob-O'), ('Bob', 'Bobby')])
    {'Bob': ['Bobby', 'Bob-O', 'Bobby']}
    """
    name_dict={}
    i=0
    for n_tuple in name_tuples:
        if name_tuples[i][0] not in name_dict:
            name_dict[name_tuples[i][0]]=[name_tuples[i][1]]
        elif name_tuples[i][0] in name_dict:
            name_dict[name_tuples[i][0]].append(name_tuples[i][1])
        i+=1
    return name_dict


# Question 4.1
def contractor_payment(suggestions):
    """
    Take in a list of lists which each contain the payments for each job for 
    each of the three contractors. Calculate the average of each contractor 
    across all contracts. Return the result as a dictionary

    Parameters:
    suggestions (list of lists): A list where each inner list contains three 
    values representing payments to each of the three contractors.

    Returns:
    averages_dict (dictionary): A dictionary where the keys are contractor 
    numbers ('1', '2', '3'), and the values are their average payments rounded
    to two decimal places.

    >>> contractor_payment([[10, 20, 30], [0, 20, 10]])
    {'1': 5.0, '2': 20.0, '3': 20.0}

    >>> contractor_payment([[10, 20, 30], [30, 20, 10], [5, 10, 15]])
    {'1': 15.0, '2': 16.67, '3': 18.33}

    >>> contractor_payment([[-5, -10, -4], [-20, 15, 40]])
    {'1': -12.5, '2': 2.5, '3': 18.0}

    # Add at least 3 doctests below here #
    >>> contractor_payment([[100, 200, 300]])
    {'1': 100.0, '2': 200.0, '3': 300.0}

    >>> contractor_payment([[10, 10, 10], [20, 20, 20], [30, 30, 30]])
    {'1': 20.0, '2': 20.0, '3': 20.0}

    >>> contractor_payment([])
    {}

    >>> contractor_payment([[0, 0, 0], [0, 0, 0]])
    {'1': 0.0, '2': 0.0, '3': 0.0}
    """
    # initialize the totals for each contractor
    sum1 = 0
    sum2 = 0
    sum3 = 0
    # edge case for when no suggestions are inputted
    if len(suggestions) == 0:
        return {}
    
    # iteratively add up the totals for each contractor across all jobs
    for three_contractors in suggestions:
        sum1+=three_contractors[0]
        sum2+=three_contractors[1]
        sum3+=three_contractors[2]
    
    # calculate the average of all jobs for each contractor
    avg_1 = round(sum1/len(suggestions), 2)
    avg_2 = round(sum2/len(suggestions), 2)
    avg_3 = round(sum3/len(suggestions), 2)

    # place averages into dictionary and return
    averages_dict = {'1': avg_1,'2': avg_2,'3':avg_3}
    return averages_dict

# Question 4.2
def new_pay(hours):
    """
    Take in a dictionary of three contractors and the amount of hours they 
    worked. Check if any of the hours are less than expected. If yes, return
    an automatic -10 penalty and set the pay to Penalty. Otherwise, evaluate
    the conditions for the hours they worked and decide on the result of the 
    pay.

    Parameters:
        hours (dict): A dictionary containing the hours worked by three 
        contractors. Values are integers or floats

    Returns:
        bonus_pay or penalty (float): The calculated bonus pay or penalty. 
        If any contractor has worked negative hours, the function returns -10 
        and sets the 'pay' key in the input dictionary to 'Penalty'.
               Otherwise:
               - Bonus: If bonus_pay > 0
               - Penalty: If bonus_pay < 0
               - No: If bonus_pay == 0

    >>> case1 = {'1': 200, '2': 138, '3': 172}
    >>> round(new_pay(case1), 2)
    0.51
    >>> case1
    {'1': 200, '2': 138, '3': 172, 'pay': 'Bonus'}

    >>> case2 = {'1': 130, '2': 84, '3': -14}
    >>> new_pay(case2)
    -10
    >>> case2
    {'1': 130, '2': 84, '3': -14, 'pay': 'Penalty'}

    >>> case3 = {'1': 42, '2': 96, '3': 63}
    >>> round(new_pay(case3), 1)
    -2.4
    >>> case3
    {'1': 42, '2': 96, '3': 63, 'pay': 'Penalty'}

    # Add at least 3 doctests below here #
     >>> case4 = {'1': 0, '2': 0, '3': 0}
    >>> new_pay(case4)
    -5.0
    >>> case4
    {'1': 0, '2': 0, '3': 0, 'pay': 'Penalty'}

    >>> case5 = {'1': 500, '2': 400, '3': 300}
    >>> round(new_pay(case5), 2)
    10.0
    >>> case5
    {'1': 500, '2': 400, '3': 300, 'pay': 'Bonus'}

    >>> case6 = {'1': 100, '2': 100, '3': 100}
    >>> round(new_pay(case6), 2)
    -2.5
    >>> case6
    {'1': 100, '2': 100, '3': 100, 'pay': 'Penalty'}
    """
    penalty = -10
    if hours['1'] < 0 or hours['2'] < 0 or hours['3'] < 0:
        hours['pay'] = 'Penalty'
        return penalty
    hours_by_contractor1 = hours['1']
    hours_by_contractor2 = hours['2']
    hours_by_contractor3 = hours['3']
    bonus_pay = (0.01 * hours_by_contractor1 + 0.015 * hours_by_contractor2 
                 + min(0.02 * abs(100 - hours_by_contractor3), 0.025 \
                       * hours_by_contractor3) - 5)
    
    if bonus_pay < 0:
        result='Penalty'
    elif bonus_pay > 0:
        result='Bonus'
    else:
        result = 'No'
    hours['pay'] = result
    return bonus_pay

# Question 5
def potential_ideas_for_business(items):
    """
    For each supplier, check the ingredients that they have. If they are not
    in our products list, add them. If they are already, ignore them. Iterate
    through this for each supplier and for each ingredient. 

    Parameters: 
        items (dict): A dictionary where keys are supplier names (strings) and 
        values are lists of ingredients (strings) provided by that supplier.
    
    Returns:
        list: An alphabetically sorted list of unique ingredients (strings) 
        from all suppliers.
    
    >>> items = {'supplier 1': ['Tea', 'Peaches'], \
    'supplier 2': ['Peaches', 'Apples', 'Cups']}
    >>> potential_ideas_for_business(items)
    ['Apples', 'Cups', 'Peaches', 'Tea']

    >>> items = {'supplier 1': ['Flour', 'Eggs', 'Chocolate', 'Milk'], \
    'supplier 2': ['Milk', 'Eggs', 'Vanilla', 'Butter'], \
    'supplier 3': ['Butter', 'Sugar']}
    >>> potential_ideas_for_business(items)
    ['Butter', 'Chocolate', 'Eggs', 'Flour', 'Milk', 'Sugar', 'Vanilla']

    >>> items = {'supplier 1': [], 'supplier 2': []}
    >>> potential_ideas_for_business(items)
    []

    >>> items = {'supplier 1': ['Salt'], 'supplier 2': ['Salt']}
    >>> potential_ideas_for_business(items)
    ['Salt']

    >>> items = {'supplier 1': [], 'supplier 2': ['Honey']}
    >>> potential_ideas_for_business(items)
    ['Honey']

    >>> items = {}
    >>> potential_ideas_for_business(items)
    []
    """
    products=[]
    for supplier in items:
        i=0
        while i<len(items[supplier]):
            if items[supplier][i] not in products:
                products.append(items[supplier][i])
            i+=1
    
    return sorted(products)

# Question 6.1
def count_lines_1(filepath):
    """
    Open the file from the filepath to be readable. Then, reads line by line
    and adds one to the count for every line.

    Parameters:
    filepath (str): The path to the file to be read.

    Returns:
    line_count (int): The number of lines in the file.

    >>> count_lines_1('files/test1.txt')
    6
    >>> count_lines_1('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    >>> count_lines_1('files/offices2.txt')
    4
    >>> count_lines_1('files/offices1.txt')
    3
    >>> count_lines_1('files/empty_trip.txt')
    0

    """
    line_count = 0
    with open(filepath, 'r') as file:
        for line in file:
            line_count += 1
    return line_count


# Question 6.2
def count_lines_2(filepath):
    """
    Open the file in read mode, then read the file. After, split the lines into
    a list and count the length of the list.

    Parameters:
    filepath (str): The path to the file to be read.

    Returns:
    line_count (int): The number of lines in the file.

    >>> count_lines_2('files/test1.txt')
    6
    >>> count_lines_2('files/test2.txt')
    24

    # Add at least 3 doctests below here #

    >>> count_lines_2('files/offices2.txt')
    4
    >>> count_lines_2('files/offices1.txt')
    3
    >>> count_lines_2('files/empty_trip.txt')
    0
    
    The 3 tests above have files with empty lines at the end, so read and then
    splitting will count all lines regardless of whether there is text or not.
    """
    with open(filepath, 'r') as file:
        text = file.read()
        # better than splitting with \n but fails with trailing newlines. 
        lines = text.splitlines()
    return len(lines)


# Question 6.3
def count_lines_3(filepath):
    """
    Open the file in read mode, then read the file. Count the number of lines
    in the file and return the lines into a list and return the length of the 
    list.

    Parameters:
    filepath (str): The path to the file to be read.

    Returns:
    line_count (int): The number of lines in the file.

    >>> count_lines_3('files/test1.txt')
    6
    >>> count_lines_3('files/test2.txt')
    24

    # Add at least 3 doctests below here #
    >>> count_lines_3('files/offices2.txt')
    4
    >>> count_lines_3('files/offices1.txt')
    3
    >>> count_lines_3('files/empty_trip.txt')
    0
    """
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return len(lines)


# Question 7
def collected_items(filepath):
    """
    Reads a file containing lines of comma-separated values, extracts the 
    third column ("item"), and returns a list of these items. Skips empty 
    lines and lines with fewer than three elements.

    Parameters:
        filepath (str): The path to the file to process.

    Returns:
        items (list): A list of strings representing the extracted items.
    
    >>> collected_items('files/ings1.txt')
    ['ice-cream', 'boba tea', 'fish']
    >>> collected_items('files/ings2.txt')
    ['shovel', 'headphones', 'bird', 'brownies']
    >>> collected_items('files/empty_trip.txt')
    []

    # Add at least 3 doctests below here #
    >>> collected_items('files/single_line.txt')
    ['novel']
    >>> collected_items('files/extra_columns.txt')
    ['cereal', 'soda']
    >>> collected_items('files/malformed_lines.txt')
    ['flowers', 'tools', 'vegetables']
    """
    items=[]
    position_of_item = 2
    least_length = 3
    with open(filepath, 'r') as file:
        for line in file:
            line=line.strip()
            if line:
                parts=line.split(',')
                if len(parts)<least_length:
                    continue
                else:
                    items.append(parts[position_of_item])

    return items


# Question 8
def case_letters(filepath):
    """
    Count up each capital and lower letter in the filepath name. Write these
    counts into the file itself.

    Parameters:
        filepath (str): The path to the file to process.

    Returns:
        the function itself doesn't return anything, however it writes in the
        target filepath.

    >>> case_letters('files/AlErNaTiNg.txt')
    >>> with open('files/AlErNaTiNg.txt', 'r') as outfile1:
    ...    print(outfile1.read().strip())
    5
    13
    >>> case_letters('files/another_test.txt')
    >>> with open('files/another_test.txt', 'r') as outfile2:
    ...    print(outfile2.read().strip())
    0
    19

    # Add at least 3 doctests below here #
    >>> case_letters('files/@(234@).txt')
    >>> with open('files/@(234@).txt', 'r') as outfile3:
    ...    print(outfile3.read().strip())
    0
    8

    >>> case_letters('files/ALL_UPPERCASE.txt')
    >>> with open('files/ALL_UPPERCASE.txt', 'r') as outfile4:
    ...    print(outfile4.read().strip())
    12
    8

    >>> case_letters('files/all_lowercase.txt')
    >>> with open('files/all_lowercase.txt', 'r') as outfile5:
    ...    print(outfile5.read().strip())
    0
    20
    """
    
    upper_count=0
    lower_count=0
    for letter in filepath:
        if letter.isupper() and letter.isalpha():
            upper_count+=1
        elif letter.islower() and letter.isalpha():
            lower_count+=1
    
    with open(filepath, 'w') as file:
        file.write(f"{upper_count}\n{lower_count}")
    return 


# Question 9
def map_office(filepath):
    """
    Maps office numbers to their corresponding floor descriptions
    and writes these mappings to a file. Additionally, calculates
    and returns the sum of all valid office numbers.

    Mapping rules:
    - Less than 1: "not a valid office number"
    - Between 1 and 199 (inclusive): "ground floor"
    - Between 200 and 299 (inclusive): "second floor"
    - Above 300: "third floor and above"

    Parameters:
        filepath (str): Path to the input file containing office numbers.

    Returns:
        count (int): The sum of all valid office numbers.
    
    >>> map_office('files/offices1.txt')
    259
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    ground floor
    not a valid office number
    second floor

    >>> map_office('files/offices2.txt')
    734
    >>> with open('files/floors.txt', 'r') as f:
    ...    print(f.read().strip())
    third floor and above
    not a valid office number
    second floor
    ground floor

    >>> map_office('files/offices3.txt')
    0
    >>> with open('files/floors.txt', 'r') as f:
    ...     print(f.read().strip())
    not a valid office number
    not a valid office number
    not a valid office number

    >>> map_office('files/offices4.txt')
    100
    >>> with open('files/floors.txt', 'r') as f:
    ...     print(f.read().strip())
    ground floor

    >>> map_office('files/offices5.txt')
    999
    >>> with open('files/floors.txt', 'r') as f:
    ...     print(f.read().strip())
    third floor and above
    ground floor
    second floor
    """
    count = 0
    with open(filepath, 'r') as file:
        office_numbers = file.readlines()
        with open('files/floors.txt', 'w') as f:
            for line in office_numbers:
                number = int(line.strip())
                if number < 1:
                    result = 'not a valid office number'
                elif number <= 199:
                    result = 'ground floor'
                    count += number
                elif number <= 299:
                    result = 'second floor'
                    count += number
                else:   
                    result = 'third floor and above'
                    count += number
                f.write(f'{result}\n')
    return count


