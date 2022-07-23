''' Questions:
1.	Write a Python Program to Find LCM?
2.	Write a Python Program to Find HCF?
3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
4.	Write a Python Program To Find ASCII value of a character?
5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
'''

import logging
logging.basicConfig(filename="Programming_Assignment5.log", level=logging.DEBUG, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

def q1(n1, n2):
    logging.info("This function will provide LCM of two numbers")
    try:
        if n1>n2:
            i = n1
            while i%n1 != 0 or i%n2 != 0:
                i = i+1
            logging.info("LCM of %s & %s is : %s", n1, n2, i)
            return i
        else:
            i = n2
            while i % n1 != 0 or i % n2 != 0:
                i = i + 1
        logging.info("LCM of %s & %s is : %s", n1, n2, i)
        return i
    except Exception as e:
        logging.exception(e)

def q2(n1, n2):
    logging.info("This function will provide HCF of two numbers")
    try:
        if n1<n2:
            i = n1
            while n1%i != 0 or n2%i != 0:
                i = i-1
            logging.info("HCF of %s & %s is : %s", n1, n2 , i)
            return i
        else:
            i = n2
            while n1%i != 0 or n2%i != 0:
                i = i-1
            logging.info("HCF of %s & %s is : %s", n1, n2 , i)
            return i
    except Exception as e:
        logging.exception(e)

def q3(n1):
    logging.info("This function will convert entered Decimal number into Binary, Octal & Hexadecimal number system")
    try:
        s1 = ""
        s2 = ""
        s3 = ""
        qnt, rmd = n1,0
        while qnt >= 1:
            #rmd = int(rmd)
            rmd = qnt%2
            qnt = qnt//2
            #print(qnt)
            #print(str(rmd))
            rmd = str(rmd)
            s1 += rmd
        #logging.info("Binary of %s is : %s", n1, s1[::-1])
        #return s1

        qnt, rmd = n1, 0
        while qnt >= 1:
            rmd = qnt % 8
            qnt = qnt // 8
            rmd = str(rmd)
            s2 += rmd
        #return s2

        qnt, rmd = n1, 0
        l = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
        while qnt >= 1:
            rmd = qnt % 16
            qnt = qnt // 16
            rmd = str(l[rmd])
            s3 += rmd
        #return s3

        logging.info("Binary, Octal & Hexadecimal number of decimal no. %s is %s, %s & %s respectively", n1, s1[::-1], s2[::-1], s3[::-1])
        #logging.info(type(s1))
        #logging.info(type(s2))
        #logging.info(type(s3))

    except Exception as e:
        logging.exception(e)


#q1(10,100)
#q2(5,51)
#q3(1001)

def q4():
    logging.info("This function will give the ASCII value of the entered character")
    try:
        c = str(input("Enter a character to know its ASCII value : "))
        ASCII = ord(c)
        logging.info("ASCII value of character '%s' is : %s", c, ASCII)
    except Exception as e:
        logging.exception(e)

#q4()

def q5():
    logging.info("This function is a simple calculator for doing 4 simple mathematical operations")
    try:
        a, b, c = map(str, input("Enter required operation with proper spacing after each character in n1 + n2, n1 - n2, n1 * n2 or n1 / n2 format").split())
        if ord(b) == 43:
            logging.info("%s + %s = %s", a,c, float(a)+float(c))
        elif ord(b) == 45:
            logging.info("%s - %s = %s", a, c, float(a) - float(c))
        elif ord(b) == 42:
            logging.info("%s x %s = %s", a,c, float(a)*float(c))
        elif ord(b) == 47:
            logging.info("%s / %s = %s", a,c, float(a)/float(c))
    except Exception as e:
        logging.exception(e)
#q5()

# Remove # and enter values to get answers of q1 to q5
#q1(10,100)
#q2(5,51)
#q3(1001)
#q4()
#q5()





