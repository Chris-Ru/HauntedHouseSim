
## from variables import gametime
import sys
import time
import math
import random
import os
from functions import checkIfAlive, cls, addLives, writeFile, printSkull, printDoorway
from random import randint, randrange
ANSI_RED = u"\u001b[31m"
ANSI_BLUE = u"\u001B[34m"
ANSI_WHITE = u"\u001B[37m"
RESET_COLOR = u"\u001B[0m\u001B[2D"

# Room1
def room1():
  cls()
  checkIfAlive()

  done1 = int(open("variables/done1.txt", "r").read())
  if done1 == 1:
    print("You've already been here. The door doesn't budge when you try to open it.")
    time.sleep(2)
    import main2
    main2.main2

  def printSkullAnimation(): 
    os.system('cls' if os.name=='nt' else 'clear')
  ANSI_BLUE = u"\u001B[34m"
  RESET_COLOR = u"\u001B[0m\u001B[2D"
  ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2D"
  print(ANSI_BLUE)
  print(" ______")
  print("  ,-'  .-.  `-.")
  print(" /    (o.o)    \ ")
  print("|      |=|      | ")
  print(")     __|__     |")
  print("|   //.=|=.\\   |")
  print("|  // .=|=. \\  (")
  print("|  \\ .=|=. //  |")
  print(")_ !\\(_=_)//   |")
  print("|| . (:| |:)    |")
  print("|  .  || ||.    | ")
  print("|_____() ().____|")
  time.sleep(0.25)
  print(ANSI_HOME_CURSOR)
  print(" ______")
  print("  ,-'  .-.  `-.")
  print(" /    (o.o)    \ ")
  print("|      |=|      | ")
  print(")     __|__     |")
  print("|  // .=|=. \\  |")
  print("| //  .=|=.  \\ (")
  print("| \\  .=|=.  // |")
  print(")_ !\\(_=_) //  |")
  print("|| . (:| |:)    |")
  print("|  .  || ||.    |")
  print("|_____() ().____|")
  time.sleep(0.25)
  print(ANSI_HOME_CURSOR)
  print(" ______")
  print("  ,-'  .-.  `-.")
  print(" /    (o.o)    \ ")
  print("|      |=|      | ")
  print(")     __|__     |")
  print("| //  .=|=.  \\ |")
  print("|//   .=|=.   \\(")
  print("| \\//.=|=.\\// |")
  print(")_    (_=_)     |")
  print("|| . (:| |:)    |")
  print("|  .  || ||.    |")
  print("|_____() ().____|")
  time.sleep(0.25)
  print(ANSI_HOME_CURSOR)
  print(" ______")
  print("  ,-'  .-.  `-.")
  print(" /    (o.o)    \ ")
  print("|      |=|      | ")
  print(")     __|__     |")
  print("| // //=|=\\ \\ |")
  print("| \\//.=|=.\\// (")
  print("|     .=|=.     |")
  print(")_    (_=_)     |")
  print("|| . (:| |:)    |")
  print("|  .  || ||.    |")
  print("|_____() ().____|")
  time.sleep(0.25)
  print(ANSI_HOME_CURSOR)
  print(" ______")
  print("  ,-'  .-.  `-.")
  print(" /    (o.o)    \ ")
  print("|      |=|      | ")
  print(")    _O_|_O_    |")
  print("| // //=|=\\ \\ |")
  print("| \\//.=|=.\\// (")
  print("|     .=|=.     |")
  print(")_    (_=_)     |")
  print("|| . (:| |:)    |")
  print("|  .  || ||.    |")
  print("|_____() ().____|")
  printSkullAnimation()

  numberList = [1,2,2,2,3,3,3,3,3,3,3,3,3,3]
  randomEvent = random.choice(numberList)
  print(RESET_COLOR)
  if randomEvent == 1:
    for char in "You enter the first room. \nIn the center of the room is a dusty coffin with the lid slowly sliding off.\nAs you approach, a thin boney hand bursts out of the coffin, groping for something to crush. \nYou jump back but you were too slow. \nThe hand grabs you and crushes you on the ground, instantly killing you.": 
      print(char, end='') 
      sys.stdout.flush() 
      time.sleep(0.01) 
    printSkull()
    print("Game over.")
    exit()
  if randomEvent == 2:
    for char in "You enter the first room. In the center of the room is a dusty coffin with the lid slowly sliding off. \nAs you approach, a thin boney hand bursts out of the coffin, groping for something to crush. \nThinking fast, you sprint to the coffin and slam the lid on the skeleton, but also, unfortunately, on your other hand.":
      print(char, end='') 
      sys.stdout.flush() 
      time.sleep(0.01)
    time.sleep(2)
    print("You lose 1 life") 
    addLives(-1)
  if randomEvent == 3:
    for char in "You enter the first room. In the center of the room is a dusty coffin with the lid slowly sliding off. \nAs you approach, a thin boney hand bursts out of the coffin, groping for something to crush. \nThinking fast, you sprint to the coffin and slam the lid on teh skeleton. \nAfter the loud slam, there was a deafening silence. At least you didn't get hurt, yet.\n\n":
      print(char, end='') 
      sys.stdout.flush() 
      time.sleep(0.01) 


  def choicemenu1 (): 
    cls()
    time.sleep(0.7)
    print("\n1. Go to the lamp next to the bed.\n" +
          "2. Go to the couch.\n" +
          "3. Go to the dresser\n")

  def choicemenu2 (): 
    cls()
    time.sleep(0.7)
    print("\n1. Continuing your search you now notice a TV remote. You go towards it.")
    print("\n2. Continuing your search you now notice a computer. You go towards the computer.") 
    print("\n3. Continuing your search you now notice a panel in the bottom left corner. You go towards the panel.")

  def choicemenu3():
    cls()
    time.sleep(0.7)
    print("\n1. Moving on you notice a book lying on the table. Go to the book.")
    print("\n2. Moving on you notice a microwave. Go to the microwave.")
    print("\n3. Moving on you notice a shelf. Go to the shelf.")

  def choicemenu4():
    print("\n. ")

  time.sleep(1)
  def processChoice1 (choice) :
    if choice == 1:
      for char in "Once you reach the lamp, you turn it on. The moment you turn it on, metal spikes shoot out of the wall straight towards you. With your reflexes, you were able to dodge most of them in time. Your arm wasn’t so lucky...":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)
      print("You lost one life")
      addLives(-1)
    elif choice == 2:
      for char in "You start moving the couch cussions around and notice a screwdriver. You pick up the screwdriver and place it back down. What could it be used for?":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)
    else:
      for char in "Once you reach the dresser you open it up revealing tons of clothes. You start poking around until a skeleton jumps out of the dresser and falls back down scaring the life out of you. At least it didn’t do anything to you...":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)

  def processChoice2 (choice) :
    if choice == 1:
      for char in "You open up the back of the TV remote but then you notice a band of three colors incorporated within the back. The colors are red, orange and yellow. Uhmm…..":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)
    elif choice == 2:
      for char in "You open up the computer but immediately a video starts to play. It reveals a girl with dark, long black hair wearing a pale colored white dress. She keeps approaching towards the front of your screen when suddenly the lights turn off. When they turn on again she appears in front of you, screeching revealing her terrifying face. Then she disappears…":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)
    else:
      for char in "Once you've reached the panel you begin to tug at it's frame hoping for a way out. Once the frame is removed successfully, a bunch of bugs and insects begin to pour out of the panel spreading across the floor. These bugs began to eat your foot but you quickly shut the frame into the panel preventing anymore from entering. You quickly dispose the rest of the bugs and insects until you notice your foot is severely injured.\n You lost one life.":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)
      addLives(-1)

  def processChoice3 (choice) :
    if choice == 1:
      for char in "Once you reach the table you pick up the book revealing a picture. A hand comes out and grabs your hand injuring it. However a key appears. You are finally able to get out of this horrid room.":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)
        addLives(-1)
    elif choice == 2:
      for char in "You open the microwave door and notice a key. You are finally able to get out of this horrid room":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)
    else:
      for char in "Once you reach the shelf you notice a picture on the shelf. When you're about to pick the picture up, a ghost comes out of the picture scaring the daylights out of you. Thankfully it didn’t do anything….yet.":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.04)

  
  def handleStage1():
    cls()
    choiceCount = 1
    checkIfAlive()

    while(choiceCount <= 4):  
      done1 = int(open("variables/done1.txt", "r").read())
      if done1 == 1:
        print("You've already been here. You fall through a portal, dropping you back to the main room.")
        exec(open("main2.py")).read()
        
      else:
        if ( choiceCount == 1 ):
          choicemenu1()
          choice1 = input("Choose a number: ")
          processChoice1(choice1)
        elif ( choiceCount == 2 ):
          choicemenu2()
          choice2 = input("Choose a number: ")
          processChoice2(choice2)
        elif ( choiceCount == 3 ):
          choicemenu3()
          choice3 = input("Choose a number: ")
          processChoice3(choice3)
      choiceCount += 1
      checkIfAlive()

   
    open("variables/done1.txt", "w").write("1")  
    import main2
    main2.main2()
  handleStage1()

