import random

number = random.randint(1, 10)
number_of_guesses = 0

while number_of_guesses < 3:
    print('Угадай число от 1 до 10:')
    guess = input()
    guess = int(guess)
    number_of_guesses += 1

    if guess == number:
        print('Отлично! Это и есть загаданное число!')
        break

    #elif number_of_guesses >=
