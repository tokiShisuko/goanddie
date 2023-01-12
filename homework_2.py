#Assignment 1

import random
r = random.randint(1,99)
while True:
    guess = int(input("Input a number betwen 1 and 100 "))
    if guess > r:
        print("Too high!")
    elif guess < r:
        print("Too low!")
    else:
        print("Correct!")
        break

#Assigment 2

list = [1, 5, 23, 26, 43, 6594, 456, 424]

print(list[0] + list[1] + list[2]+ list[3]+ list[4]+ list[5]+ list[6]+ list[7])



#Assignment 3

usr_wrd = input("Input an English letter (all small) ")
first = usr_wrd[0]
lst = usr_wrd[1::]
if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
    print(usr_wrd + "way")
else:
    print(lst + first + "ay")

#Assignment 4

mylist = [1,2,3,4,5]
print(mylist[0::4])
mylist2 = ['a','b','c','d']
print(mylist2[0::3])

#Assigment 5

hobbies = [ "football","coding"]
user_hobby = input("What is your favourite hobby?")
hobbies.append(user_hobby)
hobbies.sort()
print(hobbies)

#Assignment 6

sub = ['Myanmar', "English", "Math", "History", "Geography", "Science", ]
del_sub = input("Which of these don't you like? ")
if del_sub in sub:
    sub.remove(del_sub)
print(sub)

