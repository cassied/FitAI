### BMI and calorie calculator

def main ():
    a = input (print ("enter 1 to the BMI calculator, or enter 2 to the calorie calculator"))
    if a == "1":
        BMIcalc ()
    elif a == "2":
        caloriecalc ()
    else:
        print ("please enter 1 or 2")
        main ()

def BMIcalc ():
    height = eval (input (print ("please enter your height: (m)")))
    weight = eval (input (print ("please enter your weight: (kg)")))
    BMI = weight / (height ** 2)
    print ("your BMI is: ", BMI)
    if BMI <= 16:
        print ("you need to eat more and get more nutrition, you are too thin")
    elif 16 < BMI <= 18.5:
        print ("your weight is a little bit light, the best way for you is to eat more")
    elif 18.5 < BMI <= 25:
        print ("great, you are in the right way, keep going on")
    elif 25 < BMI <= 30:
        print ("oops, you are just a little bit heavy. However, stand in front of the mirror to watch yourself, if you are not fat, you must have some muscles")
    elif 30 < BMI <= 35:
        print ("hmmm... Compare with other people, you are heavy. However, stand in front of the mirror to watch yourself, if you are not fat, you must have some muscles")
    elif 35 < BMI <= 40:
        print ("Hey, do something, you need to keep fit. However, stand in front of the mirror to watch yourself, if you are not fat, you must have some muscles")
    elif 40 < BMI:
        print (" Wow, your BMI is very hight, please try to keep fit. However, if you are a body builder, just ignore it")
    x = input ("press enter to quit")

def caloriecalc ():
    height = eval (input (print ("please enter your height: (cm)")))
    weight = eval (input (print ("please enter your weight: (kg)")))
    age = eval (input (print ("please enter your age: (years)")))
    gender = input (print ("please enter your gender: (male/female)"))
    if gender == "male":
        BMR = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "female":
        BMR = 10 * weight + 6.25 * height - 5 * age - 161
    print ("you should get ", BMR, "Calories per day. If you get ", BMR + 500, "Calories per day, you can gain 1lb per week. If you get", BMR - 500, "Calories per day, you can lose 1lb per week")
    x = input ("press enter to quit")
    
main ()
