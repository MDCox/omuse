###############################################
##                   omuse                   ##
###############################################
#                                             #
#   Main file for omuse. Right now it doesn't #
# play anything back because the rest of the  #
# program which would allow that simply isn't #
# far enough along to for base functionality. #
# It will currently print out the generated   #
# melody and any song info used to make it.   #
#                                             #
# Later on it will call the other files, and  #
# contain the main loop.                      #
#                                             #
###############################################

from musicgen import *

print "Welcome to omuse!"

while True:
    command = raw_input("type 'gen' to generate a peice: ")
    if command == 'gen':
        print "melody:\n" + str(melody)
        print "scale:\n" + str(scale)
        print "chords:\n" + str(chords)
        print "progression:\n" + str(progression)
    else:
        break
