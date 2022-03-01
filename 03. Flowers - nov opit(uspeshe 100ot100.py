chrysanthemum = int(input())
roses = int(input())
tulips = int(input())
season = input()
is_it_holiday = input()


total_flowers = chrysanthemum + roses + tulips

if season == "Spring" or season == "Summer":
    flowers_price = chrysanthemum * 2 + roses * 4.10 + tulips * 2.50
elif season == "Winter" or season == "Autumn":
    flowers_price = chrysanthemum * 3.75 + roses * 4.50 + tulips * 4.15



if is_it_holiday == "Y":
    flowers_price = flowers_price + (flowers_price * 0.15)
    if tulips > 7 and season == "Spring":
        flowers_price = flowers_price - (flowers_price * 0.05)
        if total_flowers > 20:
            flowers_price = flowers_price - (flowers_price * 0.20)
        else:
            flowers_price = flowers_price
    elif roses >= 10 and season == "Winter":
        flowers_price = flowers_price - (flowers_price * 0.10)
        if total_flowers > 20:
            flowers_price = flowers_price - (flowers_price * 0.20)
        else:
            flowers_price = flowers_price
    elif total_flowers > 20:
        flowers_price = flowers_price - (flowers_price * 0.20)
    else:
        flowers_price = flowers_price
elif is_it_holiday == "N":
    flowers_price = flowers_price
    if tulips > 7 and season == "Spring":
        flowers_price = flowers_price - (flowers_price * 0.05)
        if total_flowers > 20:
            flowers_price = flowers_price - (flowers_price * 0.20)
        else:
            flowers_price = flowers_price
    elif roses >= 10 and season == "Winter":
        flowers_price = flowers_price - (flowers_price * 0.10)
        if total_flowers > 20:
            flowers_price = flowers_price - (flowers_price * 0.20)
        else:
            flowers_price = flowers_price
    elif total_flowers > 20:
        flowers_price = flowers_price - (flowers_price * 0.20)
    else:
        flowers_price = flowers_price
print(f"{flowers_price + 2:.2f}")