#1 After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads
""""
count = 0
for x in result:
    if x == "heads":
        count+=1
        print('head',count)
"""
#2 Print square of all numbers between 1 to 10 except even numbers

for x in range(1,10):
    if x % 2 == 0:
      continue
    print(x*x)

#3 Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
months = ["Jan", "Feb", "Mar", "Apr", "May"]
# Write a program that asks you to enter an expense amount and program should tell
# you in which month that expense occurred. If expense is not found then it should print that as well.
month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')