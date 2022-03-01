junior_cyclists = int(input())
senior_cyclists = int(input())
type_track = input()

total_cyclists = junior_cyclists + senior_cyclists

if type_track == "trail":
    junior_tax = 5.50
    senior_tax = 7
    total_tax_raised = (junior_tax * junior_cyclists) + (senior_tax * senior_cyclists)
    costs = total_tax_raised * 0.05
    money_left = total_tax_raised - costs
    print(f"{money_left:.2f}")
elif type_track == "downhill":
    junior_tax = 12.25
    senior_tax = 13.75
    total_tax_raised = (junior_tax * junior_cyclists) + (senior_tax * senior_cyclists)
    costs = total_tax_raised * 0.05
    money_left = total_tax_raised - costs
    print(f"{money_left:.2f}")
elif type_track == "road":
    junior_tax = 20
    senior_tax = 21.50
    total_tax_raised = (junior_tax * junior_cyclists) + (senior_tax * senior_cyclists)
    costs = total_tax_raised * 0.05
    money_left = total_tax_raised - costs
    print(f"{money_left:.2f}")
elif type_track == "cross-country":
    junior_tax = 8
    senior_tax = 9.50
    if total_cyclists >= 50:
        total_tax_raised = (junior_tax * junior_cyclists) + (senior_tax * senior_cyclists)
        tax_discount = total_tax_raised - (total_tax_raised * 0.25)
        costs_discount = tax_discount * 0.05
        money_left_discount = tax_discount - costs_discount
        print(f"{money_left_discount:.2f}")
    else:
        total_tax_raised = (junior_tax * junior_cyclists) + (senior_tax * senior_cyclists)
        costs = total_tax_raised * 0.05
        money_left = total_tax_raised - costs
        print(f"{money_left:.2f}")