center_x, center_y, radius, point_x, point_y = input().split()
center_x = float(center_x)
center_y = float(center_y)
radius = float(radius)
point_x = float(point_x)
point_y = float(point_y)
d = ((point_x - center_x) ** 2 + (point_y - center_y) ** 2) ** (1 / 2)


if d < radius:
    print(1)
else:
    print(0)
