import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="PYSlots\n" "https://github.com/Lukas-Batema/pyslots" # Set the description
    )
    parser.add_argument(
        "--mcrefvers", # Set the argument text
        action="store_true", # Store the action
        help="Use the \"Don't look directly at the bugs\" version (Obviously a Minceraft reference...)", # Set the help message
    )
    parser.add_argument(
        "--update", # Set the argument text
        "-u", # Set the shorthand argument text
        action="store_true", # Store the action
        help="Update to the latest stable version", # Set the help message
    )
    parser.add_argument(
        "--version", # Set the argument text
        "-v", # Set the shorthand argument text
        action="store_true", # Store the action
        help="Print the PYSlots version", # Set the help message
    )

    return parser.parse_args() # Return the arguments