month = input()
overnights = int(input())

price_for_apartment = 0
price_for_studio = 0

#    • На първия ред е месецът – May, June, July, August, September или October;
#    • На втория ред е броят на нощувките – цяло число.
#Предлагат се и следните отстъпки:
#    • За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
#    • За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
#    • За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
#    • За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

if month == "May" or month == "October":
    price_for_apartment = overnights * 65
    price_for_studio = overnights * 50
    if overnights > 7 and overnights <= 13:
        price_for_studio = price_for_studio - (price_for_studio * 0.05)
        print(f"Apartment: {price_for_apartment:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")
    elif overnights > 14:
        price_for_apartment = price_for_apartment - (price_for_apartment * 0.10)
        price_for_studio = price_for_studio - (price_for_studio * 0.30)
        print(f"Apartment: {price_for_apartment:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")
    else:
        print(f"Apartment: {price_for_apartment:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")
elif month == "June" or month == "September":
    price_for_apartment = overnights * 68.70
    price_for_studio = overnights * 75.20
    if overnights > 14:
        price_for_apartment = price_for_apartment - (price_for_apartment * 0.10)
        price_for_studio = price_for_studio - (price_for_studio * 0.20)
        print(f"Apartment: {price_for_apartment:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")
    else:
        print(f"Apartment: {price_for_apartment:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")
elif month == "July" or month == "August":
    price_for_apartment = overnights * 77
    price_for_studio = overnights * 76
    if overnights > 14:
        price_for_apartment = price_for_apartment - (price_for_apartment * 0.10)
        print(f"Apartment: {price_for_apartment:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")
    else:
        print(f"Apartment: {price_for_apartment:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")