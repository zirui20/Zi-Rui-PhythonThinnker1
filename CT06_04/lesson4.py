

red = 1
blue = 2
green = 3


numRed = input("How many Red plates of sushi have you eaten? ")
numBlue = input("How many Blue plates of sushi have you eaten? ")
numGreen = input("How many Green plates of sushi have you eaten? ")

total = (int(numRed) * red) + (int(numBlue) * blue) + (int(numGreen) * green)
print (total)

print("You have spent a total of $" + str(total))