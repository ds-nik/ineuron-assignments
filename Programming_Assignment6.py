''' Questions:
1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
2.	Write a Python Program to Find Factorial of Number Using Recursion?
3.	Write a Python Program to calculate your Body Mass Index?
4.	Write a Python Program to calculate the natural logarithm of any number?
5.	Write a Python Program for cube sum of first n natural numbers?
'''

# Remove # before commands mentioned after each function to get the desired answers of respective code q1 to q5
import logging
logging.basicConfig(filename="Programming_Assignment6.log", level=logging.DEBUG, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

class Programming_Assignment6():
    def q1(self):
        logging.info("this function will display fibonacci sequence using recursion programming method")
        try:
            n = int(input("Enter the value of 'n' to get the first n terms of fibonacci sequence : "))
            def fibo_recurs(n):
                if n <=1:
                    return(n)
                else:
                    return (fibo_recurs(n-1) + fibo_recurs(n-2))
            if n<=0:
                logging.info("Please enter a positive integer")
            else:
                for i in range(n):
                    logging.info("The %s terms of fibonacci sequence are %s", n, fibo_recurs(i))
        except Exception as e:
            logging.exception(e)

#Programming_Assignment6().q1()

    def q2(self):
        logging.info("This function will give factorial of a number")
        try:
            n = int(input("Enter the number of which factorial is required"))
            def fact_recurs(n):
                if n ==1:
                    return n
                else:
                    return n*fact_recurs(n-1)
            if n < 0:
                logging.info("factorial of negative integers does not exists")
            elif n == 0:
                logging.info("Factorial of 0 is 1")
                return 1
            else:
                logging.info("Factorial of %s is %s", n, fact_recurs(n))
                return fact_recurs(n)
        except Exception as e:
            logging.exception(e)

#Programming_Assignment6().q2()

    def q3(self):
        logging.info("This function will give Body Mass Index for entered value of Weight and Height")
        try:
            w, h = map(float, input("Enter the value of weight in KG and height in cm separated by comma : ").split(","))
            h1 = h/100
            BMI = (w)/(h1*h1)
            logging.info("The BMI for weight %s KG and Height %s cm is %s KG/m^2",w,h,BMI)
            return BMI
        except Exception as e:
            logging.exception(e)

#Programming_Assignment6().q3()

    def q4(self):
        logging.info("This function will give logarithm of entered number")
        try:
            import math
            n = float(input("Enter the number 'n' to get log(n) : "))
            log = math.log(n)
            log1 = math.log(n,10)
            logging.info("The natural logarithm and standard logarithm of %s is %s and %s respectively", n,log,log1)
            return log,log1
        except Exception as e:
            logging.exception(e)

#Programming_Assignment6().q4()

    def q5(self):
        logging.info("This function will give cube sum of first n natural numbers")
        try:
            n = int(input("Enter an integer value of 'n' to get the cube sum of first n natural numbers"))
            s1 = n*(n+1)/2
            s2 = s1*s1
            logging.info("The cube sum of first %s natural numbers is %s", n,s2)
            return s2
        except Exception as e:
            logging.exception(e)

#Programming_Assignment6().q5()

