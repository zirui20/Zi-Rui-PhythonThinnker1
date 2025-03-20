# print("Hello from lesson 9")


# import random

# v1 = random.randint(1, 6)
# v2 = random.randint(1, 6)
# v3 = random.randint(1, 6)

# v1_isEven = (v1 % 2)== 0
# v2_isEven = (v2 % 2)== 0
# v3_isEven = (v3 % 2)== 0

# all_isSame = v1_isEven == v2_isEven == v3_isEven

# print("1st number is: " + str(v1))
# print("2nd number is: " + str(v2))
# print("3rd number is: " + str(v3))
# print("All the numbers are odd/even: " + str(all_isSame))



# import random

# num1 = str(random.randint(1,10))

# Num = input("Guess the number ")

# if Num == num1:
#     print("CoRReCt")

# else:
#     print("Failure")



ap = int(input("How many apoles do you want? "))

price = ap * 1


if ap >10:
    price = ap * 0.9 

print("You will have a 10% discount")
print("You will have to pay: $" + str(price))


