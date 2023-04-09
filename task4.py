# Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите кол-во долек шоколадки по вертикали: "))
m = int(input("Введите кол-во долек шоколадки по горизонтали: "))

k = int(input("Введите кол-во долек, которое хотите отломить: "))

if k < m * n and (k % m == 0 or k % n == 0):
    print('Можно отлимить дольки')
else:
    print('Нельзя отломить дольки')