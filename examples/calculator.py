from cmath import exp


a = '1+5*6-4/7+8'


def calc(expression):
    print(expression)
    add_index = expression.find('+')
    if add_index != -1:
        exp1 = expression[0:add_index]
        exp2 = expression[add_index+1:]
        return calc(exp1) + calc(exp2)
    sub_index = expression.find('-')
    if sub_index != -1:
        exp1 = expression[0:sub_index]
        exp2 = expression[sub_index+1:]
        return calc(exp1) - calc(exp2)
    mul_index = expression.find('*')
    if mul_index != -1:
        exp1 = expression[0:mul_index]
        exp2 = expression[mul_index+1:]
        return calc(exp1) * calc(exp2)
    div_index = expression.find('/')
    if div_index != -1:
        exp1 = expression[0:div_index]
        exp2 = expression[div_index+1:]
        return calc(exp1) / calc(exp2)
    return float(expression)


print(f'{calc("1+5*6-4/7+8")}')
