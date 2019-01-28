# ---------------- Code Section 1 ---------------------

# The first statement never runs because it is false
# The evaluates to true so it returns 3
if False:
    1 + "two"  # This line never runs
else:
    1 + 2

# ---------------- Code Section 2 ---------------------

# declares a string available with the name "hello"
thing = "hello"
# type() returns the type of the object which will be a string
type(thing)

# when thing is changed to a float type() returns a float
thing = 28.1
type(thing)


# ---------------- Code Section 3 ---------------------

# defining a class  "TheHobbit"
class TheHobbit:
    # the class has a method which retuns the length of the  object.
    # "self" refers to the object which is  the same as "this" in Java
    def __len__(self):
        return 95022


# creating a  new object with a variable name "the_hobbit"
the_hobbit = TheHobbit()
# len() returns the value of the  method defined in the class
len(the_hobbit)


# ---------------- Code Section 4 ---------------------

# define a function called len, which takes in an obj as a parameter and then return the __len__() method.
def len(obj):
    return obj.__len__()


# ---------------- Code Section 5 ---------------------

# A function named "headline" with two parameters "text" and "align" without types
def headline(text, align=True):
    # Checks if "align" is true, if so return the statement
    if align:
        # f is a formatted string literal which is a way of formatting your string
        """ the return statement prints the value of the text, then on a new line prints the underscore the number of 
        times of the length of the the string """
        return f"{text.title()}\n{'-' * len(text)}"
    # Checks if "align" is false, if so return the statement
    else:
        return f" {text.title()} ".center(50, "o")


# ---------------- Code Section 6 ---------------------

# A call to the function "headline", since one of it's parameters are defined already you can pass any text you want
print(headline("python type checking"))

# A call to the function "headline", setting the "align" parameter to false
print(headline("python type checking", align=False))

# ---------------- Code Section 7 ---------------------


# adding type hints to a method with two arguments
# the method has a return type od string
# the first argument has a  type of string
# the second argument has a type hint of boolean and a default value of True
def headline(text: str, align: bool = True) -> str:


# ---------------- Code Section 8 ---------------------

# this tatement prints the text to the screen  and aligns it to the left
print(headline("python type checking", align="left"))

# ---------------- Code Section 9 ---------------------

# headlines_with_error.py

# A function with two parameters and  type hints
# the "text" parameter has a type of str
# the "align" parameter hsa a type of boolean, which also has a default value of False
# the method "headline"  has a return type of str

def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


# A call to the method throws no error because all the type parameters are correct
print(headline("python type checking"))
# A call to the method throws an error because the "align" parameter was set as a string instead of a bollean value
print(headline("use mypy", align="center"))


# ---------------- Code Section 10 ---------------------

# headlines.py

# A function with two parameters and  type hints
# the "text" parameter has a type of str
# the "centered" parameter hsa a type of boolean, which also has a default value of False
# the method "headline"  has no return type of str
def headline(text: str, centered: bool = False):
    if not centered:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


print(headline("python type checking"))
print(headline("use mypy", centered=True))

# ---------------- Code Section 11 ---------------------

# this is how you annotate function arguments and return value
def func(arg: arg_type, optarg: arg_type = default) -> return_type:

# ---------------- Code Section 12 ---------------------

# imports mathematical functions such as pi, ceil() etc ...

import math


# a function circumference with a parameter radius
# the parameter has been annotated with a float type hint
# the function has been annotated with a float type hint
def circumference(radius: float) -> float:
        # returns the calculation of the circumference of a circle where pi is 3.142
        return 2 * math.pi * radius



# ---------------- Code Section 13 ---------------------

# a call to the function with a radius of 1.23
circumference(1.23)

# the __annotations__ gives you all the attributes of the function
circumference.__annotations__


# ---------------- Code Section 14 ---------------------

# reveal.py

# imports in built math function
import math

# you might not know the type after a mathematical operation
# you can use reveal_type() to find out the type
reveal_type(math.pi)

radius = 1
circumference = 2 * math.pi * radius
#reveal_locals() debugs your hint type local variables and functions
reveal_locals()



# ---------------- Code Section 15 ---------------------

import math


# a function with a radius parameter
# the function type hints are added with type comments
# type comments are specially formatted comments that can be used to add type hints compatible with older code
# A type comment must start with the type: literal,  and be on the same or the following line as the function definition

def circumference(radius):
    # type: (float) -> float
    return 2 * math.pi * radius

# ---------------- Code Section 16 ---------------------

# Type comments are handled directly by the type checker, so these
# types are not available in the __annotations__
circumference.__annotations__


# ---------------- Code Section 17 ---------------------

# a function with three parameters
# annotating a function with several arguments, you write each type separated by comma
def headline(text, width=80, fill_char="-"):
    # type: (str, int, str) -> str
    # the center() method returns a string which is padded with the specified character.
    return f" {text.title()} ".center(width, fill_char)


print(headline("type comments work", width=40))

# ---------------- Code Section 18 ---------------------

# headlines.py

# a function with three arguments
# each arguments are on seperate line with own annotation
def headline(
        text,  # type: str
        width=80,  # type: int
        fill_char="-",  # type: str
):  # type: (...) -> str
    return f" {text.title()} ".center(width, fill_char)


