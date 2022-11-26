from random import randint


ran= randint(1, 100)
print("Отгадайте число от 1 до 100")
while (True):
    inp = int(input("Введите число от 1 до 100__"))
    if inp <ran :
      print("Ваше число меньше загаданного")
    elif inp>ran:
        print("Ваше число больше загаданного")
    else:
        print("Вы угадали число", ran)
        break
    