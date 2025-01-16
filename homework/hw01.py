"""
DSC 20 Winter 2025 Homework 01
Name: Tom Zheng
PID: A18424137
"""
# Question 1
def login(fname, lname):
    
    """
    Reverse fname and take every other character with [::2], this means 
    removing all odd indexed characters (since we're starting from index 0, 
    index 1 is removed)
    
    Take every third character with [::3] (start with the first character and
    take every third one character after that)

    >>> login("Marina", "Langlois")
    'aiaLgi'
    >>> login("", "")
    ''
    >>> login("San", "Diego")
    'nSDg'

    # Add your own doctests below
    >>> login("Tom", "")
    'mT'
    >>> login(42, "Zheng")
    'At least one entry is not a string'
    >>> login("", "Zheng")
    'Zn'
    >>> login(True, False)
    'At least one entry is not a string'
    
    """
    # for this question and the next, I added these checks, though for future 
    # questions they are assumed as their types are stated in the problems.
    # check that both parameters are strings
    if type(fname) == type(lname) == str:
        # reverse first name
        temp_fname=fname[::-1]
        # initialize login
        login = ""
        # loop through fname and get every third character 
        new_fname = temp_fname[::2]
        
        new_lname=lname[::3]
        login = new_fname + new_lname
        return login
    else:
        return "At least one entry is not a string"


# Question 2
def ages(age1, age2):
    """
    Check if either both ages are greater than 23, one is greater and one isn't
    (print the one that isn't), or if both aren't (print the lower age)

    >>> ages(19, 21)
    21
    >>> ages(26, 21)
    21
    >>> ages(26, 27)
    'You both can rent!'
    >>> ages(19, 23)
    19
    >>> ages(0, 0)
    0
    >>> ages(-12, -23)
    'At least one entry is not a positive integer!'
    >>> ages("hello", "world")
    'At least one entry is not an age!'
    >>> ages('',1)
    'At least one entry is not an age!'
    """
    # check that both ages are positive
    # check that both age parameters are integers
    if type(age1) == type(age2) == int:
        # check both ages are positive (only do this after checking if int)
        if age1 < 0 or age2 < 0 or (age1 < 0 and age2 < 0):
            return 'At least one entry is not a positive integer!'
        elif age1 >= 23 and age2 >= 23:
            return 'You both can rent!'
        elif age1 < 23 and age2 >= 23 or age2 < 23 and age1 >= 23:
            return min(age1, age2)
        else:
            return max(age1, age2)
    else:
        return 'At least one entry is not an age!'


# Question 3
def renter(name1, name2, name3):
    """
    Put each of the name parameters into a list and reverse their order. This
    is so that if multiple names have the same length, we always take the last
    possible name, which when reversed results in the first possible name.
    
    Create a for-loop to iterate through the list of names and check the length
    of each name. If it is bigger, replace the longest length and keep note of
    that name. Finally, return the longest name.

    >>> renter("K", "BB", "Joy")
    'Joy'
    >>> renter("Joy", "K", "BB")
    'Joy'
    >>> renter("BB", "Joy", "K")
    'Joy'
    >>> renter("BB", "K", "Jo")
    'Jo'
    >>> renter("BB", "Jo", "Su")
    'Su'

    # Add your own doctests below
    >>> renter("", "", "")
    ''
    >>> renter("120391283", "hello", "")
    '120391283'
    >>> renter("Tom Zheng", "Matt Li", "Montre Ward")
    'Montre Ward'
    """
    # reverse the list so we can take the first instance of the longest name #
    reversed_names = [name3, name2, name1]
    # initialize our "longest" variable to be -1 to account for empty strings
    longest = -1
    # the problem indicates string inputs, no need to worry about other types
    for name in reversed_names:
        if len(name) > longest:
            longest = len(name)
            longest_name = name
    return longest_name


# Question 4.1
def helper_distance(lst, x2, y2):
    """
    We let x1, y1 be the lst coordinates and x2, y2 be the given starting 
    points. The formula for the distance between two points in a Euclidean 
    plane is given by sqrt((x2-x1)^2+(y2-y1)^2). We write out the formula in 
    python and return its value.
    
    >>> helper_distance([0, 0], 3, 4)
    5.0
    >>> helper_distance([-3, -4], 3, 4)
    10.0
    >>> helper_distance([100, 100], 100.5, 100)
    0.5
    
    # Add your own doctests below
    >>> helper_distance([1, 1], 1, 1)
    0.0
    >>> helper_distance([2,4], 3, 2)
    2.236
    >>> helper_distance((0.2, 0.4), 0.7, 0.9)
    0.707
    """
    # we know we are given the proper datatypes and don't need to verify them
    distance = ((x2-lst[0])**2+(y2-lst[1])**2)**0.5
    # round to 2 decimal places to avoid errors
    return round(distance, 3)


