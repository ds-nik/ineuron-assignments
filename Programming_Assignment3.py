'''
1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?
2.	Write a Python Program to Check if a Number is Odd or Even?
3.	Write a Python Program to Check Leap Year?
4.	Write a Python Program to Check Prime Number?
5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
'''
import logging
logging.basicConfig(filename="Programming_Assignment3.log", level=logging.DEBUG, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

class Programming_Assignment3():
    def q1(self):
        logging.info("this function will check whether the entered number is positive, negative or zero")
        try:
            x = float(input("enter the number : "))
            if x == 0:
                logging.info("Entered number is Zero")
            elif x>0:
                logging.info("Entered number is Positive")
            elif x<0:
                logging.info("Entered number is Negative")
            else:
                logging.info("Please entered a valid number")
            return x
        except Exception as e:
            logging.exception(e)

    def q2(self):
        logging.info("this function will check whether the entered number is odd or even")
        try:
            x = int(input("Enter the integer number: "))
            if x%2 == 0:
                logging.info("Entered number is an Even number")
            else:
                logging.info("Entered number is an Odd number")
        except Exception as e:
            logging.exception(e)

    def q3(self):
        logging.info("This function will check whether the entered year is leap year or not")
        try:
            y = int(input("Enter the year in yyyy format: "))
            if y%100 == 0:
                if y%400 == 0:
                    logging.info("Entered year %s is a leap year", y)
                else:
                    logging.info("Entered year %s is not a leap year", y)
            else:
                if y%4==0:
                    logging.info("Entered year %s is a leap year", y)
                else:
                    logging.info("Entered year %s is not a leap year", y)
        except Exception as e:
            logging.exception(e)

    def q4(self):
        logging.info("This function will check whether the entered number is Prime number or not")
        #Prime number is a number which is divisible by 1 and itself only
        try:
            cond = True
            n = int(input("Enter an integer number: "))
            for i in range(2,(n//2)+1):
                if n%i==0:
                    cond = False
                    break
            if cond == True:
                logging.info("Entered number %s is a Prime number", n)
            if cond == False:
                logging.info("Entered number %s is not a Prime number", n)

        except Exception as e:
            logging.exception(e)

    def q4_alternate_program(self):
        logging.info("This function will check whether the entered number is Prime number or not")
        # Prime number is a number which is divisible by 1 and itself only
        try:
            n = int(input("Enter an integer number: "))
            for i in range(2, (n // 2) + 1):
                if n % i == 0:
                    logging.info("Entered number %s is not a Prime number", n)
                    break
            else:
                logging.info("Entered number %s is a Prime number", n)

        except Exception as e:
            logging.exception(e)

    def q5(self):
        logging.info("this function will give list of all the prime numbers from 1 - 10000")
        try:
            l1 = []
            cond = True
            for i in range(3,10001):
                for j in range(2,(i//2)+1):
                    if i%j == 0:
                        cond = False
                        break
                if cond == True:
                    l1.append(i)
                else:
                    cond = True
                    pass
            logging.info("the list of all the prime numbers from 1-10000 is: %s", l1)
            return l1
        except Exception as e:
            logging.exception(e)



#kindly change the following into commands by removing # to get the output of the questions 1 to 5 in the assignment
#q = Programming_Assignment3()
#q.q1()
#q.q2()
#q.q3()
#q.q4()
#q.q5()

