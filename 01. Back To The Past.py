money_inherited = float(input())
year_that_he_should_live = int(input())

year_back = 1800
age_count = 0
age = 0
money_spend_in_odd_year = 0


for year_that_he_should_live in range(year_back, year_that_he_should_live + 1):
    age_count += 1
    if year_that_he_should_live % 2 == 0:
        money_inherited -= 12000
    else:
        money_spend_in_odd_year = 12000 + (50 * age)
        money_inherited -= money_spend_in_odd_year
    age = 18 + age_count

if money_inherited > 0:
    print(f"Yes! He will live a carefree life and will have {money_inherited:.2f} dollars left.")
else:
    print(f"He will need {abs(money_inherited):.2f} dollars to survive.")