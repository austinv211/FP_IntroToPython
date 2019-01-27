

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

# we import NoReturn from the typing module
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

# import random and Any and Sequence from the typing module
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
int(False)
0

int(True)
1

True + True
2

issubclass(bool, int)
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

# this is our same len definition, but we restrict our obj to objects that fufill the Sized protocol, so that we can access the __len__ function
def len(obj: Sized) -> int:
    return obj.__len__()

#------------ Code Section 47 -----------------------

#import Protocol from the typing_extensions module
from typing_extensions import Protocol

# define a class called Sized which inherits from protocol and define a class method called __len__ that takes in the object and returns the integer length of the object
class Sized(Protocol):
    def __len__(self) -> int: ...

#define a len functon that takes in an object with the Sized protocol and return the result of __len__ defined inside the Protocol
def len(obj: Sized) -> int:
    return obj.__len__()

#------------ Code Section 48 -----------------------

# this is our player_order function from the card game commented above.
# there is a challenge with this because in general our start variable should be a string representing a player's name, but it can also take the special non string value of None
def player_order(names, start=None):

    """Rotate player order so that start goes first"""

    if start is None:

        start = choose(names)

    start_idx = names.index(start)

    return names[start_idx:] + names[:start_idx]

#------------ Code Section 49 -----------------------

# import Sequence and Optional from the typing module
# the Optional type says that a variable either has the specified type or is None
# the Union type can also be used as an equivalent
from typing import Sequence, Optional

# redefine our player_order function to specify the start parameter to be an Option[str],
# so our start variable is Optionally a string , if not it is None
def player_order(
    names: Sequence[str], start: Optional[str] = None
) -> Sequence[str]:
    ...

#------------ Code Section 50 -----------------------

# player_order.py

#this is the same code featured above
from typing import Sequence, Optional


def player_order(

    names: Sequence[str], start: Optional[str] = None

) -> Sequence[str]:

    # in this case we have not taken care of the case when start is None, so we will get an error when trying to run
    start_idx = names.index(start)

    return names[start_idx:] + names[:start_idx]

# the use of None for optional arguments is handled automatically by MyPy

#------------ Code Section 51 -----------------------

# game.py

# import the random and the sys modules
import random

import sys

#define a class called Card
class Card:

    # get a list of Suits using a string a the split() function
    SUITS = "♠ ♡ ♢ ♣".split()

    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    #define a class method called __init__ which initializes our object members suit and rank
    def __init__(self, suit, rank):

        self.suit = suit

        self.rank = rank

    # define a class method called __repr__ that returns the suit and the rank of the card
    def __repr__(self):

        return f"{self.suit}{self.rank}"

# define a class called deck to represent a deck of cards
class Deck:

    # define our __init__ instance method to take in the instance object as well as a parameter cards, and set the class member accordingly
    def __init__(self, cards):

        self.cards = cards

    # @classmethod converts a function to run as a class method.
    # define a class method called create that takes in cls, used in the case of a class method, and a parameter shuffle with a default value of False
    @classmethod

    def create(cls, shuffle=False):
        #print to the screen and fill the variable cards with a list comprehension that makes a card of each rank for each suit
        """Create a new deck of 52 cards"""

        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]

        # shuffle the cards if shuffle is true using the random.shuffle function
        if shuffle:

            random.shuffle(cards)

        # return the result of the factory method to create a Deck with cards
        return cls(cards)

    # define a instance method called deal which takes in the instance object and the number of hands to deal to
    def deal(self, num_hands):
        #print to the screen and define the cls variable to be a Deck
        """Deal the cards in the deck into a number of hands"""

        cls = self.__class__

        # return a Tuple using a comprehension in the cls function to create a tuple of decks.
        return tuple(cls(self.cards[i::num_hands]) for i in range(num_hands))

# define a player class
class Player:

    # we set our __init__ to fill the Player members of name and hand
    def __init__(self, name, hand):

        self.name = name

        self.hand = hand

    #define a instance method the plays a card for the player
    def play_card(self):

        """Play a card from the player's hand"""

        # get a random card from the player's hand
        card = random.choice(self.hand.cards)

        # remove the card from the player's hand
        self.hand.cards.remove(card)

        #print the players name and card they played
        print(f"{self.name}: {card!r:<3}  ", end="")

        #return the card played
        return card

