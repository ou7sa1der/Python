chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

total_flowers_bought = chrysanthemums + roses + tulips

if season == "Summer" or season == "Spring":
    if holiday == "Y":
        price = chrysanthemums * 2 + roses * 4.10 + tulips * 2.50
        holiday_day = price + (price * 0.15)
        if season == "Spring" and tulips > 7:
            price_discount = holiday_day - (holiday_day * 0.05)
            if total_flowers_bought > 20:
                price_discount_two = price_discount - (price_discount * 0.20)
                arrange_price = price_discount_two + 2
                print(f"{arrange_price:.2f}")
            else:
                arrange_price = price_discount + 2
                print(f"{arrange_price:.2f}")
        else:
            arrange_price = holiday_day + 2
            print(f"{arrange_price:.2f}")
    elif holiday == "N":
        price = chrysanthemums * 2 + roses * 4.10 + tulips * 2.50
        if season == "Spring" and tulips > 7:
            price_discount = price - (price * 0.05)
            if total_flowers_bought > 20:
                price_discount_two = price_discount - (price_discount * 0.20)
                arrange_price = price_discount_two + 2
                print(f"{arrange_price:.2f}")
            else:
                arrange_price = price_discount + 2
                print(f"{arrange_price:.2f}")
        elif total_flowers_bought > 20:
            price_discount_two = price - (price * 0.20)
            arrange_price = price_discount_two + 2
            print(f"{arrange_price:.2f}")
        else:
            arrange_price = price + 2
            print(f"{arrange_price:.2f}")
elif season == "Winter" or season == "Autumn":
    if holiday == "Y":
        price = chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15
        holiday_day = price + (price * 0.15)
        if season == "Winter" and roses >= 10:
            price_discount = holiday_day - (holiday_day * 0.10)
            if total_flowers_bought > 20:
                price_discount_two = price_discount - (price_discount * 0.20)
                arrange_price = price_discount_two + 2
                print(f"{arrange_price:.2f}")
            else:
                arrange_price = price_discount + 2
                print(f"{arrange_price:.2f}")
        else:
            arrange_price = holiday_day + 2
            print(f"{arrange_price:.2f}")
    elif holiday == "N":
        price = chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15
        if season == "Winter" and roses >= 10:
            price_discount = price - (price * 0.10)
            if total_flowers_bought > 20:
                price_discount_two = price_discount - (price_discount * 0.20)
                arrange_price = price_discount_two + 2
                print(f"{arrange_price:.2f}")
            else:
                arrange_price = price_discount + 2
                print(f"{arrange_price:.2f}")
        elif total_flowers_bought > 20:
            price_discount_two = price - (price * 0.20)
            arrange_price = price_discount_two + 2
            print(f"{arrange_price:.2f}")
        else:
            arrange_price = price + 2
            print(f"{arrange_price:.2f}")