#Assignment 1

def count_digit(number):
    print(len(number))
number = input("Type numbers as you like. ")
count_digit(number)

#Assigment 2

def bigger_sum(number):
    num_1 = int(input('Input a number!'))
    num_2 = int(input('Input a number!'))
    num_3 = int(input('Input a number!'))
    number = [num_1, num_2, num_3]
    ma = max(number)
    number.remove(ma)
    mu = max(number)
    number.remove(mu)
    last_num = ma **2 + mu**2
    print(last_num)
    
bigger_sum(number)
#Assignment 3

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if  year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

year = int(input("Input a year! "))
is_leap_year(year)

#Assignment 4

def area_of_circle(r):
    a = r **2 * 22/7
    print(a)
r = int(input("Input the radious of the curcle"))
area_of_circle(r)
