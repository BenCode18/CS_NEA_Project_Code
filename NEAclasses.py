class scale:

    def __init__(self, root, third, fith, chordRN, chordName): #chordRN = chordRomanNumeral
        self.root = root
        self.third = third
        self.fith = fith
        self.chordRN = chordRN
        self.chordName = chordName

    def chordNotes(self):
        chord = []
        chord.append(self.root)
        chord.append(self.third)
        chord.append(self.fith)
        return chord

#*args and **qargs - can be used for something like to create optional arguments for classes and functions?
#use to add the 7th to dominant chord object but not to any other scale degree?