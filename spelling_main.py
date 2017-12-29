import random       # Import the required module for text to speech conversion
from gtts import gTTS       # This module is imported so that we can play the converted audio
import os
grade = input('Please enter your grade level ')    #indicating grade level

with open(grade +'.txt') as temp_file:
    contents = [line.rstrip('\n') for line in temp_file]  #adding grade level words to a list

counter = 0
chosen_word= random.choice(contents)

while counter < 3:
    chosen_word= random.choice(contents)

    mytext = chosen_word
    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save('welcome.mp3')

    # Playing the converted file
    os.system('welcome.mp3')

    guess = input('enter spelling word ')

    should_restart = True
    while should_restart:
        if guess == chosen_word:
            print('correct!')
            should_restart = True
            break
        if guess != chosen_word:
            print('try again')
            counter += 1
            guess = input('enter spelling word')









