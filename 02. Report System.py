total_sum_expected_for_sale = int(input())

paying_cash_counter = 0
paying_with_card_counter = 0
cash_sum = 0
card_sum = 0
total_sum = 0
counter = 0

command = input()

while command != "End" or total_sum < total_sum_expected_for_sale:
    counter += 1
    number = int(command)
    # винаги се редуват: плащане в брой и плащане с карта.
    if counter % 2 != 0:
        # Ако продуктът надвишава 100лв., за него не може да се плати в брой
        if number >= 100:
            print("Error in transaction!")
        elif number < 100:
            paying_cash_counter += 1
            cash_sum += number
            total_sum += number
            print("Product sold!")
        elif total_sum >= total_sum_expected_for_sale:
            break
    elif counter % 2 == 0:
    # Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
        if number <= 10:
            print("Error in transaction!")
        elif number < 100:
            paying_with_card_counter += 1
            card_sum += number
            total_sum += number
            print("Product sold!")
        elif total_sum >= total_sum_expected_for_sale:
            break
    command = input()

if command == "End":
    print("Failed to collect required money for charity.")

if total_sum >= total_sum_expected_for_sale:
    average_cash_sum = cash_sum / paying_cash_counter
    average_card_sum = card_sum / paying_with_card_counter
    print(f"Average CS: {average_cash_sum:.2f}")
    print(f"Average CC: {average_card_sum:.2f}")