budget = float(input())
season = input()

if budget <= 1000:
    place_staying = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:
        location = "Morocco"
        price = budget * 0.45
elif budget > 1000 and budget <= 3000:
    place_staying = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    else:
        location = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    place_staying = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    else:
        location = "Morocco"
        price = budget * 0.90

print(f"{location} - {place_staying} - {price:.2f}")