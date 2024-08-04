# with open("Weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if not row[1] == 'temp':
#             temperatures.append(int(row[1]))

#     print(temperatures)    

import pandas

# data = pandas.read_csv("Weather_data.csv")

# monday = data[data.Day == "Monday"]
# # print(monday.condition)

# temp = monday.temp
# temp_F = (temp * (9 / 5)) + 32
# print(temp_F)


# data_dict = {
#         "students": ["Dave", "Magobo", "Zizwe"],
#         "scores": [76, 88, 92]
# }

# data = pandas.DataFrame(data_dict)
# print(data)

data = pandas.read_csv("squirrel_data.csv")

Gray_Fur = (data[data["Primary Fur Color"] == "Gray"])
count_grey = (Gray_Fur["Primary Fur Color"]).count()

Black_Fur = (data[data["Primary Fur Color"] == "Cinnamon"])
count_red = (Black_Fur["Primary Fur Color"]).count()


Red_Fur = (data[data["Primary Fur Color"] == "Black"])
count_black = (Red_Fur["Primary Fur Color"]).count()

squirrel_data = {
    "color": ["grey", "red", "black"],
    "count": [count_grey, count_red, count_black]
}

squirrel_count = pandas.DataFrame(squirrel_data)
squirrel_count.to_csv("./squirrel_count.csv")
