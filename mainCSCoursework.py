import time
from NEAclasses import scale

# class scale:

    # def __init__(self, root, third, fith, chordRN, chordName): #chordRN = chordRomanNumeral
    #     self.root = root
    #     self.third = third
    #     self.fith = fith
    #     self.chordRN = chordRN
    #     self.chordName = chordName

    # def chordNotes(self):
    #     chord = []
    #     chord.append(self.root)
    #     chord.append(self.third)
    #     chord.append(self.fith)
    #     return chord

#this is the class "scale" I imported from my classes file called "NEAclasses"




#*args and **qargs - can be used for something like to create optional arguments for classes and functions?
#use to add the 7th to dominant chord object but not to any other scale degree?

# def funcDiatonicCheck(melody, scaleList):
#       i = 0
#       diatonic = True
#       failMessage = ""
#       while i < len(melody) and diatonic == True:
#         if melody[i] in scaleList:
#             diatonic = True
#             i += 1
#         else:
#             diatonic = False
#             failMessage = ("The note:", melody[i], "is not in the key C Major")
#       return diatonic, failMessage

def funcDiatonicCheck(melodyNote, scaleList):
    if melodyNote in scaleList:
        diatonic = True
        failMessage = ""
    else:
        diatonic = False
        failMessage = (f"The note: {melodyNote} is not in the key C Major, please enter a new melody.")
    return diatonic, failMessage

def funcInputMelody(scaleList):
    melody = []
    while len(melody) != 8:
        melodyNoteInp = input("Input your melody one note at a time:")
        melodyNote = melodyNoteInp.upper()
        diatonic, failMessage = funcDiatonicCheck(melodyNote, scaleList)
        if diatonic == True:
            melody.append(melodyNote)
        else:
            print(failMessage)
        time.sleep(0.2)
    return melody

# considered having it so that when you input a note thats not in the melody scale, it either makes you restart and enter the whole melody again...
# or, it makes you just enter a different note and cary on. - This is the option I decided on going for.

def funcScaleList(scale):
    tonicChord = list(tonic.chordNotes())
    supertonicChord = list(supertonic.chordNotes())
    scaleList = []
    scaleList.extend((*tonicChord, *supertonicChord, *leadingNote.root))
    return scaleList

def funcBasicChordChoice(melody):
    choice = []
    for note in range(len(melody)):
        match melody[note]:
            case tonic.root | tonic.third:
                choice.append("tonic")
            case dominant.root | dominant.third | dominant.fith:
                choice.append("dominant")
            case subdominant.root | subdominant.third:
                choice.append("subdominant")
    return choice        




# def funcChordChoice(melody):
#     for note in melody:
#         choice = ""
#         if melody[note] == tonic.root:
#             choice = "tonic"
#             break
#         elif melody[note] == dominant.root:
#             choice = "dominant"
#             break
#         elif melody[note] == tonic.fith:
#             choice = "tonic"
#             break
#         elif melody[note] == dominant.fith:
#             choice = "dominant"
#             break
#         elif melody[note] == tonic.third:
#             choice = "tonic"
#             break
#         elif melody[note] == dominant.third:
#             choice = "dominant"
#             break
#         elif melody[note] == subdominant.root:
#             choice = subdominant
#             break
        
        # if root of tonic chord




# root of tonic, root of dominant
# chordCheckOrder = [""]

tonic = scale("C", "E", "G", "I", "C Maj")
supertonic = scale("D", "F", "A", "ii", "D Min")
mediant = scale("E", "G", "B", "iii", "E Min")
subdominant = scale("F", "A", "C", "IV", "F Maj")
dominant = scale("G", "B", "D", "V", "G Maj")
submediant = scale("A", "C", "E", "vi", "A Min")
leadingNote = scale("B", "D", "F", "vii", "B Dim")


def main():
    scaleList = funcScaleList(scale)
    print(scaleList)
    # diatonic = False
    # while diatonic == False:
    melody = funcInputMelody(scaleList)
        # diatonic, failMessage = funcDiatonicCheck(melody, scaleList)
        # if diatonic == False:
            # print(diatonic, failMessage)
    print(melody)
    choice = funcBasicChordChoice(melody)
    print(choice)

main()



# make it so that as soon as you input an invalid note into your melody, it stops you and makes you restart the process of 
# entering a melody rather than wating until you have entered all the melody notes before checking


# To Do:
    # Try to introduce a cadence point at the end, try to make it do dominant -> tonic for a perfect cadence.

# Done:
    # Make it so that the function to check if diatonic works per single melody note, then call the function
    # after each melody note is imputed in the Melody input thing.
