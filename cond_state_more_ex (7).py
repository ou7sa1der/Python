#Цени на играчките:
 #   • Пъзел - 2.60 лв.
  #  • Говореща кукла - 3 лв.
   # • Плюшено мече - 4.10 лв.
    #• Миньон - 8.20 лв.
    #• Камионче - 2 лв.

#Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от общата цена.
#От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# Ако парите са достатъчни се отпечатва:◦ "Yes! {оставащите пари} lv left."
#    • Ако парите НЕ са достатъчни се отпечатва:◦ "Not enough money! {недостигащите пари} lv needed."
#до втория знак след десетичната запетая.
price_for_vacation = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
trucks_count = int(input())

toys_sum = puzzle_count * 2.6 + talking_doll_count * 3 + teddy_bear_count * 4.1 + minion_count * 8.2 + trucks_count*2
toys_count = puzzle_count + talking_doll_count + teddy_bear_count + minion_count + trucks_count

if toys_count >= 50:
    toys_sum_discount = toys_sum - (toys_sum * 0.25)
    final_price_with_rent = toys_sum_discount - (toys_sum_discount * 0.1)
    if final_price_with_rent >= price_for_vacation:
        left_money = final_price_with_rent - price_for_vacation
        print(f'Yes! {left_money:.2f} lv left.')
elif toys_count < 50:
    money_with_rent = toys_sum - (toys_sum * 0.1)
    if money_with_rent < price_for_vacation:
        money_needed = price_for_vacation - money_with_rent
        print(f'Not enough money! {money_needed:.2f} lv needed.')
    elif money_with_rent > price_for_vacation:
        money_left = money_with_rent - price_for_vacation
        print(f'Yes! {money_left:.2f} lv left.')
