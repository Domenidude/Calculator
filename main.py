import numpy


def f(num):
    global func
    x = num
    buffer_dict = {}
    exec(func, globals(), locals())
    export_val = buffer_dict['function']
    return export_val


func = "function = x**2 + 3"
a = float(input("Define starting input value: "))
b = float(input("Define ending input value: "))
strip_num = int(input("Define number of strips: "))

diff = (b - a) / strip_num

edge_total = f(a) + f(b)

middle_total = 0

count = a
while count < b:
    middle_total += f(count)
    count += diff

total_area = (diff / 2) * (edge_total + 2 * middle_total)
print(total_area)
