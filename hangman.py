
word = input("Please enter the word you want to guess: ").strip().lower()
print(word)

letter = list()
for w in word:
    letter.append(w)
print (letter)

wrong_guess = 0
right_guess = 0
chances = len(letter)
print (chances)

while wrong_guess < chances or right_guess != chances:
    guess = input("Enter the letter you want to guess: ")
    for i in letter:
        if i == guess:
            right_guess = right_guess + 1
            print("You have guessed right")
        else:
            wrong_guess = wrong_guess + 1
            print("You have guesses wrong")

if wrong_guess == chances:
    print("You have won")
else:
    print("You have lost")
        
