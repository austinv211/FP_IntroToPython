# play.py

# define a function called play that takes in a str parameter player_name
# and returns Nothing. The None type hint is used to help identify
# a useless return value
def play(player_name: str) -> None:
    print(f"{player_name} plays")

# this will trigger an error because we are trying to assign a non-return to a variable
ret_val = play("Filip")
