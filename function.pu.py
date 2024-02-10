# def fizz_buzz():
#     a=input("Enter the number")
#     A=int(a)
#     if A%3==0 and A%5!=0:
#         print('fizz')
#     elif A%3!=0 and A%5==0:
#         print('buzz')
#     elif A%3==0 and A%2==0:
#         print('fizz buzz')
#
#
# fizz_buzz()

def fizz_buzz(A):

    if A%3==0 and A%5!=0:
        return 'fizz'
    elif A%3!=0 and A%5==0:
        return 'buzz'
    elif A%3==0 and A%2==0:
        return 'fizz buzz'


print(fizz_buzz(6))