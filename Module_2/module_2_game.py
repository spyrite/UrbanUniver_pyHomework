def draw_area():
    for i in area:
        print(*i)
    print()


def check_winner(current_turn):
    summary = []
    for i in range(3):
        summary.append(''.join(area[i]))
        summary.append(''.join([area[j][i] for j in range(3)]))

    summary.append(''.join([area[i][i] for i in range(3)]))
    summary.append(''.join([area[i][2 - i] for i in range(3)]))

    if "XXX" in summary:
        return "X"
    elif "000" in summary:
        return "0"
    elif current_turn == 9:
        return "*"
    else:
        return None


area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("Добро пожаловать в крестики-нолики")
print("----------------------------------")
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = "0"
        print("Ходят нолики")
    else:
        turn_char = "X"
        print("Ходят крестики")

    row = None
    while row not in range(3):
        row = int(input("Введите номер строки (1,2,3) ")) - 1

    column = None
    while column not in range(3):
        column = int(input("Введите номер столбца (1,2,3) ")) - 1

    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("Ячейка уже занята, вы пропускаете ход")
        draw_area()
        continue

    draw_area()
    match check_winner(turn):
        case "X":
            print("Победа крестиков")
            break
        case "0":
            print("Победа ноликов")
            break
        case "*":
            print("Ничья")
            break
