import random

with open('hangman_words.txt', 'r') as file:
    words_list = file.readlines()

# words_list=["animal", "amazon", "antarctic"]

word = random.choice(words_list).strip().upper()
letters = list(word)

dashes = ['_'] * len(word)

print("The word you need to guess is:", ' '.join(dashes))

chance = 7
used = []

while '_' in dashes and chance > 0:
    guess = input("Guess a letter: ").upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid entry, please enter a single alphabet to play this game")
        continue

    if guess in used:
        print("You have already used the letter, please try with another letter")
        continue

    used.append(guess)

    if guess in letters:
        for i in range(len(word)):
            if word[i] == guess:
                dashes[i] = guess
    else:
        chance -= 1
        print("That was a wrong guess. Chances left:", chance)

    print("Current word:", ' '.join(dashes))
    print("The letters you have already used are:", ', '.join(used))

if '_' not in dashes:
    print("Congratulations! You have guessed the word correctly. The word is:", word)
else:
    print("You have failed to guess the word correctly.")
    print("The correct word is:", word)