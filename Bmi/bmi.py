#!/usr/bin/env python3

from time import sleep
from gpiozero import LED

# ToDo accept input for positive  integers ONLY, and make it a function
# DONE INTERNALLY ONLY - ToDo change bmi height/weight calculations to a func
# ToDo  change code for RGB LED tesing

def calc_meters(height):
    return  height * .0254

def calc_kilograms(weight):
    return weight / 2.2046

def calc_bmi(kilograms, meters):
    return  kilograms / meters**2

def get_int_from_user(userprompt):
    return  int(input(userprompt))


# red = 17ellow =27 green =22
red_led = LED(17) # under weight and obese
yellow_led = LED(27) # overweight
green_led = LED(22) # normal weight

# Welcome to JAYY BMI Calculator calculator
print("Welcome to JAYS BMI Calculator\n")

# Get height from user
height = get_int_from_user("Please enter your height in inches: ")

# Convert from inches to meters
# inches * 0.0254
meters = calc_meters(height)
print("your height in meters is: " + str(meters))

# Convert from meters to centimeters
# multiply meters X 100
###centimeters = meters * 100
###print("your height in centimeters is: " + str(centimeters))

# Get weight from user
weight = get_int_from_user("Please enter your weight in pounds: ")
print()

#convert from pounds to kilograms
#kg = lb / 2.2046
kilograms = calc_kilograms(weight)
print("your weight in kg is: " + str(kilograms))

#compute BMI
# BMI = kilograms / meters squared
#Display answer to user
BMI = calc_bmi(kilograms, meters)
print("Your BMI is: " + str(BMI))

# If BMI < 18.5  print 'underweight'
if BMI < 18.5:
    print("underweight")
    red_led.on()
    sleep(5)

# if bmi >= 18.5 and < 25 print 'normal'
elif BMI >= 18.5 and  BMI < 25:
    print("normal")
    green_led.on()
    sleep(5)

# If bmi >= 25 and  bmi < 30 print 'overweight'
elif BMI >= 25 and  BMI < 30:
    print("overweight")
    yellow_led.on()
    sleep(5)

# If bmi >= 30 print 'obese'
elif BMI >= 30:
    print("obese")
    red_led.on()
    sleep(5)

def display_bmi_category()
