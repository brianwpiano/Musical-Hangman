import random

def making_a_guess():
    global update_display
    x = 0
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    if not correct_guess:
        print(f"There is no {guess}, sorry.")
        update_display += 1

HANGMANPICS = [
    '''  
  +---+
  |   |
      |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========='''
]

# Music glossary word list
word_list = ["allegro", "andante", "arpeggio", "cadenza", "crescendo", "fortissimo", "legato", "melody", "ostinato", "staccato", "tempo", "vibrato", "harmony", "dissonance", "octave"]

# Main game loop
while True:
    chosen_word = list(random.choice(word_list))
    blank_list = ["_" for _ in chosen_word]
    update_display = 0

    print(HANGMANPICS[update_display])
    print(''.join(blank_list))

    while update_display < 6:
        guess = input("Make a guess? ")
        making_a_guess()
        print(HANGMANPICS[update_display])
        print(''.join(blank_list))

        if blank_list == chosen_word:
            print("YOU WIN!")
            break

    if update_display == 6:
        print("GAME OVER.")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
