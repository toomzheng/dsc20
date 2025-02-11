"""
DSC 20 Winter 2025 Homework 05
Name: Tom Zheng
PID: A18424137
Source: TODO
"""

# Question 1

def get_qualified_customers(data, max_avg, min_range):
    """
    Takes in a list of customers and determines which ones are qualified.
    Criteria:
        The average score should be less than or equal to a specified max_avg.
        The range (difference between the largest and smallest score) should \
            be greater than or equal to a specified min_range.
        There should be no duplicate scores in the list.


    Args:
        data (dict): Dictionary where keys are customer IDs and values are
        scores representing their metrics
        max_avg (int): Maximum allowed average for the scores
        min_rage (int): Minimum required range for all scores

    Returns:
        list: A list of costumer names that meet all the criteria

    >>> data = { \
        "Jayden": [10, 10, 10, 10, 10], \
        "Terry": [1, 2, 3, 4, 5, 6, 7, 8], \
        "Austin": [10, 11, 12, 13, 14], \
        "Noah": [2, 3, 4, 5] \
    }
    >>> get_qualified_customers(data, 11, 5)
    ['Terry']

    >>> data = { \
        "Caleb": [0, 1, 2, 3, 4, 5], \
        "Keenan": [8, 9, 10], \
        "Rome": [7, 8, 9], \
        "Khalil": [] \
    }
    >>> get_qualified_customers(data, 9, 2)
    ['Caleb', 'Keenan', 'Rome']

    # Add at least 3 doctests below here #
    >>> data = {}
    >>> get_qualified_customers(data, 10, 5)
    []

    >>> data = { \
        "Alice": [], \
        "Bob": [] \
    }
    >>> get_qualified_customers(data, 10, 5)
    []

    >>> data = { \
        "Eve": [5, 5, 5, 5, 5], \
        "Mallory": [7, 7, 7, 7] \
    }
    >>> get_qualified_customers(data, 8, 1)
    []

    >>> data = { \
        "Zara": [2, 3, 4, 5, 6], \
        "Yara": [1, 2, 3, 4, 5], \
        "Lara": [1, 2, 3, 4, 50] \
    }
    >>> get_qualified_customers(data, 15, 10)
    ['Lara']
    """
    # checks
    assert isinstance(data, dict)
    assert all(isinstance(key, str) for key in data)
    assert all(isinstance(data[key], list) for key in data)
    assert all(isinstance(num, int) for key in data for num in data[key])
    assert isinstance(max_avg, int)
    assert isinstance(min_range, int)

    rng = lambda x: max(x) - min(x) if x else 0
    avg = lambda y: sum(y) / len(y) if y else 0

    return [key for key in data if rng(data[key]) >= min_range \
            and avg(data[key]) <= max_avg and \
                len(set(data[key])) == len(data[key])]

# Question 2

def message_to_customers(customer_file, decision, message):
    """
    Sends a mesage to customers based on their decision in a text file

    Args:
        customer_file (str): Path to customer file
        decision (str): Decision code to filter customers
        message (str): Message that is sent to qualified customers

    Returns:
        list: A list of formatted messages based on the decision and message

    >>> msg = "unfortunately we cannot work with you."
    >>> message_to_customers("files/customers.txt", "w", msg)
    ['(to: steve@apple.com) Dear Steve at Apple, \
unfortunately we cannot work with you.', \
'(to: jensen@nvidia.com) Dear Jensen at NVIDIA, \
unfortunately we cannot work with you.']

    >>> msg = "we are excited to work with you!"
    >>> message_to_customers("files/customers.txt", "s", msg)
    ['(to: jeff@amazon.com) Dear Jeff at Amazon, \
we are excited to work with you!', \
'(to: mark@fb.com) Dear Mark at Facebook, \
we are excited to work with you!']

    # Add at least 3 doctests below here #
    >>> msg = "thank you for your patience."
    >>> message_to_customers("files/empty_customers.txt", "w", msg)
    []

    >>> msg = "thank you for waiting."
    >>> message_to_customers("files/no_matching_customers.txt", "w", msg)
    []

    >>> msg = "welcome to the team!"
    >>> message_to_customers("files/missing_fields.txt", "s", msg)
    ['(to: steve@apple.com) Dear Steve at Apple, welcome to the team!']
    
    """
    assert isinstance(customer_file, str) 
    assert isinstance(decision, str)
    assert isinstance(message, str)

    final_message = []
    decision_index = 3
    email_index = 2
    name_index = 1
    company_index = 0
    with open(customer_file, 'r') as file:
        for line in file:
            # .strip() removes new_line characters
            split_line = line.strip().split(',')
            # check that all values exist
            if split_line[decision_index] == decision \
                and split_line[email_index].strip() \
                    and split_line[name_index].strip() \
                    and split_line[company_index].strip():
                final_message.append(f'(to: {split_line[email_index]}) \
Dear {split_line[name_index]} \
at {split_line[company_index]}, \
{message}')
                
    return final_message


# Question 3

def forge_votes(vote_file):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> forge_votes("files/vote1.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Patrick,1
    Travis,0
    Clyde,1
    Andy,1

    >>> forge_votes("files/vote2.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Maxx,1
    Tre,1
    Jakobi,0

    >>> forge_votes("files/vote3.txt")
    >>> with open("files/forged.txt", "r") as out:
    ...    for line in out:
    ...       print(line.strip())
    Andy,1

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    


# Question 4

def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
    function. No new doctests required.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (True/False) #
    return [..., ..., ..., ..., ..., ..., ..., ..., ..., ...]