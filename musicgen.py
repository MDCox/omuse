###############################################
##              Music Generator              ##
###############################################
#                                             #
#   The main file containing the functions    #
# that are directly related to generating the #
# music.  This does not include creating the  #
# actual audio, but merely the composition    #
# which is represented as a set of lists.     #
#                                             #
#   Song info is imported from inputparser.py #
# which takes input and converts it into song #
# data which is used when determining the way #
# the composition will be written.            #
#                                             #
#   The file is broken up into 3 sections:    #
#       * Chord Generator                     #
#       * Melody Generator                    #
#       * Arrangement Generator               #
# These sections exist purely for ease of use #
# and readability.  The names should be self- #
# explanitory, but further clarification is   #
# included in the documentation.              #
#                                             #
############################################### 

import random
from inputparser import *

###############################################
##              Chord Generator              ##
###############################################
#                                             #
#   Currently, the Chord Generator builds a   # 
# list defining the current key/scale that it #
# will draw notes from. It will then generate #
# all chords that will be used, based on the  #
# chordDepth variable which is passed from    # 
# inputparser.py . Finally it will create 1-4 #
# chord progressions to be used in the piece  #
# depending on the sections that the piece is #
# to use.                                     #
#                                             #
#   Will later include more chordal variation #
# including secondary dominants, modal mixture#
# and jazz-influenced chromatic alterations.  #
#                                             #
###############################################

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

    return scale

def genChords(scale, chordDepth):
    chords = [[],[],[],[],[],[],[],[]]

    # There must be a better way to do this. Probably a generator or itertools.
    repeatedScale = scale*3
    for i in range(0,8):
        chords[i].append(repeatedScale[i])
        chords[i].append(repeatedScale[i + 2])
        chords[i].append(repeatedScale[i + 4])
        if chordDepth > 1:
            chords[i].append(repeatedScale[i + 6])
            if chordDepth > 2:
                chords[i].append(repeatedScale[i + 8])
                if chordDepth > 3:
                    chords[i].append(repeatedScale[i + 10])

    return chords

def genProgression(chords, phraseLength):
    pass

scale = genKey(mode)
chords = genChords(scale, chordDepth)

###############################################
##              Melody Generator             ##
###############################################
#                                             #
#   Currently, the Melody Generator uses the  #
# chord progression as a guide to create the  #
# the melody.  Depending on the chordDepth,   #
# the melody will include varying amounts of  #
# non-harmonic tones.
#                                             #
#   Later on it will include support for non- #
# harmonic tones and common scale alterations.#
#                                             #
###############################################

def genMelody(scale, phraseLength):
    """ Creates a list with phraseLength number of slots and populates
        it with notes (or "REST") from scale  """
    
    scale.append("REST")

    melody = []
    for i in range(phraseLength):
        melody.append(scale[random.randint(0,len(scale)-1)])

    return melody

melody = genMelody(scale, phraseLength)


###############################################
##           Arrangement Generator           ##
###############################################
#                                             #
#   This section is currently just here as a  #
# placeholder.                                #
#                                             #
#   In the future, this section will determine#
# what notes will be placed where in context  #
# of the generated chord structure, melody,   #
# and instrumentation.                        #
#                                             #
###############################################