n_kilometers = int(input())
time_period = input()

#    • Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
if n_kilometers < 20:
    if time_period == "day":
        taxi_price = 0.7 + (n_kilometers * 0.79)
        print(f"{taxi_price:.2f}")
    else:
        taxi_price = 0.7 + (n_kilometers * 0.90)
        print(f"{taxi_price:.2f}")
#    • Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
elif n_kilometers >= 20 and n_kilometers < 100:
    bus_price = n_kilometers * 0.09
    print(f"{bus_price:.2f}")
#    • Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.
else:
    train_price = n_kilometers * 0.06
    print(f"{train_price:.2f}")