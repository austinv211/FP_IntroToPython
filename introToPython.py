

#------------ Code Section 33 -----------------------

# play.py

# define a function called play that takes in a str parameter player_name
# and returns Nothing. The None type hint is used to help identify
# a useless return value
def play(player_name: str) -> None:
    print(f"{player_name} plays")

# this will trigger an error because we are trying to assign a non-return to a variable
ret_val = play("Filip")

#------------ Code Section 34 -----------------------

# play.py

#this is our same play function described in the section above, but it does not have the return type hint of None
def play(player_name: str):
    print(f"{player_name} plays")

#now when try to assign the return of the function to a value, we do not get the "does not return a value warning"
ret_val = play("Henrik")

#------------ Code Section 35 -----------------------

# we import NoReturn from the typing library
from typing import NoReturn

# we can use this in this function defined below, black_hole, which always raises an excpetion and never properly returns
# the no return annotation is used for functions that never return normally, they have no return, which our function black_hole meets the criteria
def black_hole() -> NoReturn:
    raise Exception("There is no going back ...")

#------------ Code Section 35 -----------------------

# game.py

#import the random library
import random
#from the typing library, import List and Tuple
from typing import List, Tuple

#our list of suits is created by a string of the possible suits, which then has the split function called on it.
#the split function called without a character delimeter argument will split the string intoa list of words seperated by whitespaces.
SUITS = "♠ ♡ ♢ ♣".split()

#we follow a similar strategy to the suites in order to obtain a list of the card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

#a card is equal to a Tuple, where each index inside of the tuple is a str
Card = Tuple[str, str]

#a deck is list of cards, specified above.
Deck = List[Card]

# we define a function called create_deck.
# this function takes a bool parameter called shuffle which has a default value of false and returns a Deck object
def create_deck(shuffle: bool = False) -> Deck:
    #print 'Create a new deck of 52 cards' to the screen
    """Create a new deck of 52 cards"""

    #use a list comprehension to create a deck, which creates a deck of cards with one card of each rank per card suite
    deck = [(s, r) for r in RANKS for s in SUITS]

    #if shuffle is equal to true, we use random to shuffle our deck
    if shuffle:

        random.shuffle(deck)

    #finally we return the deck
    return deck


# define a function called deal_hands, which takes in a deck parameter deck (with a type Deck) and returns a Tuple of 4 decks.
def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:

    #print 'Deal the cards in the deck into four hands' to the screen.
    """Deal the cards in the deck into four hands"""

    #return the tuple which contains the deck split into 4 parts using slices. 
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

#define a function called choose, which takes in a parameter items
def choose(items):

    #print 'Choose and return a random item' to the screen.
    """Choose and return a random item"""

    #use the random library to get a random choice from the items provided to the function
    return random.choice(items)

#define a function called player_order which takes in a names parameter and a start parameter with a default value of None
def player_order(names, start=None):

    #print 'Rotate player order so that start goes first' to the screen.
    """Rotate player order so that start goes first"""

    #if the start parameter is None, then we will call the choose function and pass the names parameter value
    if start is None:

        start = choose(names)

    #create a variable called start_idx that gets the index of the item chosen as the start variable in the names list
    start_idx = names.index(start)

    #return the names list with the starting player rotated to the end of the list
    return names[start_idx:] + names[:start_idx]

#define a function called play which has a return type hint of None
def play() -> None:

    # print 'Play a 4-player card game' to the screen
    """Play a 4-player card game"""

    # call the create_deck function to create a deck, passing in a shuffle value of True so that the deck shuffles.
    deck = create_deck(shuffle=True)

    # get a list of player names from the string below, player names will be ['P1', 'P2', 'P3', 'P4']
    names = "P1 P2 P3 P4".split()

    # define a dictionary, using a dict. comprehension, which maps each player to a tuple result of the deal_hands function
    hands = {n: h for n, h in zip(names, deal_hands(deck))}

    # get the start_player from calling the choose function and giving the list of names
    start_player = choose(names)

    # turn_order is the result of the player_order function when given the list of names and the chosen start player
    turn_order = player_order(names, start=start_player)


    # Randomly play cards from each player's hand until empty

    while hands[start_player]:

        #loop through each name in the turn order
        for name in turn_order:

            #the card is equal to the random choice among the hand for the iterative name
            card = choose(hands[name])

            #remove the card from the players hand
            hands[name].remove(card)

            #print that the player played the card and its details to the screen
            print(f"{name}: {card[0] + card[1]:<3}  ", end="")

        print()

