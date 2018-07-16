# Welcome to JAYY BMI Calculator calculator

print ("Welcome to JAYS BMI Calculator")
print ()

# Get height from user, 
# Code for get  inches initially.Then later, change to ft/in.
# Then convert back to inches
# Get height from user
height = int(input("Please enter your height in inches; "))
##print (height)

# Convert from inches to meters
# inches * 0.0254
meters = height * .0254
print ("your height in meters is; " + str(meters))

# Convert from meters to centimeters
# multiply meters X 100
centimeters = meters * 100
print ("your height in centimeters is; " + str(centimeters))


# Get weight from user
weight = int(input("Please enter your weight in pounds; "))
##print (weight)
print ()

#convert from pounds to kilograms 
#kg = lb / 2.2046
kilograms = weight / 2.2046
print("your weight in kg is; " + str(kilograms))

#compute BMI
# BMI = kilograms / meters squared
#Display answer to user
bmi = kilograms / meters**2
print ("Your BMI is: " + str(bmi))

# If BMI < 18.5  print 'underweight' 
if bmi  < 18.5:
    print ("underweight")

# if bmi >= 18.5 and < 25 print 'normal' 
if bmi >= 18.5 and  bmi < 25:
    print ("normal")    

# If bmi >= 25 and  bmi < 30 print 'overweight'
if bmi >= 25 and  bmi < 30: 
    print ("overweight")

# If bmi >= 30 print 'obese'
if bmi >=  30:
    print ("obese")
