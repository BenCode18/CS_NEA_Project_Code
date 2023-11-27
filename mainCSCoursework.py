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

def funcDiatonicCheck(melody, scaleList):
      i = 0
      diatonic = True
      failMessage = ""
      while i < len(melody) and diatonic == True:
        if melody[i] in scaleList:
            diatonic = True
            i += 1
        else:
            diatonic = False
            failMessage = ("The note:", melody[i], "is not in the key C Major")
      return diatonic, failMessage


def funcInputMelody(scaleList):
    melody = []
    for i in range(0,7):
        melodyNote = (input("Input your melody one note at a time:"))
        melody.append(melodyNote.upper())
        time.sleep(0.2)
    return melody

def funcScaleList(scale):
    tonicChord = list(tonic.chordNotes())
    supertonicChord = list(supertonic.chordNotes())
    scaleList = []
    scaleList.extend((*tonicChord, *supertonicChord, *leadingNote.root))
    return scaleList

def funcChordChoice(melody):
    for note in melody:
        


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
    diatonic = False
    while diatonic == False:
        melody = funcInputMelody(scaleList)
        diatonic, failMessage = funcDiatonicCheck(melody, scaleList)
        if diatonic == False:
            print(diatonic, failMessage)
        print(melody)

main()



# make it so that as soon as you input an invalid note into your melody, it stops you and makes you restart the process of 
# entering a melody rather than wating until you have entered all the melody notes before checking


# To Do:
    # Make it so that the function to check if diatonic works per single melody note, then call the function
    # after each melody note is imputed in the Melody input thing.

