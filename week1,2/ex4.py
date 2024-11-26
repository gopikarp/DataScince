# Create 3 variables to store street, city and country, now create address variable to store entire address. 
#Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address 
# in such a way that the street, city and country prints in a separate line
street = "kv line"
city = "ernakulam"
country = "kerala"
address = street + '\n' + city + '\n' + country
print(address)
address = f'using f = {street}\n{city}'
print(address)

# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index
str =  "Earth revolves around the sun"
print(str[5:13])
print(str[-3:])

# Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits 
# daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
fruits = 'mango'
vegetables = 'tomato'
eat = f'I eat {vegetables} veggies and {fruits} fruits daily'
print(eat)
#I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement 
#is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. 
#Also try to do this in one line.

s='maine 200 banana khaye'
s= s.replace("banana","samosa")
s= s.replace("200","10")
print(s)
st= s.replace("banana","samosa").replace("200","10")
print("in one line-",st)