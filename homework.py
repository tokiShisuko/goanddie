#Assingment 1

user_name = str(input("Input your name. "))
user_num = int(input("Inpur your number. "))
if user_num < 10:
    for i in range(user_num):
        print(user_name) 
else:
    for m in range(3):
        print("Number is too high")


#Assignment 2









#Assignment 3

dir = input("Which direction do you want to count? ")
if dir == "up" or dir == "UP" or dir == "up":
    max_num = int(input("Input your maximum number "))
    for i in range (1 , max_num+1):
        print(i)
elif dir == "down" or dir == "DOWN" or dir == "Down":
    min_num = int(input("Input a number below 20 "))
    for m in range (20 , min_num-1, -1):
        print(m)
else:
    print("I don't understand")




#Assignment 4

invite = int(input("How many people would you like to invite?"))
if invite < 10:
    for i in range(invite):
        name = str(input("Who would you like to invite?"))
        print(f"{name} has been invited")
elif invite > 10:
    print("Too many people!")
