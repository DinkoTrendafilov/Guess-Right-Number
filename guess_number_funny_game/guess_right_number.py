import random

wins = 0
losses = 0

while True:
    command = input("Въведи край на играта с (end)  или играем с (ok): ")
    if command == "end":
        print(f"Ти приключи играта със следната статистика: Победи: {wins} - Загуби: {losses}")
        break
    elif command == "ok":
        number_to_guess = random.randint(1, 100)
        guess = None
        counter = 0
        while True:
            guess = int(input("Познай числото между 1 и 100, имате 6 опита, успех!: "))

            if guess == number_to_guess:
                print(f"Браво!!! Ти позна числото, то бе: {number_to_guess}")
                wins += 1
                break
            elif guess + 1 == number_to_guess or guess + 2 == number_to_guess \
                    or guess - 1 == number_to_guess or guess - 2 == number_to_guess:
                print("Топло, топло!!!")
            elif guess < number_to_guess:
                print("Нагоре!")
            elif guess > number_to_guess:
                print("Надолу!")

            counter += 1
            if counter == 6:
                print("Нямате повече опити, съжаляваме :(, опитайте отново!")
                print(f"Търсеното число бе: {number_to_guess}")
                losses += 1
                break
    else:
        print("Невалидна команда, моля въведете (end) или (ok)!")