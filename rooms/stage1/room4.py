import sys, time, math
from functions import countdownTimer, writeFile, cls, addLives, checkIfAlive, printSkull

def room4():
  cls()

  done4 = open("variables/done4.txt", "r").read()
  if done4 == 1:
    print("You've already been here. You fall through a portal, dropping you back to the main room.")
    import main2
    main2.main2

  print("You slowly open the fourth door to find an exploded nuclear power plant.\n")
  time.sleep(1)
  print("You find yourself inhaling nuclear radiation more and more as you breathe...\n")
  time.sleep(1)
  print("The radiation overtakes you and your skin starts burning.\n\n")

  time.sleep(3)
  for char in "You lose 5 hearts\n\n": 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.25)
  addLives(-5)
  #checkIfAlive()
  time.sleep(3)



  open("variables/done4.txt", "w").write("1")
  import main2
  main2.main2
