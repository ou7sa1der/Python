x = float(input())
y = float(input())
h = float(input())

#steni
side_wall = x * y
window = 1.5 * 1.5
two_sides_total = 2 * side_wall - 2 * window
back_wall = x * x
entrance = 1.2 * 2
front_and_back = 2 * back_wall - entrance
total_walls_m_square = two_sides_total + front_and_back
green_paint_l = total_walls_m_square / 3.4

#pokriv
two_roof_rectangles = 2 * (x * y)
two_roof_triangles = 2 * (x * h / 2)
total_roof_m_square = two_roof_rectangles + two_roof_triangles
red_paint_l = total_roof_m_square / 4.3

print(f'{green_paint_l:.2f}')
print(f'{red_paint_l:.2f}')