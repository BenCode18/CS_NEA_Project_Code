import time, NEAclasses
from flask import Flask, render_template

app = Flask(__name__)

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

# considered having it so that when you input a note thats not in the melody NEAclasses.NEAclasses.scale, it either makes you restart and enter the whole melody again...
# or, it makes you just enter a different note and cary on. - This is the option I decided on going for.

def funcScaleList():
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


tonic = NEAclasses.scale("C", "E", "G", "I", "C Maj")
supertonic = NEAclasses.scale("D", "F", "A", "ii", "D Min")
mediant = NEAclasses.scale("E", "G", "B", "iii", "E Min")
subdominant = NEAclasses.scale("F", "A", "C", "IV", "F Maj")
dominant = NEAclasses.scale("G", "B", "D", "V", "G Maj")
submediant = NEAclasses.scale("A", "C", "E", "vi", "A Min")
leadingNote = NEAclasses.scale("B", "D", "F", "vii", "B Dim")

@app.route("/")
def homePage():
    return render_template("Home_Page")

def main():
    scaleList = funcScaleList()
    print(scaleList)
    melody = funcInputMelody(scaleList)
    print(melody)
    choice = funcBasicChordChoice(melody)
    print(choice)

main()


# To Do:
    # Try to introduce a cadence point at the end, try to make it do dominant -> tonic for a perfect cadence.
    # create a better GUI

# Done:
    # Make it so that the function to check if diatonic works per single melody note, then call the function
    # after each melody note is imputed in the Melody input thing.
