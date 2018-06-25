from time import sleep
from gpiozero import LED
# bred = 17 yellow =27 green =22
RED_LED      = LED(17) # under weight and obese
YELLOW_LED   = LED(27) # overweight
GREEN_LED    = LED(22) # normal weight
# Welcome to JAYY BMI Calculator calculator
print("Welcome to JAYS BMI Calculator")
print()

# Get height from user,
# Code for get  inches initially.Then later, change to ft/in.
# Then convert back to inches
# Get height from user
HEIGHT = int(input("Please enter your height in inches: "))
##print(height)

# Convert from inches to meters
# inches * 0.0254
METERS = HEIGHT * .0254
print("your height in meters is: " + str(METERS))

# Convert from meters to centimeters
# multiply meters X 100
CENTIMETERS = METERS * 100
print("your height in centimeters is: " + str(CENTIMETERS))


# Get weight from user
WEIGHT = int(input("Please enter your weight in pounds: "))
##print (WEIGHT)
print()

#convert from pounds to kilograms 
#kg = lb / 2.2046
KILOGRAMS = WEIGHT / 2.2046
print("your weight in kg is: " + str(KILOGRAMS))

#compute BMI
# BMI = kilograms / meters squared
#Display answer to user
BMI = KILOGRAMS / METERS**2
print("Your BMI is: " + str(BMI))

# If BMI < 18.5  print 'underweight' 
if BMI  <18.5:
    print("underweight")
    RED_LED.on()
    sleep(5)

# if bmi >= 18.5 and < 25 print 'normal' 
elif BMI >=18.5 and  BMI< 25:
    print("normal")    
    GREEN_LED.on()
    sleep(5)

# If bmi >= 25 and  bmi < 30 print 'overweight'
elif BMI >=25 and  BMI <30: 
    print("overweight")
    YELLOW_LED.on()
    sleep(5)

# If bmi >= 30 print 'obese'
elif BMI >=30:
    print("obese")
    RED_LED.on()
    sleep(5)
