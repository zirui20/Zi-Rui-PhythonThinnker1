print("Hello from lesson 11")

px = int(input("What is the price of your item? "))

if px <= 5:
    print("Sounds good!")
elif px <= 50:
    print("Urm are you sure you need this?")
elif px <= 500:
    print("DID YOU STEAL THIS MONEY?")
elif px > 500:
    print("😭🙏 What?")