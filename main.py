import json

# +2 score for each character in the password, the rest removes score
# +4 for any symbol
# Requirement of atleast 4 characters minimum for password 

# <---------- Variables ---------->
debug = True # for detailed process outputs
score = 0 # baseline score before input
processingScore = 0 # temporary storage for processing weight for letter from weights.json
reasons = []

w = json.load(open("weights.json")) # assignment of 'w' to management of weights
if debug == True:
    print(w) # output of current weights if debug on

password = str(input("Enter your password:"))

if debug == True:
    print(f"Password Input: {password}, score = {score}")

def checkScore(finalScore): # Final score output
    if finalScore < 0:
        print("Failed")
    elif finalScore <= 5:
        print("Poor")
    elif finalScore <= 10:
        print("Good")
    else:
        print("Great")

for i in range(len(password)):
    print(i)