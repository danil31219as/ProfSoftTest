def check_brackets(line: str) -> bool:
    brackets = []
    close_open = {')': '(', '}': '{', ']': '['}
    for bracket in line:
        if bracket in close_open.values():
            brackets.append(bracket)
        else:
            if brackets and brackets[-1] == close_open[bracket]:
                brackets.pop()
            else:
                return False
    return not brackets


line = '{[(}])'
print('Правильно' if check_brackets(line) else 'Неправильно')
