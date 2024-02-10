# #input a array and find the sum of positive number?
# def summ(arr):
#     total=0
#     for i in arr:
#         if i>0:
#             total=total+i
#
#     return total
#
# a=[2,3,4,6,-4,-3]
# result=summ(a)
# print(result)
#
#

#2 Palindrome or not
# def palindrome():
#     a=input('Enter the string')
#     A=a[::-1]
#     if a==A:
#         print('palindrome')
#     else:
#         print('no')
#
#
# palindrome()

#3 palindrome when the two string is passed in argument.
# def palindrome(x,y):
#     x=x.replace(" ","").lower()
#     y=y.replace(" ","").lower()
#     if x==y:
#         return 'palindrome'
#     else:
#         return 'no'
#
#
# print(palindrome('dad','D a d'))


#4 palindrome simple without using function
# a='Mom'
# b='m o m'
# a=a.replace(" ","").lower()
# b=b.replace(" ","").lower()
# if a==b:
#     print('palindrome')
# else:
#     print('none')

#5 palindrome usind input
# a=input('Enter the string')
# a=a.replace(" ","").lower()
# if a==a[::-1]:
#     print("palindrome")
# else:
#     print("not")


#5 file handling
# with open('data.txt','r') as f:
#     b=0
#     for i in f:
#         b+=1
#         a=i.split(" ")
#         print(f"the number of word in  line {b} is {len(a)}")