# define a class to represent a Game
class Game:

    # initilaize the game by creating a deck and assigning names of players that will play the game
    def __init__(self, *names):

        """Set up the deck and deal cards to 4 players"""

        deck = Deck.create(shuffle=True)

        self.names = (list(names) + "P1 P2 P3 P4".split())[:4]

        # create the hands of the players by using a dictionary comprehension which zips each player with an index in the tuple returned by deck.deal
        self.hands = {

            n: Player(n, h) for n, h in zip(self.names, deck.deal(4))

        }

    # define a play instance method which allows the players to play the game
    def play(self):

        """Play a card game"""

        # get a random player to start with
        start_player = random.choice(self.names)

        # define our turn order using the player_order function
        turn_order = self.player_order(start=start_player)


        # Play cards from each player's hand until empty

        while self.hands[start_player].hand.cards:

            for name in turn_order:

                self.hands[name].play_card()

            print()

    # define a instance method called player_order, which takes in the instance object and a parameter called start with a default value of None
    def player_order(self, start=None):

        """Rotate player order so that start goes first"""

        #if the start is None, get a random player to start with
        if start is None:

            start = random.choice(self.names)

        # get the index of the starting player from the list of names
        start_idx = self.names.index(start)

        # return the reorded list of names, given the starting player
        return self.names[start_idx:] + self.names[:start_idx]

# if the program is called as the main program run code below
if __name__ == "__main__":

    # Read player names from command line

    player_names = sys.argv[1:]

    # start a game by creating a game and passing in the player_names using the splat operator, this maps the names into positional arguments
    game = Game(*player_names)

    # play the game
    game.play()

#------------ Code Section 52 -----------------------

# this is our card class from above, see comments above
# the self argument of the methods do not need to be annotated, as it will always be a class instance
class Card:

    SUITS = "♠ ♡ ♢ ♣".split()

    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


    def __init__(self, suit: str, rank: str) -> None:

        self.suit = suit

        self.rank = rank


    def __repr__(self) -> str:

        return f"{self.suit}{self.rank}"

#------------ Code Section 53 -----------------------

# instead of having a generic cards parameter in our init, we can specify that cards is a list of Card types.
# we can use a Class as a type
class Deck:

    def __init__(self, cards: List[Card]) -> None:

        self.cards = cards

#------------ Code Section 54 -----------------------

# this is a modification to the Deck class to have our create function return a type of Deck
# we cannot just add Deck because the Deck class is not fully yet defined
class Deck:

    @classmethod

    #instead we use a string literal for the annotation, which will be evaluated later by the type checker
    def create(cls, shuffle: bool = False) -> "Deck":

        """Create a new deck of 52 cards"""

        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]

        if shuffle:

            random.shuffle(cards)

        return cls(cards)

#------------ Code Section 55 -----------------------

# this a modified version of the player class where the player's hand is annotated as a Deck, which is possible since Deck is fully defined before we define our player
class Player:

    def __init__(self, name: str, hand: Deck) -> None:

        self.name = name

        self.hand = hand

#------------ Code Section 56 -----------------------

# we can avoid using string literals for type annotations by using the __future__ import to work with postponing evaluations of annotations until they are needed
from __future__ import annotations

class Deck:
    @classmethod
    def create(cls, shuffle: bool = False) -> Deck:
        ...

#------------ Code Section 57 -----------------------

# dogs.py

# import date from the datetime module
from datetime import date

# define a class called Animal
class Animal:

    # we intialize the class with a instance method that takes in the instance object, a str called name, and a date called a birthday, and returns a None
    def __init__(self, name: str, birthday: date) -> None:

        self.name = name

        self.birthday = birthday

    # define a class method called newborn which takes in the cls parameter and a str called name and has a string literal of "Animal" as a type annotation
    # since Animal is not fully defined yet
    @classmethod

    def newborn(cls, name: str) -> "Animal":
        # return the result of the factory method to create a newborn animal
        return cls(name, date.today())

    # define a instance method called twin which takes in the instance object and a str called name and will return an Animal
    def twin(self, name: str) -> "Animal":
        # set the cls variable to be an Animal
        cls = self.__class__
        # return the result of the factory method to create a twin of the provided animal
        return cls(name, self.birthday)

# create a class Dog which inherits from Animal
class Dog(Animal):
    # define an instance method called bark which takes in the instance object and returns a None
    def bark(self) -> None:
        # print the <The Dog's Name> says woof!
        print(f"{self.name} says woof!")

# define fido as a newborn dog
fido = Dog.newborn("Fido")

# define pluto as a twin of Fido
pluto = fido.twin("Pluto")

# make the dogs bark
fido.bark()

pluto.bark()

#------------ Code Section 58 -----------------------

# dogs.py

