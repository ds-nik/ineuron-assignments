''' Questions
1.	Write a Python program to print "Hello Python"?
2.	Write a Python program to do arithmetical operations addition and division.?
3.	Write a Python program to find the area of a triangle?
4.	Write a Python program to swap two variables?
5.	Write a Python program to generate a random number?
'''
import logging
logging.basicConfig(filename="Programming_Assignment1.log", level=logging.DEBUG, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
class Programming_Assignment1():
    def q1(self):
        try:
            logging.info("Ans of Q1")
            logging.info("Hello Python")
        except Exception as e:
            logging.exception(e)

    def q2(self):
        logging.info("this function will perform arithmetic operation addition and division")
        try:
            a=input("enter the value of 1st numbers on which arithmetic operation needs to be performed")
            b=input("enter the value of 2nd numbers on which arithmetic operation needs to be performed")
            add = int(a)+int(b)
            div=int(a)/int(b)
            logging.info("the addition and division of the entered numbers is %s and %s respectively", add, div)
            return (add,div)
        except Exception as e:
            logging.exception(e)

    def q3(self):
        logging.info("this function will provide an area of a triangle")
        try:
            a,b = map(float, input("Enter the value (cm) of height and base of a triangle separated by comma:").split(","))
            area = (a*b)/2
            logging.info("Area of an triangle is %s cm^2", area)
            return(area)
        except Exception as e:
            logging.exception(e)

    def q4(self):
        logging.info("this function will swap two variables entered by the user")
        try:
            x, y = input("Enter the value of two variable x & y separated by comma").split(",")
            temp = x
            x = y
            y = temp
            logging.info("The value of variables x & y after swapping is: %s & %s", x,y)
            return (x,y)
        except Exception as e:
            logging.exception(e)

    def q5(self):
        logging.info("this function will generate a random number between any two given numbers")
        import random
        try:
            a,b = map(int, input("Enter the value of two numbers separated by comma between which you want to generate a random number").split(","))
            c = random.randint(a,b)
            logging.info("The random number generated is : %s",c)
            return(c)
        except Exception as e:
            logging.exception(e)

#kindly change the following into commands by removing # to get the output of the questions 1 to 5 in the assignment
#q = Programming_Assignment1()
#q.q1()
#q.q2()
#q.q3()
#q.q4()
#q.q5()