#Room 2
def room2():
#Check if user passes necessary requirements: first time here, enough lives
  cls()
  checkIfAlive()
  done2 = int(open("variables/done2.txt", "r").read())
  if done2 == 1:
    print("You've already been here. You shove the door but it doesn't budge.ANSI_BLUE")
    time.sleep(2)
    import main2
    main2.main2()
    

 else:
    #code that executes when user passes all checks
    item = "nothing"
    #last function to run
    def round3():
      cls()
      print("You venture deeper into the basement")
      print("A zombie appears in front of you!")
      choice = input("[1] - Run off towards the right\n[2] - Attack\n")
      cls()
      if(choice == "1"):
        print("It's a dead end, you re-enter the basement")
        time.sleep(1)
        cls()
        round3()
      if(choice == "2"):
        #different outcomes based on what the user picked previously and stored in item vairable
        if(item == "nothing"):
          print("You punch the zombie with your bare hands")
          time.sleep(1)
          addLives(-2)
          print("The zombie bites into your leg")
          time.sleep(1)
          print("You lose 2 lives")
          checkIfAlive()
          time.sleep(2)
          print("Maybe you should've picked up something from the roof")
          time.sleep(3)
          import main2
          main2.main2()
          checkIfAlive()
          writeFile("variables/done2.txt", "1")
          time.sleep(2)
      
    #second function to run
    def round2():
      print("You open the door and see a ladder going up and a staircase going down")
      choice = input("[1] - Climb the ladder\n[2] - Descend the stairs\n")
      cls()
      #prompt user for item, change outcome based on it
      if(choice == "1"):
        print("The ladder leads to the top of the mansion")
        time.sleep(.7)
        print("There's a sharp sword and 20 dollar steam card")
        itemNum = input("[1] - Take the sword\n[2] - Take the steam card\n")
        cls()
        if(itemNum == "1"):
          print("You grab the sword")
          item = "sword"
        elif(itemNum == "2"):
          item = "steam card"
          print("You grab the steam card")
        else:
          print("You decide not to grab anything")
        print("The view is nice but theres nothing else to do here.")
        time.sleep(2)
        print("You take your item and descend the ladder again")
        time.sleep(2)
        cls()
        round2()
      elif(choice == "2"):
        cls()
        round3()
      else:
        print("Invalid choice, you go through the door again")
        time.sleep(1)
        round2()

    #first called function
    def startMaze():
      cls()
      print("You find yourself in a kitchen\nTheres a dark hallway to your right and another door in front of you")
      choice = input("[1] - Go into the hallway\n[2] - Go through the door\n")
      cls()
      if(choice == "1"):
        cls()
        print("The hallway is a dead end...")
        print("You turn around and go back to where you came from\n")
        time.sleep(3)
        startMaze()
      elif(choice == "2"):
        cls()
        round2()
      else:
        print("Invalid option, you re-enter the room again")
    startMaze()

    open("variables/done2.txt", "w").write("1")
    import main2
    main2.main2




