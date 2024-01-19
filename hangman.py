import random

# The words are down here
Words = ["Cat","Dog","Sun","Book","Tree","Happy","Blue","Jump","Laugh","Run","Smile","Water","Friend","Dance","Red","Cake","Sleep","Ball","Flower","Hat"]

#A random word will be chosen
chosenWord = random.choice(Words)
#print(chosenWord)

#word will be divided by certain characteristics

WordAct = ["Jump","Laugh","Run","Smile","Dance","Sleep"]
WordObj = ["Book","Tree","Ball","Flower","Hat","Cake","Water","Sun","Blue"]
WordLive = ["Cat","Dog","Friend"]

#based on the word the hint will be provided

hintAct = "The Word is an Action."
hintObj = "The Word is an Object."
hintLive = "The Word is an Living Thing."

if(chosenWord in WordAct):
    print(hintAct)
elif(chosenWord in WordObj):
    print(hintObj)
else:
    print(hintLive)

#prompting
print("\n Guess the Word..!!! \n")

#as per the length of word give chances
#if the word is of 4 alphabets the chances will be 4 + 2 = 6



Tries = len(chosenWord) + 2

print("You have", Tries ,"Chances")


#take the input from the user

result = ""

while(Tries>=0):
    guess = input(print("Guess a Letter: "))
    for letter in chosenWord:
        if letter == guess:
            result += letter  # Append the guessed letter to the result
        else:
            result += "_" 
            print(result)
    Tries = Tries - 1




        

