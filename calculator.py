



while (1):
    a = (input("Enter a number: "))


    op = raw_input("specify operation: ")


    b = (input("Enter a number: "))



    while 1:
        if(op == "+"):
            c = a+b
            print "Addition result is: %d"%c
            c=0
            break
        elif(op == "-"):
            c = a-b
            print "Subtraction result is: %d"%c
            c=0
            break
        elif (op == "*"):
            c=a*b
            print "Multiplication result is: %d"%c
            c=0
            break
        elif (op == "/"):
            c= a/float(b)
            print "Division result is: %f"%c
            c=0
            break
        elif (op == "^"):
            c = a ** b
            print "Exponential is: %d" % c
            c = 0
            break
        else:
            print "Sorry! wrong input, Try again"
            break


