# age = int(input("How are old are you?"))
# if age >=18:
#     print("You are old enough to move out")
#     print("You are old enough to have ID")
# else:
#     print("You are young to move out")
#     print("You are not valid for an ID")
# Body_temp = float(input('What is your body temperature?'))
# if Body_temp >=30:
#     print('You are advised to have a vest on')
# elif Body_temp >=20 and Body_temp <=29 :
#     print("You are advised to put on a sweater")
# elif Body_temp <20:
#     print("You are advised to put on a jacket")
# else:
#     print('Fill in a valid body tenperature')
Height = float(input('What is your height?'))
Weight = float(input("What is your weight?"))
BMI = Weight/(Height*Height)
print(BMI)
if BMI <18:
    print('You are underweight')
elif BMI >=18 and BMI <=25:
    print("You are normal")
elif BMI >25 and BMI <=30:
    print("You are overweight")
elif BMI>30:
    print("You are obese")
else:
    print('Fill in correct values')