#this is a modification of the Animal and dog class using TAnimal as a type variable with a bound of Animal to make sure what is passed to the cls or self.
from datetime import date
from typing import Type, TypeVar

TAnimal = TypeVar("TAnimal", bound="Animal")

class Animal:
    def __init__(self, name: str, birthday: date) -> None:
        self.name = name
        self.birthday = birthday

    @classmethod
    def newborn(cls: Type[TAnimal], name: str) -> TAnimal:
        return cls(name, date.today())

    def twin(self: TAnimal, name: str) -> TAnimal:
        cls = self.__class__
        return cls(name, self.birthday)

class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} says woof!")

fido = Dog.newborn("Fido")
pluto = fido.twin("Pluto")
fido.bark()
pluto.bark()

#------------ Code Section 59 -----------------------

# this is a modification to the game class from earlier to have an annotation of str where *names is used to pack the given names from the commandline into a tuple
# when using this technique, the annotation for names should be str, even though it will be a Tuple of strings.
class Game:

    def __init__(self, *names: str) -> None:

        """Set up the deck and deal cards to 4 players"""

        deck = Deck.create(shuffle=True)

        self.names = (list(names) + "P1 P2 P3 P4".split())[:4]

        self.hands = {

            n: Player(n, h) for n, h in zip(self.names, deck.deal(4))

        }

#------------ Code Section 60 -----------------------

# do_twice.py

# import Callable from the typing module
from typing import Callable

# define a function do twice where our function parameter is a callable (representing a function) that takes in a string and returns a None
def do_twice(func: Callable[[str], str], argument: str) -> None:
    # we then print the result of calling our function twice
    print(func(argument))

    print(func(argument))

# define a function called create_greeting which takes in a name and returns a string
def create_greeting(name: str) -> str:

    return f"Hello {name}"

# we then call do_twice, passing in our create greeting function and a Name of "Jekyll"
do_twice(create_greeting, "Jekyll")

#------------ Code Section 61 -----------------------
# hearts.py

#import Counter, random, sys, Any, Dict, List, Optional, Sequence, Tuple, Union, and overload
from collections import Counter
import random
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from typing import overload

# define a card class that has a Suit and a rank and a property called value, which is its rank as a number
# a crad also has a property of points to determine how many points a card is worth in the hearts game
class Card:
    SUITS = "♠ ♡ ♢ ♣".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    @property
    def value(self) -> int:
        """The value of a card is rank as a number"""
        return self.RANKS.index(self.rank)

    @property
    def points(self) -> int:
        """Points this card is worth"""
        if self.suit == "♠" and self.rank == "Q":
            return 13
        if self.suit == "♡":
            return 1
        return 0

    # __eq__ and __lt__ determine whether a card is equal in rank to another rank or less than another card's rank
    def __eq__(self, other: Any) -> Any:
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other: Any) -> Any:
        return self.value < other.value

    # __repr__ return the formatted string representing the card
    def __repr__(self) -> str:
        return f"{self.suit}{self.rank}"

# our Deck class is very similar to the Deck class in the original card game, but adds some new methods and overloaded methods
class Deck(Sequence[Card]):
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    @classmethod
    def create(cls, shuffle: bool = False) -> "Deck":
        """Create a new deck of 52 cards"""
        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)

    # defines the ability to play one card by removing it from the deck
    def play(self, card: Card) -> None:
        """Play one card by removing it from the deck"""
        self.cards.remove(card)

    # defines the ability to deal the cards into a number of hands
    def deal(self, num_hands: int) -> Tuple["Deck", ...]:
        """Deal the cards in the deck into a number of hands"""
        return tuple(self[i::num_hands] for i in range(num_hands))

    # defines the ability to add cards to the Deck
    def add_cards(self, cards: List[Card]) -> None:
        """Add a list of cards to the deck"""
        self.cards += cards

    # defines the ability to get the length of the deck
    def __len__(self) -> int:
        return len(self.cards)

    # multiple overloads for __getitem__ which can get a slice of the deck or a card at a specific key
    # the overload decorator is used in type relationships that are hard to express using Union or type variables
    @overload
    def __getitem__(self, key: int) -> Card: ...

    @overload
    def __getitem__(self, key: slice) -> "Deck": ...

    def __getitem__(self, key: Union[int, slice]) -> Union[Card, "Deck"]:
        if isinstance(key, int):
            return self.cards[key]
        elif isinstance(key, slice):
            cls = self.__class__
            return cls(self.cards[key])
        else:
            raise TypeError("Indices must be integers or slices")

    # defines the abilty to represent a deck by representing each card in the Deck
    def __repr__(self) -> str:
        return " ".join(repr(c) for c in self.cards)

