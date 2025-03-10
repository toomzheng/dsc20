"""
DSC 20 Winter 2025 Homework 08
Name: Tom Zheng
PID: A18424137
Source: Claude 3.5 Sonnet for clarification on some Q4 exceptions.
"""

def q1_doctests():
    """
    Doctests for Question 1.
    
    >>> broom_1 = FlyingBroom()
    >>> broom_2 = NormalBroom()
    >>> broom_3 = CursedBroom()
    >>> broom_2.boost(20)
    True
    >>> broom_1.duel(broom_2)
    False
    >>> broom_2.high_score()
    9100
    >>> broom_2.duel(broom_3)
    False
    >>> broom_2.speed
    30
    >>> broom_3.high_score()
    25750
    >>> broom_4 = CursedBroom()
    >>> broom_3.duel(broom_4)
    True
    >>> broom_4.size
    7
    >>> broom_4.speed
    20
    >>> broom_3.size
    8
    >>> broom_4.boost(40)
    True
    >>> broom_4.lives
    6
    >>> broom_4.duel(broom_2)
    True
    >>> broom_4.high_score()
    24650
    >>> broom_4.size
    8
    >>> broom_2.speed
    50
    
    
    # ADD DOCTESTS HERE #
    # 3 new objects of each class
    >>> nimbus = FlyingBroom()
    >>> firebolt = NormalBroom()
    >>> deathstick = CursedBroom()
    
    #  test boost
    >>> nimbus.magic_power = 1
    >>> nimbus.boost(10)
    True
    >>> nimbus.magic_power
    0
    >>> nimbus.boost(5)  # No magic power left
    False
    
    # test duel
    >>> cleansweep = FlyingBroom()
    >>> cleansweep.size = 10
    >>> nimbus.size = 5
    >>> cleansweep.duel(nimbus)
    True
    >>> nimbus.size = cleansweep.size  # Same size
    >>> nimbus.duel(cleansweep)
    False
    >>> thunderbolt = NormalBroom()
    >>> dark_broom = CursedBroom()
    >>> thunderbolt.duel(dark_broom)  # NormalBroom vs CursedBroom
    False
    
    # test high_score
    >>> swift = FlyingBroom()
    >>> swift.speed = 100
    >>> swift.lives = 2
    >>> swift.high_score()
    11000
    >>> quick = NormalBroom()
    >>> quick.speed = 75
    >>> quick.lives = 4
    >>> quick.high_score()
    9500
    >>> evil = CursedBroom()
    >>> evil.speed = 50
    >>> evil.lives = 3
    >>> evil.high_score()
    11150
    """
    return

# constants for FlyingBroom class
default_speed = 50
default_size = 5
default_magic_power = 3
default_lives = 3

# constants for score calculation
speed_multiplier = 100
lives_multiplier = 500

# constants for CursedBroom class
cursed_default_speed = 70
cursed_default_size = 7
cursed_default_magic_power = 5
cursed_default_lives = 5

# constants for CursedBroom score calculation
cursed_speed_multiplier = 200
cursed_lives_multiplier = 300
cursed_bonus_score = 250

# constants for duel method
speed_change = 50

