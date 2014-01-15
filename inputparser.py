###############################################
##              Input Parser                 ##
###############################################
#                                             #
#   Currently all variables are hardcoded.    #
# Input will eventually be passed in and used #
# to determine song info.  Until then, sample #
# input is provided to allow functionality    #
# during development.                         #
#                                             #
###############################################

# number of bars in a section
sectionLength = 12

# tempo of piece in beats per minute
tempo = 120

# Speed that chords change, measured in bars (.5 is a half note)
harmonicRhythm = 1

# not sure how to represent instrumentation yet.
# To be figured out once music is able to be synthesized.
instrumentation = []

# level of chord extension and melodic suspension acceptable.
# Still playing around with different forms of representation,
# but a scale of 1-4 seems the most logical right now.
# 1 is pure triads with each higher number adding an extension
# until it is an 11th chord.
chordDepth = 1

# scale definitions which will be copied to "mode"
major = [0, 2, 4, 5, 7, 9, 11]
minor = [0, 2, 3, 5, 7, 8, 10]

mode = major