# import modules
import random as rand
import sys, os
from . import __init__ as __init__
from . import original_gamemode as og_gm
from . import user_input_gamemode as user_input_gm
from .other_games import menu as other_games_menu 
from .args import parse_args
from .update import update
# --------------------------------------------------
def main():
    """
    main():
        - Description: 
            The Main Menu Page
        - Arguments:
            None
    """

    args = parse_args()

    if args.update:
        update()
        sys.exit(0)
    if args.version:
        print("PYSlots Version:", __init__.VERSION)
        sys.exit(0)
    else:
        input_msg = "Welcome to PYSlots! Type in the number of the game you want to play!\n1) Original (Originated in v1.1.1)\n2) Manual Gamble (Originated in 1.3.0)\n3) Other Games\n4) Quit"
        divider_msg = "=========="

        print(input_msg + "\n" + divider_msg) # 

        user_game_selection = input()
        if user_game_selection == "1": # If the user inputs the number 1, start the "original game"
            og_gm.og_game() # Start the "original game"
        elif user_game_selection == "2": # If the user inputs the number 2, start the "user input game"
            user_input_gm.user_input_game() # Start the "user input game"
        elif user_game_selection == "3": # If the user inputs the number 3, go to the "other games" menu
            other_games_menu() # Open the "other games menu"
        elif user_game_selection == "4": # If the user inputs the number 4, exit the programme
            print("Sorry to see you go! Hope you come visit soon!") # Print the apology message
            sys.exit(0) # Exit the programme
        else:
            print("Error 404: Game Not Found") # Uh oh, they inputted a number that is not in the range from 1 to 4... That's a lot of damage...
            sys.exit(404) # Exit with the 404 Code (lol)
    try:
        if args.help: # If the argument given is --help, run the below code
            sys.exit(0) # Exit programme
    except AttributeError: # A wild Attribute Error appears...
        pass # Ash Ketchum ran from the wild Attribute Error...

if __name__ == "__main__":
    main()