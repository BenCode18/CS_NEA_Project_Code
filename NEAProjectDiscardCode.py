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