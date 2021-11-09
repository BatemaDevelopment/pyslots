import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="PYSlots\n" "https://github.com/Lukas-Batema/pyslots"
    )
    parser.add_argument(
        "--mcrefvers",
        action="store_true",
        help="Use the \"Don't look directly at the bugs\" version (Obviously a Minceraft reference...)",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update to the latest stable version",
    )
    parser.add_argument(
        "--version",
        "-v",
        action="store_true",
        help="Print the PYSlots version",
    )

    return parser.parse_args()