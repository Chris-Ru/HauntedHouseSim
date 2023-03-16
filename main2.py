import sys
import time
from functions import cls, addLives, writeFile
from stage1 import room1, room2, room3, room4, room5, room6, room69, roomFinal


def main2():
  def testDoor():
    done1 = int(open("variables/done1.txt", "r").read())
    done2 = int(open("variables/done2.txt", "r").read())
    done3 = int(open("variables/done3.txt", "r").read())
    done4 = int(open("variables/done4.txt", "r").read())
    done5 = int(open("variables/done5.txt", "r").read())
    if done1 == 0:
      print("You haven't explored room 1 yet.")
      main2()
    else:
      print("Room 1 complete.")
      if done2 == 0:
        print("You haven't explored room 2 yet.")
        main2()
      else:
        print("Room 2 complete.")
        if done3 == 0:
          print("You haven't explored room 3 yet.")
        else:     
          print("Room 3 complete.")
          if done4 == 0:
            print("You haven't explored room 4 yet.")
            main2()
          else:
            print("Room 4 complete.")
            if done5 == 0:
              print("You haven't explored room 5 yet.")
              main2()
            else:
              print("Room 5 complete.")
              print("You've collected the necessary materials to advance")
              roomFinal()

  choicesmenu = {
    1: room1,
    2: room2,
    3: room3,
    4: room4,
    5: room5,
    6: room6,
    7: testDoor,
    69: room69
  }  
  cls()
  print("\n1. Room 1\n2. Room 2\n3. Room 3\n4. Room 4\n5. Room 5\n6. Go back to sleep. It's probably just a dream anyways\n7. Test the doors")
  choice1 = input("Choose an option.")
  choice2 = choicesmenu[int(choice1)]
  choice2()