double = 2
square = 2
root = 0.5
class FlyingBroom:
    """
    Implementation of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of FlyingBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): current speed of broom, default is 50
        - size (positive int): physical size of broom, default is 5
        - magic_power (non-negative int): number of magic boosts remaining
          for this broom, default is 3
        - lives (non-negative int): number of lives a wizard has while
          flying this broom, default is 3
        """
        self.speed = default_speed
        self.size = default_size
        self.magic_power = default_magic_power
        self.lives = default_lives

    def boost(self, charm_power):
        """
        Boosts the speed of the broom by using a magical
        charm. Speed boost is calculated using the formula
        specified in the write-up. If boost is successfully
        applied (enough magic power to perform boost), return True.
        Otherwise (no remaining magic power to perform boost), return False.
        
        Parameters:
        - charm_power (int): used to calcualte speed boost formula.
          Applied as long the broom still has some magic power
          remaining.
        """
        if self.magic_power <= 0:
            return False
            
        old_speed = self.speed
        old_score = self.high_score()
        # Calculate new speed using the formula
        self.speed = int(((old_speed + charm_power)**square\
                           + (old_speed - charm_power)**square)**root)
        
        # Check if high score doubled
        new_score = self.high_score()
        if new_score >= double * old_score:
            self.set_lives(True)
        
        self.magic_power -= 1

        return True

    def set_speed(self, new_speed):
        """
        Setter method that assigns given speed value to 
        speed attribute.
        
        Parameters:
        - new_speed (int): new speed value
        """
        self.speed = new_speed

    def set_lives(self, gains = True):
        """
        Setter method that increments lives attribute 
        by 1 if gains is True, otherwise decrement by 1.
        
        Parameters:
        - gains (bool): decides whether to increment/decrement
          lives attribute by 1.
        """
        if gains:
            self.lives += 1
        else:
            self.lives -= 1

    def set_size(self, new_size):
        """
        Setter method that assigns given size value
        (non-negative) to size attribute.
        
        Parameters:
        - new_size (non-negative int): new size value
        """
        self.size = new_size

    def duel(self, other_broom):
        """
        Determines if a duel can occur between
        current broom and other_broom. If so,
        the following happens as specified in
        the write-up. Return True if current
        broom successfully performs duel, otherwise
        False.
        
        Parameters:
        - other_broom (object): Broom object
        """
        if self.size > other_broom.size:
            other_broom.speed -= speed_change
            self.speed += speed_change
            
            if other_broom.speed <= 0:
                other_broom.set_lives(False)
                other_broom.speed = default_speed
                self.size += 1
            return True
            
        elif self.size < other_broom.size:
            self.speed -= speed_change
            other_broom.speed += speed_change
            
            if self.speed <= 0:
                self.set_lives(False)
                self.speed = default_speed
                other_broom.size += 1
            return False
            
        # If sizes are equal
        return False

    def high_score(self):
        """
        Formula for high score and returns it.
        """
        return self.speed * speed_multiplier + self.lives * lives_multiplier

reset_speed = 30
class NormalBroom(FlyingBroom):
    """
    Implementation of NormalBroom. Subclass of FlyingBroom.
    """
    def duel(self, other_broom):
        """
        Duel method for NormalBroom.
        - If other_broom is an instance of CursedBroom,
          current NormalBroom loses one life, and its speed 
          resets to 30.
        - CursedBroom object gains a size, and its speed
          increases by 50.
        - Attack is thus considered unsuccessful, function
          returns False.
        - If other_broom is not a CursedBroom object, duel
          method is the same as in the parent class.
        
        Parameters:
        - other_broom (object): Broom object
        """
        if isinstance(other_broom, CursedBroom):
            self.set_lives(False)
            self.speed = reset_speed
            other_broom.size += 1
            other_broom.speed += speed_change
            return False
        return super().duel(other_broom)

class CursedBroom(FlyingBroom):
    """
    Implementation of CursedBroom. Subclass of FlyingBroom.
    """
    def __init__(self):
        """
        Constructor of CursedBroom.
        
        Initializes the specified attributes on creation:
        - speed (non-negative int): default is 70
        - size (positive int): default is 7
        - magic_power (non-negative int): default is 5
        - lives (non-negative int): default is 5
        """
        super().__init__()
        self.speed = cursed_default_speed
        self.size = cursed_default_size
        self.magic_power = cursed_default_magic_power
        self.lives = cursed_default_lives

    def high_score(self):
        """
        Formula for a CursedBroom high score and returns it.
        """
        return self.speed * cursed_speed_multiplier + self.lives * \
            cursed_lives_multiplier + cursed_bonus_score


# Question 2
# Q2, Part 1
def fix_1(lst1, lst2):
    """
    Divides each element in lst1 by each element in lst2 and appends each
    result to a new list. If division by zero, it skips and moves on the to 
    the next element.

    Args:
        lst1 (list): list of dividends
        lst2 (list): list of divisors
    
    Returns:
        list: a list of all the quotients

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    
    # NO DOCTESTS NEEDED #
    """
    out = []
    for div in lst2:
        for num in lst1:
            try:
                out.append(num / div) # add try-catch block
            except ZeroDivisionError:
                continue
    return out

