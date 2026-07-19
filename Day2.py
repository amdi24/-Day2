total_bill = 4444
number_of_people = 4
friends = ["Alice", "Bob", "Charlie", "David"]
# this is oure function 
def split_bill(total_bill, number_of_people, tip_rate=0.10):
    tip_amount = total_bill * tip_rate
    total_payment = total_bill + tip_amount  #oure paymant include the tip_rate 
    per_person_share = total_payment/number_of_people # individual person paymant
    return per_person_share
print("individual share")
for name in friends:
    print(f"resive paymant person {name},individual paymant is {split_bill(total_bill, number_of_people)}") 
    # hear for each person we are calling the function and 
    #passing the total_bill and number_of_people as arguments to calculate the individual share of the bill including the tip.