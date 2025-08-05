employees = [
    {"name": "Juan", "age": 28, "salary": 3500},
    {"name": "María", "age": 32, "salary": 4200},
    {"name": "Carlos", "age": 25, "salary": 3100},
    {"name": "Ana", "age": 40, "salary": 5000},
    {"name": "Luis", "age": 30, "salary": 3900},
]

# for row in employees:
#     print(row["name"])


def good():

    names = [employee['name'] for employee in employees if employee['salary'] > 4000]
    print(names)


    # list = []
    # for employee in employees:
    #     if employee['salary'] > 4000:
    #         list.append(employee['name'])
    # print(list)
    

good()