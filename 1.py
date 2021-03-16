second = int(input("enter seconds time: "))

minutes = second//60
print(f"Total minutes for given second:{minutes}")

day = (((second // 60)//60)//24)
print(f"Total day for given second:{day}")

hour = ((second//60)//60)
print(f"Total hour for given second:{hour}")