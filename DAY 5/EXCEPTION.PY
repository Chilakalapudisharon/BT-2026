try:
    a = int(input("Enter First value"))#20
    b= int(input("Enter Secound value"))#12
    print(10/0)
    print("I am try just started")
    if b%2 == 0:
        raise Exception
    else:
        print(a/b)
    print("I am try, I am done")  
except ZeroDivisionError as zd:
    print(zd)
except Exception as e:
    print("Division by evens are not allowed")     
else:
    print("Hi I am else now alive because try is executed.")
finally:
    print("Hello there I am finally,I am going to close")            