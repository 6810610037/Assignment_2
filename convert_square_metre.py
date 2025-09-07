#convert_square_metre

x,y = input().split()
x = int(x)
y = int(y)
rai = x / 1600
work = x / 400
square_wah = x / 4
if y == 1:
    result = rai
if y == 2:
    result = work
if y == 3:
    result = square_wah
print(f"{result:.2f}")