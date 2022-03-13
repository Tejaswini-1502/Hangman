#import the required modules
import random
import hangmanArt
import hangmanWords

#store the list of words in a variable called word_list
word_list = hangmanWords.word_list
#From the random module use the choice function to randomly select a word from word_list
chosen_word = random.choice(word_list)
#display is  a list to store the correctly guessed letter by the player
#The letter in display corresponds to the letter in the chosen_word
display = []
#Initially the player has 6 lives
lives = 6
#end_of_game is  a boolean variable initially set to False. It becomes true when the player correctly guesses all the letters i.e when the game ends
end_of_game = False

print(hangmanArt.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Finding the length of the chosen_word and appending those many dashes(_) in the display list
len_chosen_word = len(chosen_word)
for i in range(len_chosen_word):
  display.append('_')


while not end_of_game:
  guess = input("Guess a letter: ").lower()
  print("Your guess: ",guess)
  if guess in display:
    print(f"You have already guessed {guess}")
  
  for i in range(len_chosen_word):
      if guess == chosen_word[i]:
          display[i] = guess
        
  print(f"{' '.join(display)}")

  #if guess not in chosen_word decreament the number of lives
  #if lives reaches to 0, the player loses and the game ends
  if guess not in chosen_word:
    print(f"{guess} not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      print(hangmanArt.stages[lives])
      print("You lost!")
      break

  #if there are no more '_'(dashes) in diplay list it implies that the player has won and hence the game ends
  if '_' not in display:
    end_of_game = True
    print("You win!")
    
  print(hangmanArt.stages[lives])