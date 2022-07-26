import random
import time
from time import sleep, strftime

money = 1000


#Write your game of chance functions here
print("----------Welcome to the casino----------")
sleep(1)
print ("Today is: " + strftime("%A %B %d, %Y"))
print ("------" + strftime("%H") + ":" + strftime("%M") + ":" + strftime("%S") + "-----")
sleep(1)

print("\nYou have £", money, "\n")

#-----------------------------------Heads or Tails game logic---------------------------------
def headsOrTails(amount, bet):
  print("""                                                                                                                            
                            ████████████                                                
                        ██████      ████████                                            
                      ████              ████                                            
                      ██            ██    ████                                          
                    ████            ██    ████                                          
                    ██              ██      ████                                        
                    ██              ██      ████                                        
                    ██              ██      ████                                        
                    ██              ██      ████                                        
                    ██              ██      ████                                        
                    ██              ██      ████                                        
                    ████            ██    ████                                          
                      ██      ████████    ████                                          
                      ████              ████                                            
                        ██████      ████████                                            
                            ████████████                                                                                                                               
        """)
  global money
  decision = random.randint(1,2)
  if decision == 1:
    print("--------The coin lands on heads--------")
    sleep(1)
    if bet.lower() == "heads":
      winnings = amount
      money = money + winnings
      print("You won £", winnings)  
      print("You now have £", money)
      sleep(1)
    elif bet.lower() == "tails":
      losings = amount
      money = money - losings
      print("You Lost £", losings)
      print("You now have £", money)
      sleep(1)
  elif decision == 2:
    print("--------The coin lands on Tails--------")
    sleep(1)
    if bet.lower() == "tails":
      winnings = amount
      money = money + winnings
      print("You won £", winnings)  
      print("You now have £", money)
      sleep(1)
    elif bet.lower() == "heads":
      losings = amount
      money = money - losings
      print("You Lost £", losings)
      print("You now have £", money)
      sleep(1)

       

#-----------------------------------Cho-Han game logic------------------------------------
def ChoHan(amount, bet):
  global money
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,6)
  sum = roll1 + roll2
  if sum % 2 == 0:
    print("The number is", sum)
    print("--------Even Wins--------")
    sleep(1)
    if bet.lower() == "even":
      winnings = amount
      money = money + winnings
      print("You won £", winnings)  
      print("You now have £", money)
      sleep(1)
    elif bet.lower() == "odd":
      losings = amount
      money = money - losings
      print("You Lost £", losings)
      print("You now have £", money)
      sleep(1)
  elif sum % 2 == 1:
    print("The number is", sum)
    print("--------Odd Wins--------")
    sleep(1)
    if bet.lower() == "odd":
      winnings = amount
      money = money + winnings
      print("You won £", winnings)  
      print("You now have £", money)
      sleep(1)
    elif bet.lower() == "even":
      losings = amount
      money = money - losings
      print("You Lost £", losings)
      print("You now have £", money)
      sleep(1)
    


#-----------------------------------Higher or Lower game logic--------------------------------
def higherCard(amount, bet):
  global money
  decision = random.randint(1,8)
  randomCard = random.randint(1,8)
  if bet.lower() == "y":
    print("Your card is: ", randomCard)
    sleep(1)
    if randomCard > decision:
      print("The opponents card was: ", decision)
      print("\n----------You won!----------")
      winnings = amount
      money = money + winnings
      print("You won £", winnings)  
      print("You now have £", money)
      sleep(1)
    elif randomCard < decision:
      print("The opponents card was: ", decision)
      print("\n----------You lost----------")
      losings = amount
      money = money - losings
      print("You Lost £", losings)
      print("You now have £", money)
      sleep(1)
    else:
      print("The opponents card was: ", decision)
      print("\nIt's a draw")
      sleep(1)
  elif bet.lower() == "n":
    print("You have quit")
    sleep(1)
    

#-----------------------------------Roulette game logic------------------------------------
def roulette(amount, bet):
  global money
  randRoll = str(random.randint(1, 35))
  print(randRoll, "Was rolled")
  sleep(1)
  if bet == randRoll:
    print("You win")
    winnings = amount * 35
    money = money + winnings
    print("You won £", winnings)  
    print("You now have £", money)
    sleep(1)
  elif int(randRoll) % 2 == 0:
    if bet.lower() == "black":
      winnings = amount
      money = money + winnings
      print("You won £", winnings)  
      print("You now have £", money)
      sleep(1)
    elif bet.lower() == "red":
      losings = amount
      money = money - losings
      print("You Lost £", losings)
      print("You now have £", money)
      sleep(1)
  elif bet != randRoll:
      losings = amount
      money = money - losings
      print("You Lost £", losings)
      print("You now have £", money)
      sleep(1)


#-----------------------------------Start of Game-------------------------------------------