# Question 4.2
def lunch(lunch_places, office_x, office_y, threshold):
    """
    Use the helper function from 4.1 to calculate the distance from each of the 
    coordinates given in the list. Then, compare if it is bigger than the
    threshold value.

    >>> lunch([[0, 0], [30.5, 20.7]], 3.2, 4, 6)
    [[0, 0]]
    >>> lunch([[-3, -4], [6, 7]], 3, 4, 10)
    [[-3, -4], [6, 7]]
    >>> lunch([[100, 100]], 100.5, 100, 0.2)
    []

    # Add your own doctests below
    >>> lunch([[0,0], [0.25, 0.25], [10.224, 3.234]], 25, 25, 12)
    []
    >>> lunch([[0,0]], 0, 0, 0)
    [[0, 0]]
    >>> lunch([[12, 398], [120, 204], [128, 873], [128, 28]], 120, 294, 1000)
    [[12, 398], [120, 204], [128, 873], [128, 28]]
    """
    possible_spots = []
    for coord in lunch_places:
        distance = ((office_x - coord[0])**2 + (office_y - coord[1])**2)**0.5
        if distance <= threshold:
            possible_spots.append(coord)
    return possible_spots


# Question 5
def lunch_names(lunch_places, office_x, office_y, threshold, names):
    """
    Check that each restaurant is matched to a coordinate. Create an empty list
    and calculate the distance from the office. If it is within the threshold,
    add it to the list but instead of the coordinate the name of the 
    restaurant. Otherwise, ignore it.

    >>> lunch_names([[0, 0], [30, 20], [5, 9]], 3.2, 4, 6, \
    ['place1', 'place2', 'place3'])
    ['place1', 'place3']
    >>> lunch_names([[-3, -4], [6, 7]], 3, 4, 10, \
    ['place1', 'place2'])
    ['place1', 'place2']
    >>> lunch_names([[100, 100]], 100.5, 100, 0.2, ['place1'])
    []
    
    # Add your own doctests below
    >>> lunch_names([[0, 0]], 0, 0, 0, [''])
    ['']
    >>> lunch_names([[1, 23], [24, 12], [64, 2]], 12, 21, 43, ['place1', \
                    'place2', 'place3', 'place4'])
    'Not all restaurants are matched with a coordinate!'
    >>> lunch_names([[74, 32], [230, 28], [92, 76]], 12, 24, 182, ['place1', \
                    'place2', 'place3'])
    ['place1', 'place3']
    """
    # check that every restaurant is matched to a coordinate
    if len(lunch_places) == len(names):
        possible_spots = []
        for coord in lunch_places:
            # calculate the distance of each restaurant
            distance = ((office_x-coord[0])**2 + (office_y-coord[1])**2)**0.5
            # check threshold requirement
            if distance <= threshold:
                '''
                technically a slight error if two restaurants were able to 
                have the same coordinate (ex. they are stacked in a building)
                i'm not sure if it's necessary, though in case I have attached
                a code sample below which utilizes enumerate to solve this
                '''
                place_index = lunch_places.index(coord)
                # add restaurant to possible spots
                possible_spots.append(names[place_index])
        return possible_spots
    else:
        return 'Not all restaurants are matched with a coordinate!'

# example of how we may use enumerate to account for identical coordinates
'''
if len(lunch_places) == len(names):
    possible_spots = []
    for i, coord in enumerate(lunch_places):
        distance = ((office_x - coord[0])**2 + (office_y - coord[1])**2)**0.5
        if distance <= threshold:
            possible_spots.append(names[i])
    return possible_spots
else:
    return 'Not all restaurants are matched with a coordinate!'
'''


# Question 6
def meeting_message(i_name, time, place, s_name):
    """
    Set up a template function, and insert the parameters into the places
    necessary. Then, return it.

    >>> print(meeting_message("Penny", "3:15pm", "Cheesecake Factory", \
        "Sheldon"))
    Dear Penny,
    Please join our meeting at 3:15pm, at the Cheesecake Factory.
    <BLANKLINE>
    See you soon: Sheldon

    >>> print(meeting_message("Freya", "", "Dog Park", "Marina"))
    Dear Freya,
    Please join our meeting at , at the Dog Park.
    <BLANKLINE>
    See you soon: Marina

    # Add your own doctests below

    >>> print(meeting_message("", "", "", ""))
    Dear ,
    Please join our meeting at , at the .
    <BLANKLINE>
    See you soon: 
    
    >>> print(meeting_message("Jake", "2:10pm", "Din Tai Fung", "Tom"))
    Dear Jake,
    Please join our meeting at 2:10pm, at the Din Tai Fung.
    <BLANKLINE>
    See you soon: Tom

    >>> print(meeting_message("12", "j", "0", ""))
    Dear 12,
    Please join our meeting at j, at the 0.
    <BLANKLINE>
    See you soon: 
    """
    template = f"Dear {i_name},\n" \
            + f"Please join our meeting at {time}, at the {place}.\n\n" \
            + f"See you soon: {s_name}"

    return template


