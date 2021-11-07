import random as rand

currentMoney = 1000
timesLooped = 0
userInput = "Press \"Y\" to continue, or press anything else to end:"

print("==========")
print("Slot Numbers")
print("==========")

while currentMoney > 0:
  if timesLooped >= 2:
    print(userInput)
    print("==========")
    userAnswer = input()
    
    if userAnswer == "y" or userAnswer == "Y" or userAnswer == "yes" or userAnswer == "Yes":
      print("==========")
      print("Slot Numbers")
      print("==========")
    else:
      print("Stopping...")
      print("==========")
      break
    
  slotOne = rand.randint(1,6)
  print(slotOne)
  slotTwo = rand.randint(1,6)
  print(slotTwo)
  slotThree = rand.randint(1,6)
  print(slotThree)
  print ("==========")
  
  moneyGambled = rand.randrange(100,500,100)
  
  if slotOne == slotTwo == slotThree:
    currentMoney += moneyGambled
    print("$" + str(currentMoney) + ".00")
    print("==========")
  else:
    currentMoney -= moneyGambled
    if currentMoney < 0:
      currentMoney = 0
      
      print("$" + str(currentMoney) + ".00")
      
      print("==========")
      print("Stopping...")
      print("==========")
      
      break
    elif currentMoney == 0:
      print("$" + str(currentMoney) + ".00")
      
      print("==========")
      print("Stopping...")
      print("==========")
      
      break
    else:
      print("$" + str(currentMoney) + ".00")
      print("==========")
  
  timesLooped += 1