def room3():
  cls()
  done3 = int(open("variables/done3.txt", "r").read())
  if done3 == 1:
    print("You've already been here. You kick ")
    time.sleep(2)
    import main2
    main2.main2()

  print("It's an empty room with nothing inside except for a lone button. You press the button and walk out of the room.")
  time.sleep(4)  
  open("variables/done3.txt", "w").write("1")
  import main2
  main2.main2()


def room4():
  cls()

  done4 = int(open("variables/done4.txt", "r").read())
  if done4 == 1:
    print("You've already been here. You don't bother trying the door.")
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
  checkIfAlive()
  time.sleep(3)

  open("variables/done4.txt", "w").write("1")
  import main2
  main2.main2

def room5():
  done5 = int(open("variables/done5.txt", "r").read())
  if done5 == 1:
    print("You've already been here. You don't like the door.")
    exec(open("main2.py").read())


  print(ANSI_BLUE,"                _")
  print("           .' . // '.")
  print("          '_ '_\/_'  `_")
  print("          .  . \\  .  .")
  print("         .==. ` \\' .'")
  print("  .\|   //  \\   \,")
  print("  \_'`._\\__//_.'`.;")
  print("    `.__      __,' \\")
  print("        |    |      \\")
  print("        |    |       `")
  print("        |    |")
  print("        |    |")
  print("        |____|")
  print("       =='  '==") 
  print(RESET_COLOR)
  print(" ")
  time.sleep(0.75)

  print("A man in a cloak is sitting at a table, you must answer his riddle correctly to continue.\n")
  time.sleep(1)

  print("I am alive without breath and cold as death. I am never thirsty but always drinking. What am I?")
  time.sleep(1)


