"""
DSC 20 Winter 2025 Lab 08
Name: TODO
PID:  TODO
SOURCE:
"""

# Question 1

class Main_Store:
    """
    >>> p = Main_Store("Magic Wand", "HERE!", 50, 100)
    >>> p.name
    'Magic Wand'
    >>> p.address
    'HERE!'
    >>> p.stock
    50
    >>> p.display_address()
    'Magic Wand is located at: HERE!'
    >>> p.pay_tax(10)
    >>> p.total
    90.0
    >>> p.reduce_stock(20)
    >>> p.stock
    30
    >>> ep = Branch("Enchanted Shield", "THERE!", 70, 200, '45.67')
    >>> ep.change_gps_location('56.78')
    >>> ep.gps_location
    '56.78'
    >>> ep.display_address()
    'Enchanted Shield is located at: THERE!, GPS location: 56.78'
    >>> ep.total
    200
    >>> ep.bonus_from_main(100)
    >>> ep.total
    250.0
    >>> p.send_stock_to_local(ep, 40)
    >>> p.stock
    0
    >>> ep.stock
    100
    """
    def __init__(self, name, address, stock, total):
        self.name = name
        self.address = address
        self.stock = stock
        self.total = total

    def display_address(self):
        return f"{self.name} is located at: {self.address}"

    def pay_tax(self, tax_amount):
        """
        Applies tax_amount to the stores's tax_amount.
        """
        self.total -= (tax_amount / 10) * self.total

    def reduce_stock(self, quantity):
        """
        Reduces the stock of the item by the given quantity.
        If the quantity is greater than the current stock, set the stock to 0.
        """
        self.stock = max(0, self.stock - quantity)

    def restock(self, quantity):
        """
        Increases the stock of the item by the given quantity.
        """
        self.stock -= quantity

    def send_stock_to_local(self, local_branch, amount):
        """
        Sends stock to local branch. If the amount is greater than the \
        current stock, sends everything that main store has.\
        Updates all stocks. 
        """
        amount_to_send = min(amount, self.stock)
        self.reduce_stock(amount_to_send)
        local_branch.restock(amount_to_send)

class Branch(Main_Store):

    def __init__(self, name, address, stock, total, gps_location):
        super().__init__(name, address, stock, total)
        self.gps_location = gps_location

    def display_address(self):
        """
        Displays information about the enchanted item, including its 
            enchantment level.
        """
        basic_info = super().display_address()
        return f"{basic_info}, GPS location: {gps_location}"


    def change_gps_location(self, new_gps):
        """
        Applies a magical boost to the item's enchantment level.
        """
        self.gps_location = new_gps

    def bonus_from_main(self, bonus_amount):
        """
        Increases total by a percentage of bonus_amount depending on the \
        value of bonus_amount. If the bonus is less than 100, apply \
        full bonus. If bonus is greater than or equal to 500, apply \
        a quarter of the bonus. Otherwise, apply half the bonus.
        """
        if bonus_amount <= 100:
            self.total = self.total + bonus_amount
        elif bonus_amount >= 500:
            self.total = self.total + (bonus_amount * 0.2)
        else:
            self.total = self.total + (bonus_amount * 0.5)


# Question 2

def q2_doctests():
    """
    >>> frodo = Hobbit(20, 2, 5, 7)
    >>> sam = Hobbit(19, 18, 4, 5)
    >>> frodo.barter(sam, 34)
    True
    >>> frodo.coins
    2
    >>> frodo.pipeweed
    1
    >>> sam.coins
    18
    >>> sam.pipeweed
    8
    >>> frodo.go_on_adventure(5)
    True
    >>> frodo.courage
    2
    >>> sam.payment_after_adventure(5, 2, 1)
    True
    >>> sam.courage
    4
    >>> sam.coins
    23
    >>> sam.hobbit_level()
    'Your hobbit is at level 1'
    >>> merry = Common_Hobbit(23, 15, 5, 2)
    >>> bilbo = GrandPa_Hobbit(100, 84, 70, 30)
    >>> merry.barter(bilbo, 20)
    'GrandPa_Hobbit wins again!'
    >>> merry.coins
    0
    >>> bilbo.hobbit_level()
    'Your hobbit is at level 27'

    """

class Hobbit:
    
    def __init__(self, age, coins, pipeweed, courage):
        # YOUR CODE STARTS HERE #
        return

    def barter(self, other_hobbit, item_value):
        # YOUR CODE STARTS HERE #
        return

    def go_on_adventure(self, needed_courage):
        # YOUR CODE STARTS HERE #
        return

    def payment_after_adventure(self, revenue, needed_courage, gained_courage):
        # YOUR CODE STARTS HERE #
        return

    def hobbit_level(self):
        # YOUR CODE STARTS HERE #
        return

class Common_Hobbit(Hobbit):
    def barter(self, other_hobbit, item_value):
        # YOUR CODE STARTS HERE #
        return

class GrandPa_Hobbit(Hobbit):
    def hobbit_level(self):
        # YOUR CODE STARTS HERE #
        return
