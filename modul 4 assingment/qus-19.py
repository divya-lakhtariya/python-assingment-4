'''
Que-19:How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding  snippets.
ans :- Try : This block will test the excepted error to occur
    Except :  Here you can handle the error
    Finally : Finally block always gets executed either exception is generated or not.

        example:-
'''
def divide(x,y):
    try:
        result=x/y
    except zerodivisionerror:
        print("diving by zero")
    else:
        print("ans :",result)
    finally :
        print('execut')

divide(3,2)
divide(3,0)