# this print works because all the arguments passed in the function are of the correct  type
print(headline("type comments work", width=40))

# An Error will occurs because the width argument expects an integer but instead it's a string
print(headline("type comments work", width="full"))


# ---------------- Code Section 19 ---------------------


# you can also type comments to variables by the same way its done for functions
pi = 3.142  # type: float


# ---------------- Code Section 20 ---------------------

# game.py

# imports the random function
import random

#our list of suits is created by a string of the possible suits, which then has the split function called on it.
#the split function called without a character delimeter argument will split the string intoa list of words seperated by whitespaces.
SUITS = "♠ ♡ ♢ ♣".split()
#we follow a similar strategy to the suites in order to obtain a list of the card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


# we define a function called create_deck.
# this function takes a bool parameter called shuffle which has a default value of false and returns a Deck object
def create_deck(shuffle=False):
    """Create a new deck of 52 cards"""

    #use a list comprehension to create a deck, which creates a deck of cards with one card of each rank per card suite

    deck = [(s, r) for r in RANKS for s in SUITS]

    #if shuffle is equal to true, we use random to shuffle our deck

    if shuffle:
        random.shuffle(deck)
    return deck


# define a function called deal_hands, which takes in a deck parameter deck (with a type Deck) and returns a Tuple of 4 decks.

def deal_hands(deck):
    """Deal the cards in the deck into four hands"""
    # return the tuple which contains the deck split into 4 parts using slices.
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


#define a function called play
def play():
    """Play a 4-player card game"""

    # call the create_deck function to create a deck, passing in a shuffle value of True so that the deck shuffles.
    deck = create_deck(shuffle=True)
    # get a list of player names from the string below, player names will be ['P1', 'P2', 'P3', 'P4']
    names = "P1 P2 P3 P4".split()
    # define a dictionary, using a dict. comprehension, which maps each player to a tuple result of the deal_hands function
    hands = {n: h for n, h in zip(names, deal_hands(deck))}

    # loop through each name in the turn order
    for name, cards in hands.items():

            card_str = " ".join(f"{s}{r}" for (s, r) in cards)
        print(f"{name}: {card_str}")

#if the source file is excuted as the main program, call the play function
if __name__ == "__main__":
    play()

 # ---------------- Code Section 21 ---------------------

# adding type hints to simple type like str, float or bool
# you simple add it using type itself
name: str = "Guido"
pi: float = 3.142
centered: bool = False

# ---------------- Code Section 22 ---------------------

# adding it to composite types is simply the same
# but it doesn't tell you the types of each element
# List is a collection which is ordered and changeable. Allows duplicate members.
names: list = ["Guido", "Jukka", "Ivan"]
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
version: tuple = (3, 7, 1)
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
options: dict = {"centered": False, "capitalize": True}


# ---------------- Code Section 23 ---------------------

# importing the special types in the typing module
# the types help in specifying the types of each element in a composite types
from typing import Dict, List, Tuple
# tells you that all the elements in the list are of the type str
names: List[str] = ["Guido", "Jukka", "Ivan"]
# tells you that all the elements in the tuple are of the type int
version: Tuple[int, int, int] = (3, 7, 1)
# tells you that all the elements in the Dict are of the types str and bool
options: Dict[str, bool] = {"centered": False, "capitalize": True}

# ---------------- Code Section 24 ---------------------


# type hinting the function create_deck which takes a bool argument with a default value of False
# the function returns a deck of cards with a list of tuple of two strings
def create_deck(shuffle: bool = False) -> List[Tuple[str, str]]:
    """Create a new deck of 52 cards"""
    # explained already in code section 20
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


# ---------------- Code Section 25 ---------------------

# importing the special types in the typing module
from typing import List, Sequence

# function sequare that has an argument sequence which is an ordered list of float types
# thw function has a return type of a list of float types
def square(elems: Sequence[float]) -> List[float]:
    return [x**2 for x in elems]

# ---------------- Code Section 26 ---------------------

#  a function called deal_hands, which takes in a deck parameter deck (a list of tuple of two strings) and returns a Tuple of 4 decks(a list of tuple of two strings).
def deal_hands(
    deck: List[Tuple[str, str]]
) -> Tuple[
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
]:
    """Deal the cards in the deck into four hands"""
    # return the tuple which contains the deck split into 4 parts using slices.
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


# ---------------- Code Section 27 ---------------------

# importing the special types in the typing module
from typing import List, Tuple

# a card type alias of Tuple of two strings
Card = Tuple[str, str]
# a deck type alias which is a list of Card
Deck = List[Card]


# ---------------- Code Section 28 ---------------------

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]

# ---------------- Code Section 29 ---------------------

# as expalined in code section 27
from typing import List, Tuple
Card = Tuple[str, str]
Deck = List[Card]

Deck
typing.List[typing.Tuple[str, str]]


# ---------------- Code Section 30 ---------------------

# a function with a player_name argument that has no explicit return
def play(player_name):
    print(f"{player_name} plays")

# assigning the function to a variable and passing a parameter returns the parameter value
ret_val = play("Jacob")
Jacob plays

# printing the parameter has a Nonne value
print(ret_val)
None











