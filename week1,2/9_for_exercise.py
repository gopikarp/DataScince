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