# define a Player which has a name and a hand of cards.
class Player:
    def __init__(self, name: str, hand: Optional[Deck] = None) -> None:
        self.name = name
        self.hand = Deck([]) if hand is None else hand

    # define the ability to list which cards are playable this round
    def playable_cards(self, played: List[Card], hearts_broken: bool) -> Deck:
        """List which cards in hand are playable this round"""
        if Card("♣", "2") in self.hand:
            return Deck([Card("♣", "2")])

        lead = played[0].suit if played else None
        playable = Deck([c for c in self.hand if c.suit == lead]) or self.hand
        if lead is None and not hearts_broken:
            playable = Deck([c for c in playable if c.suit != "♡"])
        return playable or Deck(self.hand.cards)

    # define the ability to list playable cards the are guaranteed to not win the trick
    def non_winning_cards(self, played: List[Card], playable: Deck) -> Deck:
        """List playable cards that are guaranteed to not win the trick"""
        if not played:
            return Deck([])

        lead = played[0].suit
        best_card = max(c for c in played if c.suit == lead)
        return Deck([c for c in playable if c < best_card or c.suit != lead])

    # define the ability to play a card by getting the playable and non_winning cards and determing whether points are important, then chooses an appropraite card from their hand
    def play_card(self, played: List[Card], hearts_broken: bool) -> Card:
        """Play a card from a cpu player's hand"""
        playable = self.playable_cards(played, hearts_broken)
        non_winning = self.non_winning_cards(played, playable)

        # Strategy
        if non_winning:
            # Highest card not winning the trick, prefer points
            card = max(non_winning, key=lambda c: (c.points, c.value))
        elif len(played) < 3:
            # Lowest card maybe winning, avoid points
            card = min(playable, key=lambda c: (c.points, c.value))
        else:
            # Highest card guaranteed winning, avoid points
            card = max(playable, key=lambda c: (-c.points, c.value))
        self.hand.cards.remove(card)
        print(f"{self.name} -> {card}")
        return card

    # defines the ability to determine if a player has a card
    def has_card(self, card: Card) -> bool:
        return card in self.hand

    # defines the ability for a player to represent itself as a string
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r}, {self.hand})"

# defines a human player class which inherits from Player with a new play_card method and returns the card the player played.
class HumanPlayer(Player):
    def play_card(self, played: List[Card], hearts_broken: bool) -> Card:
        """Play a card from a human player's hand"""
        playable = sorted(self.playable_cards(played, hearts_broken))
        p_str = "  ".join(f"{n}: {c}" for n, c in enumerate(playable))
        np_str = " ".join(repr(c) for c in self.hand if c not in playable)
        print(f"  {p_str}  (Rest: {np_str})")
        while True:
            try:
                card_num = int(input(f"  {self.name}, choose card: "))
                card = playable[card_num]
            except (ValueError, IndexError):
                pass
            else:
                break
        self.hand.play(card)
        print(f"{self.name} => {card}")
        return card

