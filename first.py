print("Hello World!")

from time import sleep
from random import randint
print("Hello World!")


#----------------------------------------------
# Animated Banner Program
#----------------------------------------------

import os
import time
import sys
repeat=0

if 'idlelib.run' in sys.modules:
    input('\nPlease make sure that you have opened the program by double clicking on it\n(Not in IDLE)\tPress enter to start anyway:\t')

#the width of the display
#(the windows console is 79 characters wide).
WIDTH = 115

message = "998 33 330 03 08 -"

message=message.upper()
#the printed banner version of the message
#this is a 7-line display, stored as 7 strings
#initially, these are empty.
printedMessage = [ "","","","","","","" ]

#a dictionary mapping letters to their 7-line
#banner display equivalents. each letter in the dictionary
#maps to 7 strings, one for each line of the display.
characters = { " " : [ "   ",
                       "   ",
                       "   ",
                       "   ",
                       "   ",
                       "   ",
                       "   " ],

               "A" : [ "#####",
                       "#   #",
                       "#   #",
                       "#####",
                       "#   #",
                       "#   #",
                       "#   #" ],

               "B" : [ "#### ",
                       "#   #",
                       "#   #",
                       "#### ",
                       "#   #",
                       "#   #",
                       "#### " ],

               "C" : [ " ####",
                       "#    ",
                       "#    ",
                       "#    ",
                       "#    ",
                       "#    ",
                       " ####" ],

               "D" : [ "#### ",
                       "#   #",
                       "#   #",
                       "#   #",
                       "#   #",
                       "#   #",
                       "#### " ],

               "E" : [ "#####",
                       "#    ",
                       "#    ",
                       "#####",
                       "#    ",
                       "#    ",
                       "#####" ],

               "F" : [ "#####",
                       "#    ",
                       "#    ",
                       "#####",
                       "#    ",
                       "#    ",
                       "#    " ],

               "G" : [ " ### ",
                       "#   #",
                       "#    ",
                       "#    ",
                       "# ###",
                       "#   #",
                       " ### " ],
               
               "H" : [ "#   #",
                       "#   #",
                       "#   #",
                       "#####",
                       "#   #",
                       "#   #",
                       "#   #" ],

               "I" : [ "#####",
                       "  #  ",
                       "  #  ",
                       "  #  ",
                       "  #  ",
                       "  #  ",
                       "#####" ],

               "J" : [ "######",
                       "    # ",
                       "    # ",
                       "    # ",
                       "    # ",
                       "#   # ",
                       " ###  " ],

               "K" : [ "#   #",
                       "#  # ",
                       "# #  ",
                       "##   ",
                       "# #  ",
                       "#  # ",
                       "#   #" ],

               "L" : [ "#    ",
                       "#    ",
                       "#    ",
                       "#    ",
                       "#    ",
                       "#    ",
                       "#####" ],

               "M" : [ "##       ##",
                       "# #     # #",
                       "#  #   #  #",
                       "#   # #   #",
                       "#    #    #",
                       "#    #    #",
                       "#    #    #" ],

               "N" : [ "#     #",
                       "##    #",
                       "# #   #",
                       "#  #  #",
                       "#   # #",
                       "#    ##",
                       "#     #" ],

               "O" : [ "#####",
                       "#   #",
                       "#   #",
                       "#   #",
                       "#   #",
                       "#   #",
                       "#####" ],

               "P" : [ "#####",
                       "#   #",
                       "#   #",
                       "#####",
                       "#    ",
                       "#    ",
                       "#    " ],


               "Q" : [ " ##### ",
                       "#     #",
                       "#     #",
                       "#     #",
                       "#     #",
                       "#     #",
                       " #### #" ],

               "R" : [ "##### ",
                       "#    #",
                       "#    #",
                       "####  ",
                       "#   # ",
                       "#    #",
                       "#    #" ],

               "S" : [ " ####",
                       "#    ",
                       "#    ",
                       " ### ",
                       "    #",
                       "    #",
                       "#### " ],

               "T" : [ "#######",
                       "   #   ",
                       "   #   ",
                       "   #   ",
                       "   #   ",
                       "   #   ",
                       "   #   " ],

               "U" : [ "#    #",
                       "#    #",
                       "#    #",
                       "#    #",
                       "#    #",
                       "#    #",
                       " #### " ],

               "V" : [ "#   # ",
                       "#   # ",
                       "#   # ",
                       "#   # ",
                       "#   # ",
                       " # #  ",
                       "  #   " ],

               "W" : [ "#        #",
                       "#        #",
                       "#        #",
                       "#   ##   #",
                       "#  #  #  #",
                       "# #    # #",
                       "##      ##" ],

               "X" : [ "#     #",
                       " #   # ",
                       "  # #  ",
                       "   #   ",
                       "  # #  ",
                       " #   # ",
                       "#     #" ],

               "Y" : [ "#     #",
                       " #   # ",
                       "  # #  ",
                       "   #   ",
                       "   #   ",
                       "   #   ",
                       "   #   " ],

               "Z" : [ "#####",
                       "    #",
                       "   # ",
                       "  #  ",
                       " #   ",
                       "#    ",
                       "#####" ],

               "1" : [ "  #  ",
                       "###  ",
                       "  #  ",
                       "  #  ",
                       "  #  ",
                       "  #  ",
                       "#####" ],

               "2" : [ " ### ",
                       "#   #",
                       "    #",
                       "   # ",
                       " #   ",
                       "#    ",
                       "#####" ],

               "3" : [ " ### ",
                       "#   #",
                       "    #",
                       "   # ",
                       "    #",
                       "#   #",
                       " ### " ],

               "4" : [ "#   #",
                       "#   #",
                       "#   #",
                       "#####",
                       "    #",
                       "    #",
                       "    #" ],

               "5" : [ "#####",
                       "#    ",
                       "#    ",
                       "#### ",
                       "    #",
                       "    #",
                       "#### " ],

               "6" : [ " ####",
                       "#    ",
                       "#    ",
                       "#### ",
                       "#   #",
                       "#   #",
                       " ### " ],

               "7" : [ "######",
                       "     #",
                       "     #",
                       "    # ",
                       "    # ",
                       "   #  ",
                       "   #  " ],

               "8" : [ " ### ",
                       "#   #",
                       " # # ",
                       "  #  ",
                       " # # ",
                       "#   #",
                       " ### " ],

               "9" : [ " ### ",
                       "#   #",
                       "#   #",
                       " ####",
                       "    #",
                       "    #",
                       "    #" ],

               "0" : [ " ### ",
                       "#   #",
                       "#  ##",
                       "# # #",
                       "##  #",
                       "#   #",
                       " ### " ],


               "!" : [ "  #  ",
                       "  #  ",
                       "  #  ",
                       "  #  ",
                       "  #  ",
                       "     ",
                       "  #  " ],

               "'" : [ " | ",
                       " | ",
                       "   ",
                       "   ",
                       "   ",
                       "   ",
                       "   " ],

               "." : [ "     ",
                       "     ",
                       "     ",
                       "     ",
                       "     ",
                       "     ",
                       "#    " ],

               "," : [ "  ",
                       "  ",
                       "  ",
                       "  ",
                       "  ",
                       " /",
                       "/ " ],

                "-": ["    _#******#_   ",
                      "  #*          *#  ",
                      " #   00    00   # ",
                      "#       ||       #",
                      "#    -______-    #",
                      " #_            _# ",
                      "   *#________#*   "]
               
               }

for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

#the offset is how far to the right we want to print the message.
#initially, we want to print the message just off the display.
offset = WIDTH
while True:
    os.system("cls")
    #print each line of the message, including the offset.
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    #move the message a little to the left.
    offset-=1
    #if the entire message has moved 'through' the display then
    #start again from the right hand side.
    print(((len(message)+2)*6) * -1,offset)
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH

    if offset == -220:
        break
    #take out or change this line to speed up / slow down the display
    time.sleep(0.01)