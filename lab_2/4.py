# if temperature is greater than 30, its a hot day otherwise if its less than 10,
# its a cold day, otherwise is neither hot nor cold.

temp = int(input("Enter a temperature:"))
if temp >= 30:
    print("Its a hot day")
elif temp <= 10:
    print(" Its a cold day")
else:
    print("Its neither hot nor cold")

