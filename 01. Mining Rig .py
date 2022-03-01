import math
price_for_video_card = int(input())
price_for_trasitioner = int(input())
price_for_used_power = float(input())
winning_from_one_device = float(input())

total_price_for_vcards = price_for_video_card * 13
total_price_for_transitioners = price_for_trasitioner * 13
spend_money = total_price_for_vcards + total_price_for_transitioners + 1000
winning_for_day = winning_from_one_device - price_for_used_power
total_winnings_per_day = 13 * winning_for_day
days_to_return_investment = spend_money / total_winnings_per_day

print(spend_money)
print(math.ceil(days_to_return_investment))