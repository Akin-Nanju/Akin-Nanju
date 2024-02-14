#THIS IS KIND OF UPDATED VERSION OF PROJECT 1
n1=input("Enter your name Student 1: ")   #TAKING NAME AS INPUT FROM USER
n2=input("Enter your name Student 2: ")
n3=input("Enter your name Student 3: ")
n4=input("Enter your name Student 4: ")
n5=input("Enter your name Student 5: ")

#OPENING THE FILE MARKS.TXT IN WRITE MODE AND WRITING THE MARKS OF STUDENT
with open('marks.txt','w') as f:
    f.write("40,45,40,50,65\n"
            "33,45,67,60,70\n"
            "45,60,23,56,77\n"
            "50,69,79,34,22\n"
            "34,56,79,56,20\n")

#AGAIN OPENING THE FILE MARKS. TXT AS READ MODE
with open('marks.txt','r') as a:
#READING THE LINE AND INITIALIZING IT
    r1=a.readline().strip().split(",")
    r2=a.readline().strip().split(",")
    r3 = a.readline().strip().split(",")
    r4 = a.readline().strip().split(",")
    r5 = a.readline().strip().split(",")

#INITIATING TOTAL MARKS FOR 5 STUDENTS AS 0
    total_marks1 = 0
    total_marks2 = 0
    total_marks3 = 0
    total_marks4 = 0
    total_marks5 = 0
    print("Marks and Total of Student 1 is :")

#READING THE VALUE OF ROW 1
    for b in r1:
        m1=int(b)
 #CALCULATING TOTAL MARKS
        total_marks1+=m1
        print(m1, end=",")
    print(" ")
    print(f"The total marks of student {n1} is {total_marks1}")
    print(" ")
    print("Marks and Total of Student 2 is :")

#READING THE VALUE IN ROW 2
    for b in r2:
        m2=int(b)
        total_marks2+=m2
        print(m2, end=",")
    print(" ")
    print(f"The total marks of student {n2} is {total_marks2}")
    print(" ")
    print("Marks and totala of student 3 is :")

# READING THE VALUE IN ROW 3
    for b in r3:
        m3=int(b)
        total_marks3+=m3
        print(m3, end=",")
    print(" ")
    print(f"The total marks of Student {n3} is {total_marks3}")
    print(" ")
    print("Marks and totala of student 4 is :")

# READING THE VALUE IN ROW 4
    for b in r4:
        m4 = int(b)
        total_marks4 += m4
        print(m4, end=",")
    print(" ")
    print(f"The total marks of Student {n4} is {total_marks4}")
    print(" ")
    print("Marks and total of student 5 is :")

# READING THE VALUE IN ROW 5
    for b in r5:
        m5 = int(b)
        total_marks5 += m5
        print(m5, end=",")
    print(" ")
    print(f"The total marks of Student {n5} is {total_marks5}")
    print(" ")

#SEPARATING CASES FOR EACH STUDENT
    print(f"For {n1}")
#USING FUNCTION FOR FUTHER CALCULATION
    def case1():
#ASKING USER IF THEY WANT TO CALCULATE PERCENTAGE OR NOT
        ans=input("Do you want us to calculate your percntage(yes/no): ")
        ans=ans.lower()
#CHECKING THE USERS ANS
        if ans=='yes':
#WILL EXECUTE IF USER INOUT YES
          verify=input("Enter your name: ")
          if verify==n1:
             per=(total_marks1/500)*100
             print(f"{n1} your per is {per}")
          elif verify != n1:
            print("UNKNOWN NAME")
#WILL EXECUTE IF USER INPUT NI
        elif ans=='no':
            print("ok")
        print(" ")
#CALLING THE FUNCTION
    case1()
    print(f"for {n2}")
    def case2():
        ans = input("Do you want us to calculate your percntage(yes/no): ")
        ans = ans.lower()
        if ans == 'yes':
            verify = input("Enter your name: ")
            if verify==n2:
                per=(total_marks2/500)*100
                print(f"{n2} your per is {per}")
            elif verify!=n2:
                print("UNKNOWN NAME")
        elif ans=='no':
                print("ok")
        print(" ")


    case2()


    print(f"for {n3}")
    def case3():
        ans = input("Do you want us to calculate your percntage(yes/no): ")
        ans = ans.lower()
        if ans == 'yes':
            verify = input("Enter your name: ")
            if verify == n3:
                per = (total_marks3 / 500) * 100
                print(f"{n3} your per is {per}")
            elif verify!=n3:
                print("UNKNOWN NAME")
        elif ans == 'no':
                print("ok")
        print(" ")


    case3()


    print(f"for {n4}")
    def case4():
        ans = input("Do you want us to calculate your percntage(yes/no): ")
        ans = ans.lower()
        if ans == 'yes':
            verify = input("Enter your name: ")
            if verify == n4:
                per = (total_marks4 / 500) * 100
                print(f"{n4} your per is {per}")
            elif verify!=n4:
                print("UNKNOWN NAME")
        elif ans == 'no':
                print("ok")
        print(" ")


    case4()


    print(f"for {n5}")
    def case5():
        ans = input("Do you want us to calculate your percntage(yes/no): ")
        ans = ans.lower()
        if ans == 'yes':
            verify = input("Enter your name: ")
            if verify == n5:
                per = (total_marks5/ 500) * 100
                print(f"{n5} your per is {per}")
            elif verify!=n5:
                print("UNKNOWN NAME")
        elif ans == 'no':
                print("ok")
        print(" ")
    case5()



















