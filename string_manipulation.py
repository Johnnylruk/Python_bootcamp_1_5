name = input("Please type your name ")

name_upper = name.upper()
name_lower = name.lower()

total_letters = name.replace(" ", "")

name_split = name.split()

print(f"The user full name with all upper case letters is {name_upper} ")
print(f"The user full name with all lower case letters is {name_lower} ")
print(f"The count of total letters is: {len(name)} and the letters without space is: {len(total_letters)} ")
print(f"The user first name is {name_split[0]} ")