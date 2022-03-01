budget = float(input())
season = input()


if budget <= 100:
    if season == "summer":
        season_price = budget - (budget * 0.7)
        print("Somewhere in Bulgaria")
        print(f"Camp - {season_price:.2f}")
    elif season == "winter":
        season_price = budget - (budget * 0.3)
        print("Somewhere in Bulgaria")
        print(f"Hotel - {season_price:.2f}")
elif budget <= 1000:
    if season == "summer":
        season_price = budget - (budget * 0.6)
        print("Somewhere in Balkans")
        print(f"Camp - {season_price:.2f}")
    elif season == "winter":
        season_price = budget - (budget * 0.2)
        print("Somewhere in Balkans")
        print(f"Hotel - {season_price:.2f}")
elif budget > 1000:
    season_price = budget - (budget * 0.1)
    print("Somewhere in Europe")
    print(f"Hotel - {season_price:.2f}")