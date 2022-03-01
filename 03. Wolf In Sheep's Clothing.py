searching_string = input()
word_count = searching_string.split()
eaten_sheep_counter = 0
wolf_counter = 0
position_counter = 0
sheep_count = 0

for animal in word_count[::-1]:
    position_counter += 1
    if animal == 'wolf,' or animal == 'wolf':
        wolf_counter += position_counter
    if wolf_counter > 0:
        eaten_sheep_counter = wolf_counter - 1
    sheep_count += 1

if wolf_counter == 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {eaten_sheep_counter}! You are about to be eaten by a wolf!" )