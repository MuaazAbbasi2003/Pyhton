# with open("./weather_data.csv") as file:
#     contents = file.readlines()
#
# print(contents)

# import csv
# import pandas
#
#
# with open("./weather_data.csv") as file:
#     data= csv.reader(file)
#     temperatures=[]
#     for row in data:
#         try:
#             temp= int(row[1])
#             temperatures.append(temp)
#         except ValueError:
#             continue
# print(temperatures)

import pandas

data= pandas.read_csv("./weather_data.csv")
print(data["temp"])

