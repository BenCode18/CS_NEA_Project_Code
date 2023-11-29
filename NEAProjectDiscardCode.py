#def chooseChords(melody, scale):
    

# scale = {
#     "C" : {
#         "scaleDegree" : 1,
#         "third" : "E",
#         "fith" : "G",
#         "chordRomanNumeral" : "I",
#         "chordName" : "C Major",
#     },
#     "D" : {
#         "scaleDegree" : 2,
#         "third" : "F",
#         "fith" : "A",
#         "chordRomanNumeral" : "ii",
#         "chordName" : "D Minor",
#     },
#     "E" : {
#         "scaleDegree" : 3,
#         "third" : "G",
#         "fith" : "B",
#         "chordRomanNumeral" : "iii",
#         "chordName" : "E Minor",
#     },
#     "F" : {
#         "scaleDegree" : 4,
#         "third" : "A",
#         "fith" : "C",
#         "chordRomanNumeral" : "IV",
#         "chordName" : "F Major",
#     },
#     "G" : {
#         "scaleDegree" : 5,
#         "third" : "B",
#         "fith" : "D",
#         "chordRomanNumeral" : "V",
#         "chordName" : "G Major",
#     },
#     "A" : {
#         "scaleDegree" : 6,
#         "third" : "C",
#         "fith" : "E",
#         "chordRomanNumeral" : "vi",
#         "chordName" : "A Minor",
#     },
#     "B" : {
#         "scaleDegree" : 7,
#         "third" : "D",
#         "fith" : "F",
#         "chordRomanNumeral" : "viio",
#         "chordName" : "B Diminished",
#     },
# }
#print(scale)

# melody = ["C", "D", "E", "F#", "G", "A", "B", "C"]



#*args and **qargs - can be used for something like to create optional arguments for classes and functions?
#use to add the 7th to dominant chord object but not to any other scale degree?

#OOP option

# class scale:

#     def __init__(self, root, third, fith, chordRN, chordName): #chordRN = chordRomanNumeral
#         self.root = root
#         self.third = third
#         self.fith = fith
#         self.chordRN = chordRN
#         self.chordName = chordName

#     def chordNotes(self):
#         chord = []
#         chord.append(self.root)
#         chord.append(self.third)
#         chord.append(self.fith)
#         return chord

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
        
    # I chose to use "case" and "match" instead.


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

    # This was my diatonic check function before I chose to change
    # so that it would check each note after they were inputed, rather than all of the notes at the end.


# def main():
#     scaleList = funcScaleList(scale)
#     print(scaleList)
#     # diatonic = False
#     # while diatonic == False:
#     melody = funcInputMelody(scaleList)
#         # diatonic, failMessage = funcDiatonicCheck(melody, scaleList)
#         # if diatonic == False:
#             # print(diatonic, failMessage)
#     print(melody)
#     choice = funcBasicChordChoice(melody)
#     print(choice)

    # This was my main function where I commented the lines like "# diatonic = False" as originaly these were
    # part of the function "main" but I then changed the functions funcInputMelody and funcDiatonicCheck
    # so that diatonic check would be called inside of the input melody function
    # this was so that instead of checking the notes and if they were diatonic after the whole melody had been inputed
    # it would instead check each note after each note had been inputed, and ask you to input a different note
    # as soon as you inputed an invalid note, rather than it asking you to re-enter your whole melody
    # and only telling you that one of your notes are invalid once you had inputed a whole melody.