# Q2, Part 2
def fix_2(*filepaths):
    """
    Attempts to open each file in filepaths. If the file exists, it indicates
    that the file is successfully opened. If it is not found, then it prints
    that the file was not successfully opened.

    Args:
        *filepaths (str): Variable number of file paths to attempt to open
    
    Returns:
        None: Nothing is returned, rather it prints messages

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found
    >>> fix_2('docs.txt')
    docs.txt not found
    
    # NO DOCTESTS NEEDED #
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r") # add try-catch block
            print(f'{filepath} opened')
            cur_file.close()
        except FileNotFoundError:
            print(f'{filepath} not found')

# Q2, Part 3
def fix_3(lst):
    """
    Adds each element with its following element in the list and returns
    all of the summed values in a list.

    Args:
        lst (list): The input list whose adjacent elements will be summed
        
    Returns:
        list: A list containing the sums of adjacent elements in the input list

    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []
    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]
    >>> fix_3([])
    []
    
    # NO DOCTESTS NEEDED #
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try:
            sum_of_pairs.append(lst[i] + lst[i + 1]) # add try-catch block
        except TypeError as T:
            print(type(T))
        except IndexError as I:
            print(type(I))
    return sum_of_pairs


# Question 3
def check_inputs(input1, input2):
    """
    Validates input parameters according to specific rules:

    1. input1 should be a list
    2. All of the values in input1 should be numeric. \
        It is ok if input1 is empty
    3. If there are multiple non-numeric values, you only need to throw an \
        exception for the first non-numeric value encountered
    4. input2 should be numeric
    5. input2 should be contained in input1

    Args:
        input1 (list): A list that contains numeric values
        input2 (numeric): A numeric value

    Returns:
        str: 'Input validated' if all checks pass

    Raises:
        TypeError: With appropriate error message if any validation checks fail

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'
    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    
    # Add at least 3 doctests below here #

    >>> check_inputs([10, 20, 30], 20)
    'Input validated'
    >>> check_inputs([[1, 2], 3, 4], 3)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 0 is not numeric
    >>> check_inputs([1.5, 2.5, 3.5], 4.5)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    """
    if not isinstance(input1, list):
        raise TypeError("input1 is not the correct type")
    
    idx = 0
    for item in input1:
        if not isinstance(item, (int, float)):
            raise TypeError(f"The element at index {idx} is not numeric")
        idx += 1
    
    if not isinstance(input2, (int, float)):
        raise TypeError("input2 is not the correct type")
    
    if input2 not in input1:
        raise TypeError("input2 not in input1")
    
    return 'Input validated'


# Question 4
def load_file(filepath):
    """
    Loads a file and returns the number of words within it. It checks for the
    following:

    1. The filepath is a string
    2. The file exists
    3. The file is not empty (contains at least 1 word)

    Args:
        filepath (str): Path to the file to be loaded

    Returns:
        int: Number of words in the file
    
    Raises:
        TypeError: If filepath is not a string
        FileNotFoundError: If the file does not exist
        ValueError: If the file is empty

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    >>> load_file('files/ten_words.txt')
    10
    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty
    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist
    
    # Add at least 3 doctests below here #
    >>> load_file(123)
    Traceback (most recent call last):
    ...
    TypeError: filepath is not a string
    >>> load_file('files/single_word.txt')  # File contains just "Hello"
    1
    >>> load_file('files/multiple_lines.txt') 
    24
    """
    if not isinstance(filepath, str):
        raise TypeError("filepath is not a string")
    try:
        with open(filepath, "r") as cur_file:
            content = cur_file.read() # add try-catch block
            words = content.split()

            if not words:
                raise ValueError("File is empty")
            
            return len(words)
        
    except FileNotFoundError:
        raise FileNotFoundError(f'{filepath} does not exist')