#if the source file is excuted as the main program, call the play function
if __name__ == "__main__":

    play()


#------------ Code Section 36 -----------------------

# import random and Any and Sequence from the typing library
import random
from typing import Any, Sequence

# define a function called choose, that takes in a parameter called items, which is a sequence that contains items of any type and returns an item of any type
# the return is a random choice from the sequence of items
def choose(items: Sequence[Any]) -> Any:
    return random.choice(items)

#------------ Code Section 37 -----------------------

# choose.py

#this involves our code block in section 36, see comments above
import random

from typing import Any, Sequence


def choose(items: Sequence[Any]) -> Any:

    return random.choice(items)


#define a list of names ['Guido', 'Jukka', 'Ivan']
names = ["Guido", "Jukka", "Ivan"]

# use the reveal_type function to reveal the type of the names list
reveal_type(names)

# set the name to be a randomly chosen name from the list of names
name = choose(names)

# reveal the type of name, which should be a type of Any
reveal_type(name)

#------------ Code Section 38 -----------------------

# this code is showing the use of subtypes.
# boolean values are just aliases for the integer values 0 or 1
# this shows that bool is a subclass of int
>>> int(False)
0

>>> int(True)
1

>>> True + True
2

>>> issubclass(bool, int)
True

#------------ Code Section 39 -----------------------

# define a function called double which takes a parameter called number, which has a type hint of int and returns an int
# this function doubles the number by returning the number * 2
def double(number: int) -> int:
    return number * 2

# a bool can pretend to be an int when passed into the function
print(double(True))  # Passing in bool instead of int

#------------ Code Section 40 -----------------------

#this is a the same choose function commented in code section 36
import random
from typing import Any, Sequence

def choose(items: Sequence[Any]) -> Any:
    return random.choice(items)
# this issue with using any is that you lose type information

#------------ Code Section 41 -----------------------

# choose.py

# import the random module and import Sequence and TypeVar from typing module
import random

from typing import Sequence, TypeVar

#define a type variable Chooseable using TypVar from the typing module
# a type variable must ne defined using TypVar
Choosable = TypeVar("Chooseable")

# define our choose function from before, but use Choosable instead of Any
def choose(items: Sequence[Choosable]) -> Choosable:

    return random.choice(items)

#we will reveal the types on our same list of names from before
names = ["Guido", "Jukka", "Ivan"]

# this will reveal a type of builtins.list[builtins.str*]
reveal_type(names)

name = choose(names)

#this will reveal a type of builtins.str* instead of Any
reveal_type(name)

#------------ Code Section 42 -----------------------

# choose_examples.py

# import choose
from choose import choose

# reveal the types of the chosen item from the lists below
# each will return the the type of the item contain in the list since we used a type variable Choosable inside of the choose function
# the type returned by Choosable will the type determined by subtype relationships if not all items are of the same type
reveal_type(choose(["Guido", "Jukka", "Ivan"]))

reveal_type(choose([1, 2, 3]))

reveal_type(choose([True, 42, 3.14]))

reveal_type(choose(["Python", 3, 7])

#------------ Code Section 43 -----------------------

# choose.py

#this is our same code from above, see comments above
import random

from typing import Sequence, TypeVar

#here we define our Choosable can only be either a str or float
Choosable = TypeVar("Choosable", str, float)


def choose(items: Sequence[Choosable]) -> Choosable:

    return random.choice(items)


reveal_type(choose(["Guido", "Jukka", "Ivan"]))

reveal_type(choose([1, 2, 3]))

#this will return float since int is a subtype of float
reveal_type(choose([True, 42, 3.14]))

#this will return an error since the return type cannot be object
reveal_type(choose(["Python", 3, 7]))

#------------ Code Section 44 -----------------------

# here we restrict the choose function in our Card Game to accept a sequence of Choosable  and return a choosable
# which can then is restricted to a type of str or Card
Choosable = TypeVar("Choosable", str, Card)

def choose(items: Sequence[Choosable]) -> Choosable:

#------------ Code Section 45 -----------------------

# define a function called len, which takes in an obj as a parameter and then return the __len__() method.
def len(obj):
    return obj.__len__()

#------------ Code Section 46 -----------------------

# from typing import Sized
from typing import Sized

# this is our same len definition, but we restrict our obj to objects that fufill the Sized protocol
def len(obj: Sized) -> int:
    return obj.__len__()

#------------ Code Section 47 -----------------------

