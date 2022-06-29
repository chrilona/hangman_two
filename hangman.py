import random
import string
from words import words

def get_words(words):
    word=random.choice(words) 
    while "-" in word or " " in words:
        word=random.choice(words)
    return word   

def play_hangman():
    word=get_words(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    lives=6

    user_input=input("Guess a letter: ")
    print(user_input)
    
    while len(word_letters)>0 and lives>0 :

        print("You have ",lives ,"left and you have used these letters:", " ".join(used_letters))
        word_list=[letter if letter in used_letters else "-" for letter in word] 
        print("Current word: "," ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives=lives - 1
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print(f"You have already used {user_letter}.Please try again ")

        else:
            print("Invalid character.TRY again")

    if lives==0:
       print("Sorry you died.The word was" ,word)
    else:
     print("Your guess was correct" ,word, "!! Congratulations" )      




