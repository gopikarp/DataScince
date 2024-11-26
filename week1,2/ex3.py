# 1You have a football field that is 92 meter long and 48.8 meter wide. 
# Find out total area using python and print it.
length = 92
width = 48.8
area = length*width
print("total area ",area)

# 2You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave 
# shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
boughtPack = 9
packCost = 1.49
givenAmt = 20

totalAmt = boughtPack*packCost
returnBalance = givenAmt - totalAmt
print("the shopkeeper give you the balance amount of",returnBalance,"$")
# 3You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. 
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. 
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
 
length = 5.5
tileCost = 500
area = length*length
cost = area*tileCost
print("Total cost is",cost)


# 4) Print binary representation of number 17
num = 17
print("binary number is",format(num,'b'))#'b', which means binary format.