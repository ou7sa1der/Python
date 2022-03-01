w = float(input()) * 100
h = float(input()) * 100

seats_lost = 3
h_with_coridor = h - 100
desks_on_row = h_with_coridor // 70

rows = w // 120

seats_count = (rows * desks_on_row) - seats_lost
print(f'{seats_count:.0f}')


