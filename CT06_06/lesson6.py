print("Hello from lesson 6")

Students = int(input("How many students are there in the class? "))
TotScore = 0

for i in range(Students):
    Score = int(input("What did this student get? "))
    TotScore = TotScore + Score

    print("The average score is: " + str(TotScore/Score))
