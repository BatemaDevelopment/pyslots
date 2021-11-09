import random as rand

def main():
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
    
      if user_ans == "y" or user_ans == "Y" or userAnswer == "yes" or user_ans == "Yes":
        print(divider_msg)
        print(slots_msg)
        print(divider_msg)
      else:
        print(stopping_msg)
        print(divider_msg)
        break
    
    slot_one = rand.randint(1,6)
    print(slot_one)
  
    slot_two = rand.randint(1,6)
    print(slot_two)
  
    slot_three = rand.randint(1,6)
    print(slot_three)
  
    print(divider_msg)
    money_gambled = rand.randrange(100,500,100)
  
    if slot_one == slot_two == slot_three:
      current_money += money_gambled
      print("$" + str(current_money) + ".00")
      print(divider_msg)
    else:
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
    
if __name__ == "__main__":
  main()