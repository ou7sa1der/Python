degrees = int(input())
time_of_day = input()

#От конзолата се четат точно два реда:
#    • Градусите - цяло число;
#   • Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".

if time_of_day == "Morning":
    if degrees >= 10 and degrees <= 18:
        print(f"It's {degrees} degrees, get your Sweatshirt and Sneakers.")
    elif degrees > 18 and degrees <= 24:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
elif time_of_day == "Afternoon":
    if degrees >= 10 and degrees <= 18:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees > 18 and degrees <= 24:
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your Swim Suit and Barefoot.")
elif time_of_day == "Evening":
    if degrees >= 10 and degrees <= 18:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees > 18 and degrees <= 24:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")