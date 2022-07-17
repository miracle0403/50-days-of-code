# 🚨 Don't change the code below 👇

year = int(input("Which year do you want to check? "))

# 🚨 Don't change the code above 👆



#Write your code below this line 👇

remain1 = year % 4

remain2 = year % 100

remain3 = year % 400



#if it is divisible by 4

if remain1 == 0:

    #check if it is divisible by 100

    if remain2 > 0: 

        #if it has remainder

        print("Leap year.") 

        #is a leap year

    else:

        #check if it is divisible by 400

        if remain3 == 0: 

        #divisible by 400

            print("Leap year.") 

            #is a leap year

        else: 

            print("Not leap year.")         

else:

    #it is not divisible by 4

    print("Not leap year.")    





