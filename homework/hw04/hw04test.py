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

    >>> age_groups('files/header.txt', 'files/empty_out.txt')
    >>> with open('files/empty_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35

    >>> age_groups('files/mixed_dates.txt', 'files/mixed_dates_out.txt')
    >>> with open('files/mixed_dates_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35
    Jake,-1
    Emma,0
    Noah,1
    
    >>> age_groups('files/extra_whitespace.txt', 'files/extra_whitespace_out.txt')
    >>> with open('files/extra_whitespace_out.txt', 'r') as outfile:
    ...    for line in outfile:
    ...       print(line.strip())
    name,older than 35
    Alice,1
    Bob,-1
    """
    current_year = 2024
    required_age = 35
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
                year = int(new_line[2].split('/')[2])
                # control flow to determine their age relative to 35.
                if current_year-year < required_age:
                    f.write(f'\n{new_line[0]},-1')
                elif current_year-year == required_age:
                    f.write(f'\n{new_line[0]},0')
                else:
                    f.write(f'\n{new_line[0]},1')
    return