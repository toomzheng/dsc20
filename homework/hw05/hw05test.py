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
