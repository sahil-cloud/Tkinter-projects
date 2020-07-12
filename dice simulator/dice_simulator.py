#making the dice simulator
from random import randrange,randint

a=randint(1,6)
#printing the outside boundry

# if a==0:
    

for i in range(1,7):
    if i<=3:
        if a == i:
            print("[''''''''''''''']")
            print("[", end="               ")
            print("]")
            print("[", end="    ")
            print(" * "*i)
            # print("]")
            print("[", end="               ")
            print("]")
            print("[,,,,,,,,,,,,,,,]")
    else:
        if a == i:
            c = a-3
            print("[''''''''''''''']")
            print("[", end="               ")
            print("]")
            print(end="       ")

            print("* * *")
            print(end="       ")
            print(" * "*c)
            # print("]")
            print("[", end="               ")
            print("]")
            print("[,,,,,,,,,,,,,,,]")

# print(' * '*3)
