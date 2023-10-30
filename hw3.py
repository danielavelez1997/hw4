##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 

from functools import reduce

def count_simba(word,sentence):
    return sum(map(lambda sentence: sum(map(lambda x: 1 if word in x else 0,sentence.split())), sentence)) 

word= "Simba"
sentence=["Simba and Nala are lions.", "I laugh in the face of danger.","Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

count_simba(word,sentence)

#%%
# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 
import pandas as pd
from datetime import datetime


def get_day_month_year(my_date):
    days=list(map(lambda d:d.day ,my_date))
    months=list(map(lambda d:d.month ,my_date))
    year=list(map(lambda d:d.year ,my_date))
    data={'day':days,'month':months,'year':year}
    edited_data= pd.DataFrame(data)
    return edited_data 

dates = [datetime(2023, 10, 29)]
result = get_day_month_year(dates)
print(result)

#%%
# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#


import geopy.distance as gd
def compute_distance(geoInputs):
    #list comparision
    #distancePairs = [gd.geodesic(pair[0],pair[1]).kilometers for pair in geoInputs]

    #map
    distancePairs = list(map(lambda geoPair: gd.geodesic(geoPair[0],geoPair[1]).kilometers, geoInputs))
    return distancePairs

geoCoordiSets = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
print(compute_distance(geoCoordiSets),"unit in kilometer")

#%%
#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

def sum_general_int_list(integerSets):
    sum = 0
    for integerList in integerSets:
        # if is int type, we return and sum together
        if type(integerList) == int: sum += integerList

        #else is a nested List, we recursive deep down
        else: sum += sum_general_int_list(integerList)
    return sum


integerNestedList = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
print("integerNestedList sum is: ", sum_general_int_list(integerNestedList))
list_1=[[2], 3, [[1,2],5]]
print("list_1 sum is: ", sum_general_int_list(list_1))