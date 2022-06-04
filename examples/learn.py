#a = 5
#b = 7
# if a > b:
#    result = a - b
# else:
#    result = b - a
#print('result:', result)

def practicum():
    args = {
        0: 'Практикум',
        1: 'Яндекс',
    }
    args[0] = 'Яндекс'
    args[1] = 'Практикум'
    return [a for a in args.keys()]


print(practicum())
