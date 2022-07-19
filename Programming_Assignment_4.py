'''Questions:
1. Write a Python Program to Find the Factorial of a Number?
2. Write a Python Program to Display the multiplication Table?
3. Write a Python Program to Print the Fibonacci sequence?
4. Write a Python Program to Check Armstrong Number?
5. Write a Python Program to Find Armstrong Number in an Interval?
6. Write a Python Program to Find the Sum of Natural Numbers?'''

import logging
logging.basicConfig(filename="Programming_Assignment_4.log", level=logging.DEBUG, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

class Programming_Assignment_4:
    #def __init__(self,cond):
     #   self.cond = cond
    def q1(self):
        logging.info("this function will give the factorial of a Number")
        try:
            n = int(input("Enter the integer of which factorial is required : "))
            l = list()
            # n! = n * (n-1) * (n-2) * -------- * 2 * 1
            for i in range(0,n):
                l.append(n-i)
            f = 1
            for i in l:
                f = f * i
            logging.info("factorial of %s is : %s ", n,f)
            return f
        except Exception as e:
            logging.exception(e)

    def q2(self):
        logging.info("this function will display the multiplication table matrix of the entered number")
        try:
            n = int(input("Enter an integer number"))
            for i in range(1,11):
                logging.info("%s x %s = %s", i, n, i*n)
        except Exception as e:
            logging.exception(e)

    def q3(self):
        logging.info("this function will print the list of elements of fibonacci sequence up to entered value 'n'")
        try:
            n = int(input("Enter the number of digits of fibonacci sequence desired"))
            l = [1, 1]

            for i in range(1,n-1):
                s = l[i] + l[i-1]
                l.append(s)
            logging.info("list of first %s digits of fibonacci sequence is %s", n, l)
        except Exception as e:
            logging.exception(e)

    def q4(self):
        logging.info("this function will check whether the entered number is armstrong number or not")
        try:
            n = int(input("Enter an integer number to know whether it is armstrong number or not: "))
            l = list(str(n))
            l1 = []
            r = len(l)
            for i in l:
                s = int(i)
                for j in range(r-1):
                    s = s * int(i)
                l1.append(s)
            add = sum(l1)
            if add == n:
                logging.info("Entered number %s is an Armstrong number", n)
            else:
                logging.info("Entered number %s is not an Armstrong number", n)
        except Exception as e:
            logging.exception(e)
    def check_armstrong_num(self, n):
        #logging.info("this function will check whether the entered number is armstrong number or not")
        try:
            #n = int(input("Enter an integer number to know whether it is armstrong number or not: "))
            l = list(str(n))
            l1 = []
            r = len(l)
            for i in l:
                s = int(i)
                for j in range(r-1):
                    s = s * int(i)
                l1.append(s)
            add = sum(l1)
            if add == n:
               # self.cond = True
                logging.info("%s is armstrong num",n)
                #return self.cond
            else:
                #self.cond = False
                #logging.info("%s is not armstrong num",n)
                pass
                #return self.cond
        except Exception as e:
            logging.exception(e)
    def q5(self):
        logging.info("this function will give list of armstrong numbers in an entered range")
        try:
            r1, r2 = map(int, input("Entered the range in r1-r2 format:").split("-"))
            l =[]
            for i in range(r1,r2+1):
                q = Programming_Assignment_4()
                q.check_armstrong_num(i)
                #Programming_Assignment_4().check_armstrong_num(i)

                #if self.cond == True:
                 #   l.append(i)
                #else:
                 #   pass
            #logging.info(l)
            #logging.info(list(range(r1,r2+1)))
        except Exception as e:
            logging.exception(e)

    def q6(self):
        logging.info("this function will give sum of 'n' natural numbers")
        try:
            n = int(input("Enter the value of 'n' to get the sum of 'n' natural numbers : "))
            s = 0
            for i in range(1,n+1):
                s = s + i
            logging.info("The sum of %s natural numbers is: %s", n, s)
            return s
        except Exception as e:
            logging.exception(e)

#Programming_Assignment_4().q1()
#Programming_Assignment_4().q2()
#Programming_Assignment_4().q3()
#Programming_Assignment_4().q4()
#Programming_Assignment_4().q5()
#Programming_Assignment_4().q6()


















