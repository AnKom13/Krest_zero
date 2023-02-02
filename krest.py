# вывод игрового поля 
def show_field():
    print('  0 1 2 ')
    print(f"0 {f['00']} {f['01']} {f['02']}")
    print(f"1 {f['10']} {f['11']} {f['12']}")
    print(f"2 {f['20']} {f['21']} {f['22']}")


# Проверка хода
def check_move(p):
    while True:
        print(f'Ходит игрок {p} :', end=' ')
        x = input()
        if f[x] == '-':
            return x
        print('Неверный ход, попробуйте еще')


# проверка на выигрыш
def check_win(s):
    t = s * 3
    return any([
        # строки
        f['00'] + f['01'] + f['02'] == t,
        f['10'] + f['11'] + f['12'] == t,
        f['20'] + f['21'] + f['22'] == t,
        # столбцы
        f['00'] + f['10'] + f['20'] == t,
        f['01'] + f['11'] + f['21'] == t,
        f['02'] + f['12'] + f['22'] == t,
        # диагонали
        f['00'] + f['11'] + f['22'] == t,
        f['20'] + f['11'] + f['02'] == t
    ]
    )


# генерация матрицы стартового поля
f = {str(x) + str(y): '-' for x in range(0, 3) for y in range(0, 3)}

print('Игра - крестики-нолики')
print('Первый  игрок играет X, второй O')
print('Для хода необходимо ввести координаты поля (например 01)')
print('Поехали')
i = 0
while True:
    i += 1
    show_field()
    f[check_move(1)] = 'X'
    if check_win('X'):
        print('Победа игрока 1')
        break

    if i == 5:
        print('Ничья')
        break

    show_field()
    f[check_move(2)] = 'O'

    if check_win('O'):
        print('Победа игрока 2')
        break

show_field()
