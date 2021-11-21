import random as rand
import sys, os
from . import __init__ as __init__
from . import original_gamemode as og_gm
from . import user_input_gamemode as user_input_gm
from .other_games import menu as other_games_menu 
from .args import parse_args
from .update import update

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

        print(input_msg + "\n" + divider_msg)

        user_game_selection = input()
        if user_game_selection == "1":
            og_gm.og_game()
        elif user_game_selection == "2":
            user_input_gm.user_input_game()
        elif user_game_selection == "3":
            other_games_menu()
        elif user_game_selection == "4":
            print("Sorry to see you go! Hope you come visit soon!")
            sys.exit(0)
        else:
            print("Error 404: Game Not Found")
            sys.exit(404)
    try:
        if args.help:
            sys.exit(0)
    except AttributeError:
        pass

if __name__ == "__main__":
    main()