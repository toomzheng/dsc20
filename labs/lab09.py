"""
DSC 20 Winter 2025 Lab 09
Name: Tom Zheng
PID: A184241367
Source: N/A
"""

# Question 1

def q1_doctests():
    """
    >>> Ingredient(5, 50.0, 0.05)
    Traceback (most recent call last):
    ...
    TypeError: name must be a string
    
    >>> Ingredient("salt", 5, 0.05)
    Traceback (most recent call last):
    ...
    TypeError: weight must be a float
    
    >>> Ingredient("salt", 50.0, 3)
    Traceback (most recent call last):
    ...
    TypeError: price must be a float

    >>> salt = Ingredient("salt", 50.0, 0.05)
    >>> pepper = Ingredient("pepper", 100.0, 0.03)
    >>> salt.name
    'salt'
    >>> salt.weight
    50.0
    >>> salt.price
    0.05

    >>> salt.total_cost()
    2.5
    >>> pepper.total_cost()
    3.0

    >>> str(salt)
    '50.0g of salt at $0.05 per gram'
    >>> str(pepper)
    '100.0g of pepper at $0.03 per gram'

    >>> salt
    Ingredient: salt
    >>> pepper
    Ingredient: pepper

    >>> salt == pepper
    False
    >>> salt != pepper
    True
    >>> salt > pepper
    False
    >>> salt >= pepper
    False
    >>> salt < pepper
    True
    >>> salt <= pepper
    True
    """
    
    return