end2 = 0
while True:
  print("Loading Games....")

  
  sleep(2)
  print("\nWhat game would you like to play?")
  game = input(" \n1) Heads or Tails, 2) Cho-Han, 3) Higher or Lower, 4) Roulette\n")
  
  
  if game == "1":
    print("----------You are playing Heads or Tails----------")
    while True:
      try:
        amount = int(input("\nEnter the amount you'd like to bet: "))
        break
      except ValueError:
        print("Please input integer only...")  
      continue
    while True:
      if amount <= 0:
        print("You cannot enter 0 or a negative number")
        amount = int(input("Enter the amount you'd like to bet: "))
      elif amount <= money:
        break
      else:
        print("You dont have that much!")
        amount = int(input("Enter the amount you'd like to bet: "))
    bet = str(input("Heads or Tails?: "))
    headsOrTails(amount, bet)
    end2 = 1
    break
    
  elif game == "2":
    print("----------You are playing Cho-Han----------")
    while True:
      try:
        amount = int(input("\nEnter the amount you'd like to bet: "))
        break
      except ValueError:
        print("Please input integer only...")  
      continue
    while True:
      if amount <= 0:
        print("You cannot enter 0 or a negative number")
        amount = int(input("Enter the amount you'd like to bet: "))
      elif amount <= money:
        break
      else:
        print("You dont have that much!")
        amount = int(input("Enter the amount you'd like to bet: "))

    while True:
      bet = str(input("Odd or Even: "))
      allowed = ['odd', 'even']
      if bet.lower() in allowed:
        break
      else:
        print("invalid input")
        continue
 
    ChoHan(amount, bet)
    end2 = 1
    break
    
    
  elif game == "3":
    print("----------You are playing Higher or Lower----------")
    while True:
      try:
        amount = int(input("\nEnter the amount you'd like to bet: "))
        break
      except ValueError:
        print("Please input integer only...")  
      continue
    while True:
      if amount <= 0:
        print("You cannot enter 0 or a negative number")
        amount = int(input("Enter the amount you'd like to bet: "))
      elif amount <= money:
        break
      else:
        print("You dont have that much!")
        amount = int(input("Enter the amount you'd like to bet: "))
    bet = str(input("\nWould you like to pick a random card? y/n "))
    higherCard(amount, bet)
    end2 = 1
    break
    
  elif game == "4":
    print("----------You are playing Roulette----------")
    while True:
      try:
        amount = int(input("\nEnter the amount you'd like to bet: "))
        break
      except ValueError:
        print("Please input integer only...")  
      continue
    while True:
      if amount <= 0:
        print("You cannot enter 0 or a negative number")
        amount = int(input("Enter the amount you'd like to bet: "))
      elif amount <= money:
        break
      else:
        print("You dont have that much!")
        amount = int(input("Enter the amount you'd like to bet: "))
    
    while True:
      bet = str(input("Pick a single number for 35x returns or black or red for 2x: "))
      allowed = ['black', 'Black', 'red', 'Red', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
      if bet in allowed:
        break
      else:
        print("invalid input")
    roulette(amount, bet)
    end2 = 1
    break
  else:
    print("not valid")
    end2 = 1
    break

    
  
endGame = str(input("\nWould you like to play another game?\n"))

if endGame.lower() == "no":
  print("Game Ending....")
  sleep(2)
  quit()

#-----------------------------------Main Game Loop--------------------------------------------
end=0
while money > 0:        
  
  print("What game would you like to play?")
  game = input(" \n1) Heads or Tails, 2) Cho-Han, 3) Higher or Lower, 4) Roulette\n")
  

  
  if game == "1":
    print("----------You are playing Heads or Tails----------")
    while True:
      try:
        amount = int(input("\nEnter the amount you'd like to bet: "))
        break
      except ValueError:
        print("Please input integer only...")  
      continue
    while True:
      if amount <= 0:
        print("You cannot enter 0 or a negative number")
        amount = int(input("Enter the amount you'd like to bet: "))
      elif amount <= money:
        break
      else:
        print("You dont have that much!")
        amount = int(input("Enter the amount you'd like to bet: "))
    bet = str(input("Heads or Tails?: "))
    headsOrTails(amount, bet)
    
  elif game == "2":
    print("----------You are playing Cho-Han----------")
    while True:
      try:
        amount = int(input("\nEnter the amount you'd like to bet: "))
        break
      except ValueError:
        print("Please input integer only...")  
      continue
    while True:
      if amount <= 0:
        print("You cannot enter 0 or a negative number")
        amount = int(input("Enter the amount you'd like to bet: "))
      elif amount <= money:
        break
      else:
        print("You dont have that much!")
        amount = int(input("Enter the amount you'd like to bet: "))
    while True:
      bet = str(input("Odd or Even: "))
      allowed = ['odd', 'even']
      if bet.lower() in allowed:
        break
      else:
        print("invalid input")
        
 
    ChoHan(amount, bet)
    end2 = 1
    
  elif game == "3":
    print("----------You are playing Higher or Lower----------")
    while True:
      try:
        amount = int(input("\nEnter the amount you'd like to bet: "))
        break
      except ValueError:
        print("Please input integer only...")  
      continue
    while True:
      if amount <= 0:
        print("You cannot enter 0 or a negative number")
        amount = int(input("Enter the amount you'd like to bet: "))
      elif amount <= money:
        break
      else:
        print("You dont have that much!")
        amount = int(input("Enter the amount you'd like to bet: "))
    bet = str(input("\nWould you like to pick a random card? y/n "))
    higherCard(amount, bet)
    
  elif game == "4":
    print("----------You are playing Roulette----------")
    while True:
      try:
        amount = int(input("\nEnter the amount you'd like to bet: "))
        break
      except ValueError:
        print("Please input integer only...")  
      continue
    while True:
      if amount <= 0:
        print("You cannot enter 0 or a negative number")
        amount = int(input("Enter the amount you'd like to bet: "))
      elif amount <= money:
        break
      else:
        print("You dont have that much!")
        amount = int(input("Enter the amount you'd like to bet: "))
    while True:
      bet = str(input("Pick a single number for 35x returns or black or red for 2x: "))
      allowed = ['black', 'Black', 'red', 'Red', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
      if bet in allowed:
        break
      else:
        print("invalid input")
    roulette(amount, bet)
  else:
    print("not valid")

  
print("You lost all your money")

