import urllib.request, sys, os
from .args import parse_args

args = parse_args()

def update():
    try:
        # print("Checking for newer versions, then updating if any...")
        url = f"https://raw.githubusercontent.com/Lukas-Batema/pyslots/{'1.2.0' if args.mcrefvers else 'master'}/PYSlots/resources/pyslots_ids.json"
        urllib.request.urlretrieve(
            url, os.path.dirname(__file__) + "/resources/pyslots.json"
        )
        sys.exit(0)
    except:
        pass