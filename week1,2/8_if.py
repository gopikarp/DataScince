## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#i Write a program that asks user to enter a city name and it should tell which country the city belongs to
"""city_name = input('enter a city name ')

if city_name in india: 
    print(f'{city_name} in india')
elif city_name in pakistan: 
    print(f'{city_name} in pakistan')
elif city_name in bangladesh: 
    print(f'{city_name} in bangladesh')
else :
    print(f'invalid')
"""
#ii Write a program that asks user to enter two cities and it tells you if they both are in same 
# country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" 
# but if I enter mumbai and dhaka it should print "They don't belong to same country"
"""city = input('enter 1st city')
city2 = input('enter 2nd city')

if city in india and city2 in india :
     print("Both cities are in india" )
elif  city in pakistan and city2 in pakistan :
     print("Both cities are in pakistan" )
elif  city in bangladesh and city2 in bangladesh :
     print("Both cities are in bangladesh" )
else :
    print('They don t belong to same country')
"""
# Write a python program that can tell you if your sugar is normal or not. Normal fasting level 
# sugar range is 80 to 100.
# i Ask user to enter his fasting sugar level

lev = input('enter fasting sugar level')
lev = float(lev)
# If it is below 80 to 100 range then print that sugar is low
if lev<80 : print(f'{lev} is lower')
# If it is above 100 then print that it is high otherwise print that it is normal
elif lev>100 : print(f'{lev} is high')
else : print('normal')
