import random

def guess_the_number():
    # Загадываем случайное число от 1 до 400
    number = random.randint(1, 400)
    attempts = 10

    print("Я загадал число от 1 до 400. Попробуй угадать его за 10 попыток.")

    # Цикл для угадывания числа
    for i in range(attempts):
        try:
            # Пользователь вводит свою догадку
            guess = int(input(f"Попытка {i + 1}. Введите ваше число: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        # Проверяем, больше ли, меньше ли или равно загаданное число догадке пользователя
        if guess < number:
            print("Загаданное число больше вашего.")
        elif guess > number:
            print("Загаданное число меньше вашего.")
        else:
            print(f"Поздравляем! Вы угадали число {number} с {i + 1} попытки.")
            break
    else:
        print(f"Вы использовали все 10 попыток. К сожалению, вы не угадали. Число было: {number}")

if __name__ == "__main__":
    guess_the_number()