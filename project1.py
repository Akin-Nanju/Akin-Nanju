#Taking marks as input from user
a=input('Enter the marks of DSA: ')
A=int(a)      #Coverting the inputted string as integer bcuz everything taken input in python is considered as string
b=input('Enter the marks of WEB: ')
B=int(b)
c=input('Enter the marks of STAT: ')
C=int(c)
d=input('Enter the marks of JAVA: ')
D=int(d)
e=input('Enter the marks of System Analysis: ')
E=int(e)
if A>30 and B>30 and C>30 and D>30 and E>30:     #Checking the condition for being passed in exam using for loop and and operator
    print('CONGRATULATION YOU HAVE PASSED YOUR EXAM')
else:
        print('SORRY TO SAY BUT YOU HAVE FAILED')

ans=input("DO YOU WANT US TO CALCULATE YOUR PERCENTAGE(yes/no): ")    #Asking the user if they want to calculate their percenatage or not in yes/no format
if ans.lower()== 'yes':      #If user input yes this loop will execute
    sum=A+B+C+D+E        #Calculating sum of total marks obtsioned by user
    print(f"YOUR TOTAL MARKS IN 5 subject is {sum}")
    per=(sum/500)*100
    print(f"YOUR TOTAL PERCENTAGE IS {per}")
elif ans.lower()== 'no':    #If user input no this loop will execute
    print("OK. CONGRATULATION ON PASSING")
else:        #If user input something else this loop will execute
    print("YOU HAVE INPUT WRONG VALUE. PLEASE CHECK")


