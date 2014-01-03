###############################################
##              Melody Generator             ##
###############################################
#                                             #
#   Currently, the Melody Generator builds a  # 
# list defining the current key/scale that it #
# will draw notes from. It will then randomly #
# choose notes and create a melody. No rhythm #
# support has been added yet.                 #
#                                             #
#   Later on it will use input from the Chord #
# Generator to guide melody creation.         #
#                                             #
###############################################

import random

"""
Temporary hard coded song info. This will be removed and it'll use info from other
parts of the program. phraseLength is measured in eigth notes.
"""
major = [0, 2, 4, 5, 7, 9, 11]
minor = [0, 2, 3, 5, 7, 8, 10]
mode = major
phraseLength = 32

def genKey(mode):
    """ Randomly chooses tonic and builds a scale from the scale pattern
        contained in mode. """

    chromatic = ["a", "bb", "b", "c", "db", "d", "eb", "e", "f", "gb", "g", "ab"]

    tonic = random.randint(0,11)
    
    """ rearrange chromatic[] to start on tonic """
    chromatic.extend(chromatic[:tonic])
    del chromatic[:tonic]
    
    scale = []
    for i in mode:
        scale.append(chromatic[i])
    scale.append("REST")

    return scale

def genMelody(scale, phraseLength):
    """ Creates a list with phraseLength number of slots and populates
        it with notes (or "REST") from scale  """

    melody = []
    for i in range(phraseLength):
        melody.append(scale[random.randint(0,len(scale)-1)])

    return melody


scale = genKey(mode)
melody = genMelody(scale, phraseLength)

return melody