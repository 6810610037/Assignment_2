x1, y1, x2, y2, x, y = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
x = float(x)
y = float(y)

if x1 == x2 or y1 == y2:
    print(-1)
elif (x1 < x < x2 and y1 < y < y2) or (x2 < x < x1 and y2 < y < y1):
    print(1)
else:
    print(0)
