import json

# +2 score for each character in the password, the rest removes score
# +4 for any symbol
# Requirement of atleast 4 characters minimum for password 

# <---------- Variables ---------->
debug = True # for detailed process outputs
score = 0 # baseline score before input
processingScore = 0 # temporary storage for processing weight for letter from weights.json
reasons = []
password = ""

w = json.load(open("weights.json")) # assignment of 'w' to management of weights
if debug == True:
    print(w) # output of current weights if debug on

while len(password) <=4:
    password = str(input("Enter your password (4+ chars):"))

# <---------- Score Processing ---------->

# 1. +2 for each character in password, +4 for each character. Ignore spaces
for i in password:
    if i == " ":
        processingScore = 0
    elif i.isalnum():
        processingScore = w['characterBaseline'] # if number or character, +2 
    else:
        processingScore = w['symbolBaseline'] # if not number or character, must be a symbol: +4
    score = score+processingScore

    if debug == True:
        if processingScore == 2:
            print(f"[DEBUG]: Character '{i}' +2 score, detected character")
        elif processingScore == 3:
            print(f"[DEBUG]: Character '{i}' +4 score, detected symbol")
        elif processingScore == 0:
            print(f"[DEBUG]: Space detected, no score given")
        else:
            print(f"[DEBUG]: !! ERROR !! Score was {processingScore} for '{i}'")
        print("[DEBUG]: Total score output:", score)

    processingScore = -1 # reset to -1 for error detection, next run should replace processingScore immediately if handled appropriately

    # 2. All Upper/Lower detection, -1

    upperScore = 0
    lowerScore = 0

    for i in password:
        if i.isUpper():
            upperScore +=1
            if debug == True:
                print(f"[DEBUG]: Character {i} detected as uppercase")
        elif i.isLower():
            lowerScore +=1
            if debug == True:
                print(f"[DEBUG]: Character {i} detected as lowercase")
        else:
            if debug == True:
                print(f"[DEBUG]: !! ERROR !! {i} was not resolved as Upper or Lower")

if upperScore - len(password) == 0:
    score = score + w['allUpper']
    if debug == True:
        print(f"[DEBUG]: {w['allUpper']} score due to all uppercase detected")
elif lowerScore - len(password) == 0:
    score = score + w['allLower']
    if debug == True:
        print(f"[DEBUG]: {w['allLower']} score due to all lowercase detected")



# <---------- Output Final Score & Reasons for Deduction (if any) ---------->

# def checkScore(finalScore, finalReasoning): # Final score output & reasoning
#    if finalScore < 0:
#        print("Failed (below 0)")
#    elif finalScore <= 5:
#        print("Poor (below 5)")
#    elif finalScore <= 10 and finalScore >15:
#        print("Good (above 10)")
#    else:
#        print("Great")

## UNFINISHED: Scores and their strength results are not final

# checkScore(score, reasons)