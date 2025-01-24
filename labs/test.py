def keep_a_secret(filename):
    """
    Decodes message from the given input file.

    >>> print(keep_a_secret('files/encoded_1.txt').strip())
    jack reacher
    23@4 b#l31oo%m@^ way
    FSD@si%m3~on fis#he%r
    121 rockefeller avenue
    32'1 fulleH##r "dr^i~v@e
    @@4:)5#0p1m#
    7/29 06.45
    >>> print(keep_a_secret('files/encoded_2.txt').strip())
    kurt hendricks
    simon 1p@egg
    @kremlin office
    b%i>%g@ be>n @lond#o&&n
    moscow
    @reykj@av>>ik:/
    12:50 23/11
    >>> print(keep_a_secret('files/encoded_3.txt').strip())
    <BLANKLINE>
    >>> keep_a_secret('files/encoded_4.txt').strip()
    'kurt hendricks\\nsimon 1p@egg'
    """
    # YOUR CODE GOES HERE #
    decoded_messages = []
    with open(filename, 'r') as file:
        for line in file: 
            stripped_line = line.strip()
            decoded_line = (stripped_line
                            .replace('!', '')
                            .replace('?', '')
                            .replace(';', '')
                            .replace('$', ''))
            decoded_messages.append(decoded_line)
    return '\n'.join(decoded_messages) + '\n'
