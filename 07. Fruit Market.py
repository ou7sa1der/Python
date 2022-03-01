strawbery_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberry_kg = float(input())
strawbery_kg = float(input())

raspberry_price = strawbery_price / 2
orage_price = raspberry_price - (0.4 * raspberry_price)
bananas_price = raspberry_price - (0.8 * raspberry_price)

raspberry_sum = raspberry_kg * raspberry_price
oranges_sum = oranges_kg * orage_price
bananas_sum = bananas_kg * bananas_price
strawbery_sum = strawbery_kg * strawbery_price

total_sum = raspberry_sum + oranges_sum + bananas_sum + strawbery_sum

print(total_sum)