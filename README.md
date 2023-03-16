# Welcome to the Haunted House RPG Game

Our program's main purpose is to create a text based adventure game which is themed after a haunted house. In this house haunted users will need to escape by choosing choices that will lead to their success. There are multiple rooms that the user will have to go through. However they have only 10 lives at the start of the game and certain choices made may result in a deduction of lives. Once the user's lives hit zero the game is over. Therefore the user needs to escape through all the rooms in order to successfully win the game. 

## How to Use

At the beginning of the game the user will be prompted with a main menu that gives them access to multiple rooms. Once they have chosen a room of their choice they will be faced with options (presented as menus) that dictate whether the user completes the room or wins the game. 

## File Descriptions

### General Files

main.py - Makes the main menu with all the rooms, imports modules, and creates a dictionary containing all the rooms

### Code Files

functions.py -  defines all the functions and prints out some ASCII art as well. 
main2.py - redirects to main menu and makes sure you can't renter to the same room
stage1.py - Contains all the code for the every single room by having the choices and responses laid out. 

### Text Files

Variable Folder 
  Done.txt : the files are mainly to detect whether the user has entered the room previously. Therefore sets all the files originally to 0 and then sets it to 1 once the user has entered the room. 

READ ME.md : These is where the user can understand our game concept, understand it's features and code, and learn how to play the game. 

### ASCII
Wanted to incoporate some visuals into game therefore have a designated folder and file called function.py that prints different ASCII art with colors. 
      - chair & lamp
      - grandfather clock (animation)
      - skull (printed in function.py)
      - skeleton door
      - skull 

### Terminal Introduction

“You only have an hour…”
You suddenly open your eyes and notice that you’ve awakened in a place other than your bed with no memories, only knowing that you have to escape within an hour. The room is dark and honestly somewhat spooky.
You look around and notice a giant gleaming father clock. It’s 2 AM. One hour away from the witching hour.

“
You are faced with five doors each looking slightly different from the other. The first door is thicccccc, constructed with black metal and with medieval-looking designs carved into the doorframe. An intricately carved skull replaces a handle. The second door is covered with spiky thorns with vines intertwining all across. 

“

3 AM, also known as the witching hour or the devil's hour, is when all supernatural beings come out. At this time, you will die, no matter how strong your will to live is.
Using luck, clues and your noggin (that hopefully still works after the memory loss), you will have to make your way out of the mansion. 
Each room contains a different puzzle that could get you out of the haunted house. 
Choose wisely, and we wish you the best of luck.

## Creators

DNHS AP CS Principles, Group Colin KianB - 

Kian Kishimoto
Ridhima Inukurti
Megan Corrigan
Komay Sugiyama
Christopher Rubin

## AP Requirements 

```            
Conditionals                 -     main2.py stage1.py 
Iteration                    -     function.py, stage1.py           
Lists & Dictionaries         -     stage1.py, main.py
Functions                    -     functions.py, stage1.py
Random Values                -     main.py, main2.py, stage1.py  
Strings & Numbers            -     main.py, main2.py, stage1.py, functions.py      
```
