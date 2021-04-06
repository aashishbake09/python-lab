# Price of a house is $1M. If the buyer has good credit, they need to put down 10%
# otherwise they need to put down 20%.
# Print the down payment.

price = 100000
good_credit = input("Do you have good credit")
if good_credit == "true":
    Down_payment = 0.1 * price
else:
    Down_payment = 0.2 * price
print(f"Down_payment: ${Down_payment}")

