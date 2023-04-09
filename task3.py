# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

number = input('Введите шестизначный номер Вашего билета: ')
while True:
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print('Ура, Ваш билет счастливый!')
        else:
            print('Ваш билет не счастливый :-( Надеемся в следующий раз Вам повезет!')
        break
    else:
        print('Введен некорректный номер билета!)')
        break