def choicemenu1 (): 
  cls()
  time.sleep(0.7)
  print("\n1. bug.\n2.fish.\n3. I dont know")


def choicemenu2 (): 
  cls()
  time.sleep(0.7)
  print("\n1. the man is insulted and slaps you with his brother a young whale shark?")
  print("\n2. the man removes his cloak and reveals a fish head, then the user proceeds forward.") 
  print("\n3. Answer the question.")           

  open("variables/done5.txt", "w").write("1")
  import main2
  main2.main2


#Room 6
def room6():
  cls()
  printSkull()
  print("As you fall asleep, you feel an inkling of doubt creep into your mind.\n\n")
  time.sleep(1.5)
  print("Maybe it's not just a dream\nBut its too late.")
  time.sleep(3)
  cls()
  time.sleep(1.5)
  for char in "You drift off into blackness...\n": 
      print(char, end='') 
      sys.stdout.flush() 
      time.sleep(0.15) 
  exit()

def room69():
  cls()
  checkIfAlive()

  done69 = int(open("variables/done69.txt", "r").read())
  if done69 == 1:
    print("You've already been here. You fall through a portal, dropping you back to the skeleton room.")
    import main2
    main2.main2()


  for char in "You close your eyes and concentrate. When you open your eyes, everything is pure white. You have successfully transcended mortality.\n\n\n": 
    print(char, end='') 
    sys.stdout.flush() 
    time.sleep(0.03)
  time.sleep(3) 
  addLives(2)
  checkIfAlive()
  open("variables/done69.txt", "w").write("1")
  import main2
  main2.main2()


def roomFinal():
  for char in "You look into each room, satisfied that you've throroughly searched everything. The room still doesn't have an exit.\n\nYou decide to sit down on the chair that was next to you when you woke up. To your surprise, when you sit down in the chair you hear 5 clicks, one above each doorway. The room is silent until the entire wall opens up behind you.\n\n Astounded, you step out of the room, into your own bedroom. You look behind you, and the wall is once again solid, as if the room you just escaped didn't exist. ": 
    print(char, end='') 
    sys.stdout.flush() 
    time.sleep(0.03) 
  time.sleep(3)
  for char in "Credits: Kian, Komay, Megan, Ridhima, and Christopher":
    print(char, end='')
    sys.stdout.flush()
    time.sleep(0.03)
  print("Thanks for playing!")
  exit()
