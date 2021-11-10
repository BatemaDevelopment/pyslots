import random as rand
import sys, os
from . import __init__ as __init__
from .args import parse_args
from .update import update


def main():
    args = parse_args()

    if args.update:
        print("This feature currently does not work. Please use 'pip install --upgrade pyslots', to update.")
        sys.exit(0)
        # update()
    if args.version:
        print("This feature currently does not work! Check back later.")
        # print("PYSlots Version:", __init__.VERSION)
        sys.exit(0)
    else:
        current_money = 1000
        times_looped = 0
        user_input = "Press \"Y\" to continue, or press anything else to end:"
        stopping_msg = "Stopping..."
        divider_msg = "=========="
        slots_msg = "Slot Numbers"

        print(divider_msg)
        print(slots_msg)
        print(divider_msg)

        while current_money > 0:
            if times_looped >= 1:
                print(user_input)
                print(divider_msg)
                user_ans = input()

                if user_ans == "y" or user_ans == "Y" or user_ans == "yes" or user_ans == "Yes":
                    print(divider_msg)
                    print(slots_msg)
                    print(divider_msg)
                else:
                    print(stopping_msg)
                    print(divider_msg)
                    break

            slot_one = rand.randint(1, 6)
            print(slot_one)

            slot_two = rand.randint(1, 6)
            print(slot_two)

            slot_three = rand.randint(1, 6)
            print(slot_three)

            print(divider_msg)
            money_gambled = rand.randrange(100, 500, 1)

            if slot_one == slot_two == slot_three:
                current_money += round(money_gambled, None)
                print("$" + str(current_money) + ".00")
                print(divider_msg)
            elif slot_one == slot_two or slot_two == slot_three:
                current_money += round(money_gambled / 4, None)
                print("$" + str(current_money) + ".00")
                print(divider_msg)
            elif slot_one == slot_three:
                current_money += round(money_gambled / 16, None)
                print("$" + str(current_money) + ".00")
                print(divider_msg)
            elif slot_one != slot_two != slot_three:
                current_money -= money_gambled
                if current_money < 0:
                    current_money = 0

                    print("$" + str(current_money) + ".00")

                    print(divider_msg)
                    print(stopping_msg)
                    print(divider_msg)

                    break
                elif current_money == 0:
                    print("$" + str(current_money) + ".00")

                    print(divider_msg)
                    print(stopping_msg)
                    print(divider_msg)
                    break
                else:
                    print("$" + str(current_money) + ".00")
                    print(divider_msg)
            times_looped += 1
    try:
        if args.help:
            sys.exit(0)
    except AttributeError:
        pass

if __name__ == "__main__":
    main()