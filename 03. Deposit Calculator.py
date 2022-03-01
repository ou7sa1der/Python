deposit_sum = float(input())
deposit_time = int(input())
yearly_interest = float(input())

interest = deposit_sum * (yearly_interest / 100)
interest_for_one_month = interest / 12
total_sum = deposit_sum + (deposit_time * interest_for_one_month)

print(total_sum)