import random
tryes = 1  # количество попыток, должно начинаться с одного иначе попыток будет на 1 меньше реальных
randnum = random.randint(1,100)  # выбирается число от 1 до 100
print("я загадал число от 1 до 100, пиши число я буду говорить больше оно или меньше")
while True:
    try:
            usernum = int(input())  # пользователь пишет число от 1 до 100
            if usernum < 1 or usernum > 100:
                print("пиши числа только от 1 до 100!")
            elif usernum < randnum:
                print("больше")
                tryes += 1
            elif usernum > randnum:
                print("меньше")
                tryes += 1
            else:
                print("молодец!")
                print("ты угадал за", tryes, end=" ") 
                if tryes >= 10 and tryes <= 20:  # определение для правильного склонения слово "попытка"
                    print("попыток")
                else:
                    c = tryes % 10
                    if c == 1:
                        print("попытку!")
                    elif c <= 4 and c >= 2:
                        print("попытки!")
                    else:
                        print("попыток!")
                break
    except ValueError:
        print("нужно писать только цифры, а не буквы")