# Question 7
def seat_number(lst):
    """
    Create an empty list. iterate through the given lst and if the name length 
    is not in the empty list, append its length into the empty list. If it is,
    append "taken" into the list. 

    >>> seat_number(["Marina", "Tom", "B"])
    [6, 3, 1]
    >>> seat_number(["Marina", "Sue", "Ben", "Freya"])
    [6, 3, 'taken', 5]
    >>> seat_number(["Marina", "Sue", "Ben", ""])
    [6, 3, 'taken', 0]

    # Add your own doctests below
    >>> seat_number(["", "", "", ""])
    [0, 'taken', 'taken', 'taken']
    >>> seat_number(["Tom", "", "", "Kat"])
    [3, 0, 'taken', 'taken']
    >>> seat_number([""])
    [0]
    """

    new_lst=[]
    for name in lst:
        if len(name) not in new_lst:
            new_lst.append(len(name))
        else:
            new_lst.append("taken")
    return new_lst


# Question 8
def computers(choices):
    """
    Count the number of "DESKtop" in the list and number of "LAPtop" in the 
    list. Compare them and if DESKtop is strictly greater than LAPtop count 
    then return True. Otherwise, return false.

    >>> computers(["DESKtop", "LAPtop", "DESKtop"])
    True
    >>> computers(["LAPtop", "LAPtop"])
    False
    >>> computers(["DESKtop", "Pager", "Tablet", "LAPtop"])
    False

    # Add your own doctests below
    >>> computers(["aweifoj", "oaiejf", "weoifajw"])
    False
    >>> computers([])
    False
    >>> computers(["DESKtop", "paper", "Desktop", "laptop"])
    True
    """
    desktop_count = choices.count("DESKtop")
    laptop_count = choices.count("LAPtop")
    return desktop_count > laptop_count
    # other method is below

'''
desktop_count = 0
laptop_count = 0
for item in choices:
    if item == "DESKtop":
        desktop_count += 1
    elif item == "LAPtop":
        laptop_count +=1
return desktop_count > laptop_count
    
'''


# Question 9
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
    '25.33'
    >>> age_average(["-12", "-999"])
    '0.0'
    >>> age_average(["33"])
    '33.0'
    """
    total_ages = 0
    total_length = len(lst)
    #case for empty list
    if len(lst) == 0:
        return "0.0"
    #case for nonempty list
    for age in lst:
        if int(age) > 0:
            total_ages += int(age)
        else:
            total_length -= 1
    # case for if all numbers are negative
    if total_length == 0:
        return "0.0"
    # round to two decimal places to avoid floating point errors
    return str(round(total_ages/total_length, 2))


# Question 10
def supervision_teams(team, company_name):
    """
    Initialize two lists where one will hold the values of the first team
    and the other the values of the second team. Iterate through team 
    separating the even indices and the odd indices. Then, add company_name in
    at the respective indices for ecah list.

    >>> supervision_teams(["p1", "p2", "p3"], "Marina")
    (['Marina', 'p1', 'p3'], ['p2', 'Marina'])
    >>> supervision_teams(["p1"], "Marina")
    (['Marina', 'p1'], ['Marina'])
    >>> supervision_teams(["p1", "p2", "p3", "p4", "p5", "p6"], "Marina")
    (['Marina', 'p1', 'p3', 'p5'], ['p2', 'p4', 'p6', 'Marina'])

    # Add your own doctests below
    >>> supervision_teams([""], "")
    (['', ''], [''])
    >>> supervision_teams(["p1", ""], "Tom")
    (['Tom', 'p1'], ['', 'Tom'])
    >>> supervision_teams([],'')
    ([''], [''])
    """
    team1 = []
    team2 = []
    i=0
    for name in team:
        if i % 2 == 0 or i == 0:
            team1.append(name)
            i+=1
        else: 
            team2.append(name)
            i+=1
    
    team1.insert(0, company_name)
    team2.append(company_name)
    return (team1, team2)