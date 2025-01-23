def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    result = 0
    match operation:
        case '+':
            result = operand_1 + operand_2
        case '-':
            result = operand_1 - operand_2
        case '*':
            result = operand_1 * operand_2
        case '//':
            result = operand_1 // operand_2
        case '/':
            result = operand_1 / operand_2
        case '%':
            result = operand_1 % operand_2
    #print(f'Результат операции: {result}')

cnt = 0

with open('data.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в линии {cnt}, не хватает данных для ответа')
            else:
                print(f'Ошибка в линии {cnt}, нельзя перевести в число')