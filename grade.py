def result(m1,m2,m3):
    total=m1 + m2 + m3
    percentage = total / 3

    if percentage>=98:
        grade="S"
    elif percentage>=92:
        grade="A"
    elif percentage>=85:
        grade="B"
    else:
        grade="D"
        print("total marks:")
        print("percentage marks=",percentage)
        print("grade=",grade)

m1 = float(input("enter mark1: "))
m2 = float(input("enter mark2: "))
m3 = float(input("enter mark3: "))
result(m1,m2,m3)
