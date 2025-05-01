def f(x):
    return 2.71828**x

values=[]

a = int(input("Define starting input value: "))
b = int(input("Define ending input value: "))
strip_num= int(input("Define numberof strips: "))

diff= (b-a)/strip_num

edge_total= f(a) +f(b)

middle_total = 0

count=a
while count < b:
    middle_total += f(count)
    count += diff

total_area = (diff/2)*(edge_total+ 2*middle_total)
print(total_area)
