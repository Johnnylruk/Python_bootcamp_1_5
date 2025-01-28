# data = {}

# data['Name'] = str(input("What's the student name? ")).strip().title()
# data['Mean'] = float(input("What's the student mean? "))

# if data['Mean'] >= 7:
#     data['Status'] = f"The status is Passed."
# elif data['Mean'] < 7:
#     data['Status'] = f"The status is failed."

# print(f"The student name is {data['Name']}.")
# print(f"Mean is equal to {data['Mean']}.")
# print(f"{data['Status']}")

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


# data = {
#     'Name': str(input('Name: ')),
#     'DOB': - int(input("Type your date of birth: ")) + 2025,
#     'contract': int(input("How many years of work: "))
# }

# if data['contract'] == 0:
#     print(data)
#     print(f"Name got {data['Name']} as value.")
#     print(f"Age is {data['DOB']}")
#     print(f"Contrac have {data['contract']} years")
# else:
#     data['Hired'] = int(input("When it was the first year hired? "))
#     data['Retirement'] = (data['Hired'] - (2025 - data['DOB'])) + 35
#     data['Salary'] = int(input("What's the salary? "))

#     print(data)
#     print(f"Name got {data['Name']} as value.")
#     print(f"Age is {data['DOB']}")
#     print(f"Contrac have {data['contract']} years")
#     print(f"Hired data has the value of {data['Hired']}")
#     print(f"Salary has the value of {data['Salary']}")
#     print(f"Retirement has the value of {data['Retirement']}")

    

# player ={
#     'Name': str(input("Name: ")),
#     'Matches': int(input("How many matches: "))
# }
# scores = []
# total_score = 0
# for score in range(player['Matches']):
#     scores.append(int(input(f"How many score on game{score + 1}: ")))
# player['Scores'] = scores
# #player['Total_score'] = sum(scores)
# for score in scores:
#     total_score += score
# player['Total_score'] = total_score
# print('-=' * 40)
# print(player)
# print('-=' * 40)
# print(f"Field name has the value of {player['Name']}")
# print(f"Field scores has the value of {player['Scores']}")
# print(f"Field total scores has the value of {player['Total_score']}")
# print('-=' * 40)
# print(f"The player {player['Name']} played {player['Matches']}.")
# for match in range(player['Matches']):
#         print(f'   => Match {match + 1}, scored {scores[match]}')    

num = 0
data = dict()
list_data = list()
count = 0
age_sum = 0
woman_list= list()
above_average_age = list()

while True:
    data['Name'] = str(input('Name: '))
    data['Age'] = int(input('Age: '))
    data['Gender'] = str(input('Gender [M/F]: ')).upper()
    list_data.append(data.copy())
    answer = str(input("Do you want to continue? [Y/N]"))
    if answer in 'Nn':
        for people in list_data:
            count += 1
        print(f"{count} were sucesfull registered")
        for dt in list_data:
            for k, v in dt.items():
                if k == 'Age':
                    age_sum += v
                elif v == 'F':
                    woman_list.append(dt['Name'])
        mean = age_sum / count
        print(f'The age mean is: {mean}')
        for person in list_data:
            for k, v in person.items():
                if k == 'Age':
                    if v > mean:
                        if v not in above_average_age:
                            above_average_age.append(person.copy())
        if len(woman_list) != 0:     
            print(f"This/These are the woman registered: {woman_list}")
        if len(above_average_age) != 0:
            for person in above_average_age:
                for k, v in person.items():
                    print(f'{k} = {v}', end='; ')
        break
            