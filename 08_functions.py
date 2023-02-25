print("My name is Abulhasan")
print("My name is Abulhasan")
print("My name is Abulhasan")
print("My name is Abulhasan")
print("My name is Abulhasan")

if we use a specific value again and again then we need it to make a function
so we can easily use that function,when needed
by using this we  can avoid big mistakes in the code


defining a function

1

def print_about_ali():
    print("My name is Abulhasan")
    print("My name is Abulhasan")
    print("My name is Abulhasan")

print_about_ali()         # this is a function call

2

we use def command for function

def print_tech():
    a="This is a large tech firm"
    print(a)
    print(a)
    print(a)


print_tech()           # this is a function call

defining a function with if , elif, else statements

def school_calculator(age_of_ali, school_going_age):

    if age_of_ali==school_going_age:
       print("Ali can go to school")

    elif age_of_ali > school_going_age:
       print("Ali should go for higher studies")

    elif age_of_ali == school_going_age:
       print("Ali can go to school")

    elif age_of_ali == 3:
       print(" He is a baby can't go to school ")

    else:
        print("Ali can not go to school")


school_calculator(3,9)


defining a future function

small machine learning code example for age prediction

def future_age(age):
    new_age=age+20;
    return new_age
    print(new_age)
future_predicted_age=future_age(18)
print(future_predicted_age)


# Import required modules
# import cv2 as cv
# import math
# import time
# from google.colab.patches import cv2_imshow

# input = cv.imread("2.jpg")
# output = age_gender_detector(input)
# cv2_imshow(output)


import math
print(math.pi,"value of pi is")
