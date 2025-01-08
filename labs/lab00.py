'''
Problem to solve:

Write a Python program to generate a demand for food from your cat. If the demand message (a string) is strictly less than 5 characters long, return the string "Give me more food!". Otherwise add num number of exclamation marks at the end of the demand and return it; You may assume num is a nonnegative integer.

Hint: In Python you could multiply a string by an integer to repeat the string multiple times, and use “+” to concatenate strings.

After opening the file, you should see something like this:
'''

"""
DSC 20 Lab 00
Name: Tom ZHeng
PID:  A18424137
"""

def respect_your_cat(food, num):
    """
    This method is a demand from your cats to provide food for them.
    If the food is strictly less than 5 characters, this method will 
    return "Give me more food!" Otherwise return the food as a string
    followed by 'num' # of exclamation marks.

    >>> respect_your_cat("dog", 5)
    'Give me more food!'
    >>> respect_your_cat("lots of fish and lots of fish", 4)
    'lots of fish and lots of fish!!!!'
    >>> respect_your_cat("Fruits", 0)
    'Fruits'
    """
    if len(food) < 5:
        return 'Give me more food!'
    else:
        return f'{food + "!" * num}'
    
    