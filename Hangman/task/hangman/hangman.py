import random
print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
guess = input("Guess the word {}{}: ".format(word[:3], '-'*(len(word)-3)))

if guess == word:
    print("You survived!")
else:
    print("You are hanged!")