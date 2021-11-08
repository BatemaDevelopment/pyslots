import random as rand

def main():
  currentMoney = 1000
  timesLooped = 0
  userInput = "Press \"Y\" to continue, or press anything else to end:"
  stoppingMsg = "Stopping..."
  dividerMsg = "=========="
  slotsMessage = "Slot Numbers"

  print(dividerMsg)
  print(slotsMessage)
  print(dividerMsg)

  while currentMoney > 0:
    if timesLooped >= 1:
      print(userInput)
      print(dividerMsg)
      userAnswer = input()
    
      if userAnswer == "y" or userAnswer == "Y" or userAnswer == "yes" or userAnswer == "Yes":
        print(dividerMsg)
        print(slotsMessage)
        print(dividerMsg)
      else:
        print(stoppingMsg)
        print(dividerMsg)
        break
    
    slotOne = rand.randint(1,6)
    print(slotOne)
  
    slotTwo = rand.randint(1,6)
    print(slotTwo)
  
    slotThree = rand.randint(1,6)
    print(slotThree)
  
    print(dividerMsg)
    moneyGambled = rand.randrange(100,500,100)
  
    if slotOne == slotTwo == slotThree:
      currentMoney += moneyGambled
      print("$" + str(currentMoney) + ".00")
      print(dividerMsg)
    else:
      currentMoney -= moneyGambled
      if currentMoney < 0:
        currentMoney = 0
      
        print("$" + str(currentMoney) + ".00")
    
        print(dividerMsg)
        print(stoppingMsg)
        print(dividerMsg)
      
        break
      elif currentMoney == 0:
        print("$" + str(currentMoney) + ".00")
    
        print(dividerMsg)
        print(stoppingMsg)
        print(dividerMsg)
        break
      else:
        print("$" + str(currentMoney) + ".00")
        print(dividerMsg)
    timesLooped += 1
    
if __name__ == "__main__":
  main()