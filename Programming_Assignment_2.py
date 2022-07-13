''' Questions:
1.	Write a Python program to convert kilometers to miles?
2.	Write a Python program to convert Celsius to Fahrenheit?
3.	Write a Python program to display calendar?
4.	Write a Python program to solve quadratic equation?
5.	Write a Python program to swap two variables without temp variable?
'''
import logging
logging.basicConfig(filename="Programming_Assignment2.log", level=logging.DEBUG, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

class Programming_Assignment_2():

    def q1(self):
        logging.info("this function will convert the entered value in KM to miles")
        try:
            a = float(input("enter the value in KM"))
            b = a * 0.621371192
            logging.info("The entered value %s KM is equal to %s Miles", a,b)
            return b
        except Exception as e:
            logging.exception(e)

    def q2(self):
        logging.info("this function will convert the entered value of temperature in celsius to fahrenheit")
        try:
            a = float(input("enter the value of temperature in celsius"))
            b = a * 1.8 + 32
            logging.info("The entered value of temperature in %s degree celsius is equal to %s degree fahrenheit", a,b)
            return b
        except Exception as e:
            logging.exception(e)

    def q3(self):
        logging.info("this function will display a calendar for the month and year entered by the user")
        try:
            import calendar
            m,y = map(int, input("Enter the month and year in mm/yyyy format to display the calendar").split("/"))
            logging.info(calendar.month(y,m))
        except Exception as e:
            logging.exception(e)

    def q4(self):
        logging.info("this function will solve the quadratic equation aX^2+bX+c=0 based on given inputs a,b,c")
        import cmath
        try:
            a,b,c = map(float, input("Enter the value of a,b,c for quadratic equation aX^2+bX+c=0 to be solved").split(","))
            if a != 0:
                d = b*b - 4*a*c
                sqrt_d = cmath.sqrt(d)
                if d < 0:
                    s1 = (-b+sqrt_d)/(2*a)
                    s2 = (-b-sqrt_d)/(2*a)
                    logging.info("the roots of the quadratic equation are imaginary and the value of roots are: %s and %s", s1, s2)
                if d == 0:
                    s1 = -b/(2*a)
                    s2 = -b/(2*a)
                    logging.info("the roots of the quadratic equation are equal and the value of roots are: %s and %s", s1, s2)
                if d>0:
                    s1 = (-b + sqrt_d) / (2 * a)
                    s2 = (-b - sqrt_d) / (2 * a)
                    logging.info("the roots of the quadratic equation are imaginary and the value of roots are: %s and %s", s1, s2)
                return s1,s2
            else:
                logging.info("enter the non-zero value of 'a' for equation to be a valid quadratic equation")
        except Exception as e:
            logging.exception(e)

    def q5(self):
        logging.info("this function will swap the value of variables")
        try:
            x,y = input("Enter the value two variable x & y separated by comma").split(",")
            x,y = y,x
            logging.info("Value of x & y after swapping is %s & %s", x,y)
            return x,y
        except Exception as e:
            logging.exception(e)

#kindly change the following into commands by removing # to get the output of the questions 1 to 5 in the assignment
#q = Programming_Assignment_2()
#q.q1()
#q.q2()
#q.q3()
#q.q4()
#q.q5()




