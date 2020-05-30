import random
print("H A N G M A N")


def menu():
    global hangman, repeat, word_list, word
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(word_list)
    hangman = ['-' for _ in range(0, len(word))]
    repeat = []
    choice = input('''Type "play" to play the game, "exit" to quit: ''').lower().strip()
    print()
    if choice == 'play':
        return guessword(0)
    elif choice == 'exit':
        return exit()
    else:
        return menu()

def exit():
    pass

def guessword(count= 0):
    while count <= 7:
        print(''.join(hangman))
        guess = input("Input a letter:")
        if len(guess) > 1 or guess == '':
            print("You should input a single letter\n")
            return guessword(count=count)
        if not guess.isascii() or not guess.islower():
            print("It is not an ASCII lowercase letter\n")
            return guessword(count=count)
        if guess not in hangman:
            if guess in word:
                for i in range(0, len(word)):
                    if guess == word[i]:
                        hangman.pop(i)
                        hangman.insert(i, guess)
                if ''.join(hangman) == word:
                    print('''You guessed the word {}!\nYou survived!\n'''.format(''.join(hangman)))
                    break
                print()
            else:
                if guess in repeat:
                    print("You already typed this letter\n")
                else:
                    count += 1
                    repeat.append(guess)
                    if count == 8:
                        print("No such letter in the word")
                        print("You are hanged!\n")
                        break
                    else:
                        print("No such letter in the word\n")
        else:
            print("You already typed this letter\n")

menu()