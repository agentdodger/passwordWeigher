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

def debugDivider():
    if debug == True:
        print("—"*20)

# <---------- Score Processing ---------->

# 1. +2 for each character in password, +4 for each symbol. Ignores spaces
for i in password:
    if i == " ":
        processingScore = 0
    elif i.isalnum():
        processingScore = w['characterBaseline'] # if number or character, +2 
    else:
        processingScore = w['symbolBaseline'] # if not number or character, must be a symbol: +4
    score = score+processingScore

    if debug == True:
        if processingScore == w['characterBaseline']:
            print(f"[DEBUG - Module 1]: Character '{i}' +{processingScore} score, detected character")
        elif processingScore == w['symbolBaseline']:
            print(f"[DEBUG - Module 1]: Character '{i}' +{processingScore} score, detected symbol")
        elif processingScore == 0:
            print(f"[DEBUG - Module 1]: Space detected, no score given")
        else:
            print(f"[DEBUG - Module 1]: !! ERROR !! Score was {processingScore} for '{i}'")
        print("[DEBUG - Module 1]: Total score output:", score)

    processingScore = -1 # reset to -1 for error detection, next run should replace processingScore immediately if handled appropriately

debugDivider()
# 2. All Upper/Lower detection

upperScore = 0
lowerScore = 0

for i in password:
    if i.isupper():
        upperScore +=1
        if debug == True:
            print(f"[DEBUG - Module 2]: Character {i} detected as uppercase")
    elif i.islower():
        lowerScore +=1
        if debug == True:
            print(f"[DEBUG - Module 2]: Character {i} detected as lowercase")
    else:
        if debug == True:
            if i.isnumeric():
                print(f"[DEBUG - Module 2]: Skipped character {i} due to being a number")
            elif i.isalnum() == False:
                print(f"[DEBUG - Module 2]: Skipped character {i} due to being a symbol")
            else:
                print(f"[DEBUG - Module 2]: !! ERROR !! {i} was not resolved as Upper or Lower")

if upperScore == len(password):
    score = score + w['allUpper']
    if debug == True:
        print(f"[DEBUG - Module 2]: {w['allUpper']} score due to all uppercase detected")
elif lowerScore == len(password):
    score = score + w['allLower']
    if debug == True:
        print(f"[DEBUG - Module 2]: {w['allLower']} score due to all lowercase detected")

if debug == True:
    print(f"[DEBUG - Module 2]: Total score output: {score}")

if upperScore == len(password):
    print("[DEBUG - Module 2]: Password determined to be all uppercase.")
elif lowerScore == len(password):
    print("[DEBUG - Module 2]: Password determined to be all lowercase.")
else:
    print("[DEBUG - Module 2]: Password is not all uppercase or all lowercase")

print(f"Final score: {score}")

debugDivider()
# 3. All Numbers/Letters detection

numScore = 0
letterScore = 0

for i in password:
    if i.isnumeric():
        numScore +=1
        if debug == True:
            print(f"[DEBUG - Module 3]: Character {i} detected as a number")
    elif i.isalpha():
        letterScore +=1
        if debug == True:
            print(f"[DEBUG - Module 3]: Character {i} detected as a letter")
    elif debug == True:
        print(f"[DEBUG - Module 3]: Skipped character {i} due to being a symbol")

if numScore == len(password):
    score = score + w['allNumbers']
    if debug == True:
        print(f"[DEBUG - Module 3]: {w['allNumbers']} score due to all numbers detected")
elif letterScore == len(password):
    score = score + w['allLetters']
    if debug == True:
        print(f"[DEBUG - Module 3]: {w['allLetters']} score due to all letters detected")
else:
    if debug == True:
        print("[DEBUG - Module 3]: All Numbers/Letters not detected, skipped")

if debug == True:
    print(f"[DEBUG - Module 3]: Total score output: {score}")

debugDivider()
# 4. Consecutive Numbers/Letters detection


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