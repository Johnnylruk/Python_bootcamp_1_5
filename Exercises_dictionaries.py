# # data = {}

# # data['Name'] = str(input("What's the student name? ")).strip().title()
# # data['Mean'] = float(input("What's the student mean? "))

# # if data['Mean'] >= 7:
# #     data['Status'] = f"The status is Passed."
# # elif data['Mean'] < 7:
# #     data['Status'] = f"The status is failed."

# # print(f"The student name is {data['Name']}.")
# # print(f"Mean is equal to {data['Mean']}.")
# # print(f"{data['Status']}")

# from random import randint
# import time
# from operator import itemgetter

# Players = {}
# ranking = []

# Players["Player1"] = randint(1,6)
# Players["Player2"] = randint(1,6)
# Players["Player3"] = randint(1,6)
# Players["Player4"] = randint(1,6)

# for k,v in Players.items():
#     print(f"The {k} dice was {v}.")
#     time.sleep(1)
# print("-=" * 30)
# print("             Players Ranking: ")
# print("-=" * 30)

# ranking = sorted(Players.items(), key=itemgetter(1), reverse=True)

# for k,v in enumerate(ranking):
#     print(f"{k + 1} place {v[0]} with {v[1]} points.")


data = {
    'Name': str(input('Name: ')),
    'DOB': - int(input("Type your date of birth: ")) + 2025,
    'contract': int(input("How many years of work: "))
}

if data['contract'] == 0:
    print(data)
    print(f"Name got {data['Name']} as value.")
    print(f"Age is {data['DOB']}")
    print(f"Contrac have {data['contract']} years")
else:
    data['Hired'] = int(input("When it was the first year hired? "))
    data['Retirement'] = (data['Hired'] - (2025 - data['DOB'])) + 35
    data['Salary'] = int(input("What's the salary? "))

    print(data)
    print(f"Name got {data['Name']} as value.")
    print(f"Age is {data['DOB']}")
    print(f"Contrac have {data['contract']} years")
    print(f"Hired data has the value of {data['Hired']}")
    print(f"Salary has the value of {data['Salary']}")
    print(f"Retirement has the value of {data['Retirement']}")

    

# se hire != 0
# add year hired
# salary
# calc when is retirement which is after 35 years of first hired

