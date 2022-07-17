# 🚨 Don't change the code below 👇

print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")

name2 = input("What is their name? \n")

# 🚨 Don't change the code above 👆



#Write your code below this line 👇



lower1 = name1.lower() + name2.lower()



t1 = lower1.count('t')

r1 = lower1.count('r')

u1 = lower1.count('u')

e1 = lower1.count('e')

l1 = lower1.count('l')

o1 = lower1.count('o')

v1 = lower1.count('v')



total1 = t1 + r1 + u1 + e1 

total2 = l1 + o1 + v1 + e1



final_total = str(total1) + str(total2)

final_total = int(final_total)

if final_total > 89:

    print(f"Your score is {final_total}, you go together like coke and mentos.")

elif final_total > 39 and final_total < 51:

    print(f"Your score is {final_total}, you are alright together..")

else:    

    print(f"Your score is {final_total}.")