# define a class to represent the hearts game that has a list of names of the players, the general players and the human players.
class HeartsGame:
    def __init__(self, *names: str) -> None:
        self.names = (list(names) + "P1 P2 P3 P4".split())[:4]
        self.players = [Player(n) for n in self.names[1:]]
        self.players.append(HumanPlayer(self.names[0]))

    # defines the ability to play the game of hearts until a player goes bust by the given ruleset
    def play(self) -> None:
        """Play a game of Hearts until one player go bust"""
        score = Counter({n: 0 for n in self.names})
        while all(s < 100 for s in score.values()):
            print("\nStarting new round:")
            round_score = self.play_round()
            score.update(Counter(round_score))
            print("Scores:")
            for name, total_score in score.most_common(4):
                print(f"{name:<15} {round_score[name]:>3} {total_score:>3}")

        winners = [n for n in self.names if score[n] == min(score.values())]
        print(f"\n{' and '.join(winners)} won the game")

    # defines the ability to play a round of the Hearts game by creating a Deck and adding cards to the players' hands.
    # then choose the start player and define the tricks variable using a dictionary comprehension
    def play_round(self) -> Dict[str, int]:
        """Play a round of the Hearts card game"""
        deck = Deck.create(shuffle=True)
        for player, hand in zip(self.players, deck.deal(4)):
            player.hand.add_cards(hand.cards)
        start_player = next(
            p for p in self.players if p.has_card(Card("♣", "2"))
        )
        tricks = {p.name: Deck([]) for p in self.players}
        hearts = False

        # Play cards from each player's hand until empty
        while start_player.hand:
            played: List[Card] = []
            turn_order = self.player_order(start=start_player)
            for player in turn_order:
                card = player.play_card(played, hearts_broken=hearts)
                played.append(card)
            start_player = self.trick_winner(played, turn_order)
            tricks[start_player.name].add_cards(played)
            print(f"{start_player.name} wins the trick\n")
            hearts = hearts or any(c.suit == "♡" for c in played)
        return self.count_points(tricks)

    # define the ability to get the player order for the game
    def player_order(self, start: Optional[Player] = None) -> List[Player]:
        """Rotate player order so that start goes first"""
        if start is None:
            start = random.choice(self.players)
        start_idx = self.players.index(start)
        return self.players[start_idx:] + self.players[:start_idx]

    # using the static method decorator converts a function to be a static method

    # define the abilit to get the trick winner from the 0th position of the tricks and then getting the valid tricks and players. then return the maximum of the valid list and then returning position 1
    @staticmethod
    def trick_winner(trick: List[Card], players: List[Player]) -> Player:
        lead = trick[0].suit
        valid = [
            (c.value, p) for c, p in zip(trick, players) if c.suit == lead
        ]
        return max(valid)[1]

    # static method to count the points
    @staticmethod
    def count_points(tricks: Dict[str, Deck]) -> Dict[str, int]:
        return {n: sum(c.points for c in cards) for n, cards in tricks.items()}

# start the game if the program is started as the main program
if __name__ == "__main__":
    # Read player names from the command line
    player_names = sys.argv[1:]
    game = HeartsGame(*player_names)
    game.play()

#------------ Code Section 62 -----------------------

# cosine.py

# import numpy as the np alias
import numpy as np

# define a function called print_cosine, which takes in a parameter x with a type of np.ndarray and returns a None
def print_cosine(x: np.ndarray) -> None:
    # with the specified print options, print the cosine of x
    with np.printoptions(precision=3, suppress=True):

        print(np.cos(x))

# set x to be the result of the linspace function, which returns evenly spaced numbers over a specified intervale
# 0 is the start, 2 * pi is the stop, and 9 is the number of spaces to fill

x = np.linspace(0, 2 * np.pi, 9)

# call print cosine on x
print_cosine(x)

#------------ Code Section 63 -----------------------

# the numpy warning can be silenced by adding a type comment to the line containing the import
import numpy as np  # type: ignore

#------------ Code Section 64 -----------------------

# parse_name.py

# import the parse module, which can recognize simple patterns
import parse

# define a function called parse_name, which takes in a str called text and returns a str
def parse_name(text: str) -> str:

    # define the patterns to look for in a tuple
    patterns = (

        "my name is {name}",

        "i'm {name}",

        "i am {name}",

        "call me {name}",

        "{name}",

    )

    # foreach pattern in patterns, set the result to the result of parsing the text with the pattern
    for pattern in patterns:

        result = parse.parse(pattern, text)

        # if the result is not empty, return the result for the name found
        if result:

            return result["name"]

    # return the empty string as a default case
    return ""

# get what result to what is your name.
answer = input("What is your name? ")

#try and parse the name from the answer
name = parse_name(answer)

# print hi to the parsed name
print(f"Hi {name}, nice to meet you!")

#------------ Code Section 65 -----------------------
# parse.pyi

# import Any, Mapping, Optional, Sequence, Tuple, and Union from the typing module
from typing import Any, Mapping, Optional, Sequence, Tuple, Union

# this adds type hints in order for MyPy to type check the use of parse.parse()
# define a Result class which takes fixed sequence of str, a mapping of strs, and a mapping of spans
class Result:
    def __init__(
        self,
        fixed: Sequence[str],
        named: Mapping[str, str],
        spans: Mapping[int, Tuple[int, int]],
    ) -> None: ...

    # define a method to get the union of an item and return a str
    def __getitem__(self, item: Union[int, str]) -> str: ...

    # define the ability to represent a result as a str
    def __repr__(self) -> str: ...

# define a function called parrse which takes in a str format and a str to evaluate, a bool called evaluate_result and bool called case_sensitive and returns an Optional[Result]
def parse(
    format: str,
    string: str,
    evaluate_result: bool = ...,
    case_sensitive: bool = ...,
) -> Optional[Result]: ...

# this will introduce a bug that shows an error saying incompatible return value type.
# when return result is changed back to return result["name"], MyPy will be happy