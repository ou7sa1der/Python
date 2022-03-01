skumriq_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

midi_price = 7.50

palamud_price = skumriq_price + skumriq_price * 0.60
total_palamud = palamud_kg * palamud_price

safrid_price = caca_price + caca_price * 0.80
total_safrid = safrid_kg * safrid_price

total_midi = midi_kg * midi_price

total = total_midi + total_safrid + total_palamud

print(f'{total:.2f}')