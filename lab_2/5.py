# if name is less than 3 character long- name must be at least 3 character,
# otherwise if its more than 50 character
# -name must be maximum of 50 character, otherwise - name look good.

name = input("enter your name: ")
length = len(name)
if length < 3:
    print("should be more than 3 characters")
elif length > 50:
    print("should be max of 50 character")
else:
    print("nice name")
