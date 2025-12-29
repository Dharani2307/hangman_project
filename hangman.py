import random
import hang_word
import hang

#words=["angry","activity","Devil"]
chosen_word=random.choice(hang_word.word).lower()
print(chosen_word)
lives=6
display=[]
for space in range(len(chosen_word)):
    display +='_'
print(display)
game_start=True
while game_start:
    guess_letter=input("Guess the  word:" ).lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess_letter:
            display[position]=guess_letter
    print(display)
    if guess_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_start=False
            print("You lose!")
            print(hang.stages[lives])
# Both the condition satisfy if the both chosen word and guessed word match
    if display==chosen_word:
        game_start=False
        print("You win!")
    #print(hang.stages[lives])

    if '_' not in display:
        game_start=False
        print("You win!")
    print(hang.stages[lives])