class Ingredient:
    def __init__(self, name, weight, price):
        """
        name (str): name of the ingredient
        weight (float): weight of ingredient in grams
        price (float): price per gram
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(weight, float):
            raise TypeError("weight must be a float")
        if not isinstance(price, float):
            raise TypeError("price must be a float")
        self.name = name
        self.weight = weight
        self.price = price

    def total_cost(self):
        return self.weight * self.price

    def __str__(self):
        return f"{self.weight}g of {self.name} at ${self.price} per gram"

    def __repr__(self):
        return f"Ingredient: {self.name}"

    def __eq__(self, other):
        # if equal
        return self.total_cost() == other.total_cost()
    
    def __ne__(self, other):
        # if not equal
        return self.total_cost() != other.total_cost()

    def __gt__(self, other):
        #  if greater than
        return self.total_cost() > other.total_cost()
    
    def __ge__(self, other):
        # if greater than or equal to
        return self.total_cost() >= other.total_cost()
    
    def __lt__(self, other):
        # if less than
        return self.total_cost() < other.total_cost()
    
    def __le__(self, other):
        # if less than or equal to
        return self.total_cost() <= other.total_cost()
    

# Question 2

def q2_doctests():
    """
    >>> paprika = Ingredient("paprika", 5.0, 0.1)
    >>> salt = Ingredient("salt", 50.0, 0.05)
    >>> pepper = Ingredient("pepper", 100.0, 0.03)
    >>> spice = Ingredient("paprika", 10.0, 0.05)
    >>> chilis = Ingredient("chilis", 100.0, 0.5)

    >>> ingredients1 = [paprika, salt, pepper]
    >>> ingredients2 = [spice, chilis]

    >>> seasoning = Recipe("seasoning", ingredients1, 1)
    >>> spice_blend = Recipe("spice blend", ingredients2, 2)
    >>> seasoning.name
    'seasoning'
    >>> isinstance(seasoning.ingredients, list)
    True
    >>> seasoning.difficulty
    1

    >>> seasoning.total_recipe_cost()
    6.0
    >>> spice_blend.total_recipe_cost()
    50.5

    >>> spice = Ingredient("paprika", 10.0, 0.05)
    >>> chilis = Ingredient("chilis", 100.0, 0.5)
    >>> ingredients = [spice, chilis]

    >>> str(seasoning)
    'Recipe: seasoning'
    >>> str(spice_blend)
    'Recipe: spice blend'

    >>> seasoning
    Ingredients:
    5.0g of paprika at $0.1 per gram
    50.0g of salt at $0.05 per gram
    100.0g of pepper at $0.03 per gram
    >>> Recipe("blank", [], 0)
    Ingredients:
    <BLANKLINE>

    >>> seasoning == spice_blend
    False
    >>> seasoning != spice_blend
    True
    >>> seasoning > spice_blend
    False
    >>> seasoning >= spice_blend
    False
    >>> seasoning < spice_blend
    True
    >>> seasoning <= spice_blend
    True

    >>> new_recipe = seasoning + spice_blend
    >>> new_recipe.name
    'seasoning spice blend'
    >>> isinstance(new_recipe.ingredients, list)
    True
    >>> new_recipe.difficulty
    3

    # if you are failing this doctest, you aren't updating prices properly
    >>> new_recipe.total_recipe_cost()
    56.25
    
    # if you are failing this doctest, you aren't making deep copies properly
    >>> seasoning.ingredients[0] is new_recipe.ingredients[0]
    False
    """
    return

class Recipe:
    def __init__(self, name, ingredients, difficulty):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(ingredients, list):
            raise TypeError("ingredients must be a list")
        if not isinstance(difficulty, int):
            raise TypeError("difficulty must be an integer")
        self.name = name
        self.ingredients = ingredients
        self.difficulty = difficulty
        return 
    
    def total_recipe_cost(self): 
        total = 0.0
        for ingredient in self.ingredients:
            total += ingredient.total_cost()
        return total
    
    def __str__(self):
        return f"Recipe: {self.name}"

    def __repr__(self):
        result = "Ingredients:\n"
        if not self.ingredients:
            return result
            
        return result + "\n".join(str(ingredient) for ingredient in self.ingredients)
        
    def __eq__(self, other):
        return self.total_recipe_cost() == other.total_recipe_cost()
    
    def __ne__(self, other):
        return self.total_recipe_cost() != other.total_recipe_cost()

    def __gt__(self, other):
        return self.total_recipe_cost() > other.total_recipe_cost()
    
    def __ge__(self, other):
        return self.total_recipe_cost() >= other.total_recipe_cost()
    
    def __lt__(self, other):
        return self.total_recipe_cost() < other.total_recipe_cost()
    
    def __le__(self, other):
        return self.total_recipe_cost() <= other.total_recipe_cost()
    
    def __add__(self, other_recipe):
        # create new name and difficulty
        new_name = f"{self.name} {other_recipe.name}"
        new_difficulty = self.difficulty + other_recipe.difficulty
        
        # Dictionary to track ingredients by name
        ingredients_dict = {}
        
        # process current recipe's ingredients first
        for ingredient in self.ingredients:
            # crate deep copy
            new_ingredient = Ingredient(
                ingredient.name,
                ingredient.weight,
                ingredient.price
            )
            ingredients_dict[ingredient.name] = new_ingredient
        
        # process other recipe's ingredients
        for ingredient in other_recipe.ingredients:
            if ingredient.name in ingredients_dict:
                # if ingredient exists combine weights and take lower price
                existing = ingredients_dict[ingredient.name]
                existing.weight += ingredient.weight
                existing.price = min(existing.price, ingredient.price)
            else:
                # new ingredient - make deep copy and add to dict
                new_ingredient = Ingredient(
                    ingredient.name,
                    ingredient.weight,
                    ingredient.price
                )
                ingredients_dict[ingredient.name] = new_ingredient
        
        # turn dict into lsit
        new_ingredients = []
        
        # add ingredients from current recipe first to keep order same
        for ingredient in self.ingredients:
            new_ingredients.append(ingredients_dict[ingredient.name])
        
        # add new ingredients from other not in current recipe
        for ingredient in other_recipe.ingredients:
            if ingredient.name not in {i.name for i in new_ingredients}:
                new_ingredients.append(ingredients_dict[ingredient.name])
        
        return Recipe(new_name, new_ingredients, new_difficulty)