from World import World
import time
from _datetime import date, timedelta


# placing information of each canadian province and its borders in regionData
regionData = list([])
regionData.append(("Ontario", ["Quebec", "Manitoba", "Nunavut"]))
regionData.append(("British Columbia", ["Alberta", "Yukon", "Northwest Territories"]))
regionData.append(("Alberta", ["British Columbia", "Yukon", "Northwest Territories", "Saskatchewan", "Nunavut"]))
regionData.append(("Manitoba", ["Northwest Territories", "Saskatchewan", "Nunavut", "Ontario"]))
regionData.append(("Saskatchewan", ["Northwest Territories", "Nunavut", "Manitoba", "Alberta"]))
regionData.append(("Yukon", ["British Columbia", "Northwest Territories"]))
regionData.append(("Nova Scotia", ["Quebec", "Newfoundland and Labrador", "New Brunswick", "Prince Edward Island"]))
regionData.append(("New Brunswick", ["Quebec", "Newfoundland and Labrador", "Prince Edward Island", "Nova Scotia"]))
regionData.append(("Newfoundland and Labrador", ["Quebec", "New Brunswick", "Prince Edward Island", "Nova Scotia"]))
regionData.append(("Prince Edward Island", ["Quebec", "New Brunswick", "Nova Scotia", "Newfoundland and Labrador"]))
regionData.append(("Northwest Territories", ["Nunavut", "Manitoba",
                                             "Alberta", "Saskatchewan", "British Columbia", "Yukon"]))
regionData.append(("Nunavut", ["Quebec", "Newfoundland and Labrador",
                               "Ontario", "Manitoba", "Saskatchewan", "Northwest Territories"]))
regionData.append(("Quebec", ["Ontario", "Newfoundland and Labrador",
                              "New Brunswick", "Prince Edward Island", "Nova Scotia"]))

canada = World(regionData)
current_date = date(2020, 1, 1)

print("---------------------------------------------------")
print(str(current_date.month)+'\\'+str(current_date.day)+'\\'+str(current_date.year))
print(canada)
print("---------------------------------------------------")


while canada.not_united():
    time.sleep(.0)
    current_date = current_date + timedelta(30)
    canada.update()
    print("---------------------------------------------------")
    print(str(current_date.month) + '\\' + str(current_date.day) + '\\' + str(current_date.year))
    print(canada)
    print("---------------------------------------------------")
print("winner is ", canada.winner().name())
