time_period = int(input())

electricity_bill = 0
water_bill = time_period * 20
internet_bill = time_period * 15
others_bill = 0

for sum_bills in range(1, time_period + 1):
    electricity = float(input())
    electricity_bill += electricity
    others_percent = (electricity + 20 + 15) * 0.20
    others = (electricity + 20 + 15) + others_percent
    others_bill += others

average_bill_per_month = (electricity_bill + water_bill + internet_bill + others_bill) / time_period
print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {others_bill:.2f} lv")
print(f"Average: {average_bill_per_month:.2f} lv")