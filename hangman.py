import random
import os

# Hangman Game
def play_game():
    list_words=["CAT","DOG","BEE","EAGLE","SPIDER","WASP","WHALE","BUFFALO","DONKEY","HORSE","SQUID","CAMEL","CHAMELEON","CRAB","ZEBRA","CROCODILE","RABBIT","DOLPHIN","ELEPHANT","SCORPION","SPARROW","FALCON","HIPPO","ANT","JAGUAR","LION","WOLF","BUTTERFLY","BEAR","BIRD"]
    hangman_pics= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    #Generate a new word from list_words
    word=random.choice(list_words)
    #Generate list of _
    spaces=["_"]*len(word)
    #Inicialize lives in 6
    lives=6
    
    while True:
        os.system("cls")
        print("****************************************")
        print("*                                      *")
        print("*           Hangman Game               *")
        print("*             (Animals)                *")
        print("*                                      *")
        print("****************************************")
        print(f"You have {lives} lives")
        print(hangman_pics[6-lives])
        for caracter in spaces:
            print(caracter,end=" ")
        print("\n")
        letter=input("Give me a letter: ").upper()

        exists_letter=False
        for idx,caracter in enumerate(word):
            if caracter==letter:
                spaces[idx]=letter
                exists_letter=True
        
        if not exists_letter:
            lives=lives-1

        if "_" not in spaces:
            os.system("cls")
            print("You won, you guessed the word ^_^/ : ",word)
            break
            

        if lives ==0:
            os.system("cls")
            print(hangman_pics[6])
            print("You lost, you did NOT guess the word u_u__ : ",word)
            break

if __name__ == "__main__":
    play_game()