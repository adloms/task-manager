import random

num = random.randint(1, 50)
turns = 0
max_turns = 5

print(f"Угадай число от 1 до 50 за {max_turns} попыток!")

while turns < max_turns:
    player = int(input("Введи число: "))
    turns += 1

    if player == num:
        print(f"Попал! Ты угадал за {turns} попыток!")
        break
    elif player > num:
        print("Меньше")
    else:
        print("Больше")

else:
    print(f"Не угадал. Было число {num}")