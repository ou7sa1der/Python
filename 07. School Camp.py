seaseon = input()
boys_or_girls = input()
students = int(input())
overnights = int(input())

price_discount = 0


if seaseon == "Spring":
    if boys_or_girls == "boys" or boys_or_girls == "girls":
        price_for_overnights = students * 7.20 * overnights
        if boys_or_girls == "girls":
            sport = "Athletics"
        else:
            sport = "Tennis"
    elif boys_or_girls == "mixed":
        sport = "Cycling"
        price_for_overnights = students * 9.50 * overnights
elif seaseon == "Winter":
    if boys_or_girls == "boys" or boys_or_girls == "girls":
        price_for_overnights = students * 9.60 * overnights
        if boys_or_girls == "girls":
            sport = "Gymnastics"
        else:
            sport = "Judo"
    elif boys_or_girls == "mixed":
        sport = "Ski"
        price_for_overnights = students * 10 * overnights
elif seaseon == "Summer":
    if boys_or_girls == "boys" or boys_or_girls == "girls":
        price_for_overnights = students * 15 * overnights
        if boys_or_girls == "girls":
            sport = "Volleyball"
        else:
            sport = "Football"
    elif boys_or_girls == "mixed":
        sport = "Swimming"
        price_for_overnights = students * 20 * overnights



if students >= 10 and students < 20:
    price_discount = price_for_overnights - (price_for_overnights * 0.05)
elif students >= 20 and students < 50:
    price_discount = price_for_overnights - (price_for_overnights * 0.15)
elif students >= 50:
    price_discount = price_for_overnights - (price_for_overnights * 0.50)
else:
    price_discount = price_for_overnights

print(f"{sport} {price_discount:.2f} lv.")