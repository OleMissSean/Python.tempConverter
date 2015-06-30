"""
Write two functions that will convert temperatures back and forth from the Celsius and Fahrenheit temperature scales. The formulas for making the conversion are as follows:

  Tc=(5/9)*(Tf-32)
  Tf=(9/5)*Tc+32

where Tc is the Celsius temperature and Tf is the Fahrenheit temperature. More information and further descriptions of how to do the conversion can be found at this NASA Webpage. If you finish this assignment quickly, add a function to calculate the wind chill.
Input

Your program should ask the user to input a temperature and then which conversion they would like to perform.
Sample session

Temperature converter

Enter a temperature: 20
Convert to (F)ahrenheit or (C)elsius? F

20 C = 68 F
"""

def cel(temp):
    answer = (5.0/9)*(temp-32.0)
    return answer

def far(temp):
    answer = (9.0/5)*temp+32.0
    return answer

def instructions():
    global temp
    global conv

    while True:
        try:
            temp = input("Please enter a temperature to convert: ")
            temp = int(temp)
            break
        except ValueError:
            print("No valid integer! Please try again ...")

    conv = input("Convert to (F)ahrenheit or (C)elsius? ")
    conv = conv.lower()
    work(temp, conv)

def work(temp, conv):
    if type(temp) is int and type(conv) is str:
        print (conv)
        if conv == 'f':
            print(str(far(temp)))
        elif conv == 'c':
            print(str(cel(temp)))
        else:
            print ("Oops!!  That was not a valid conversion type.  Please try again...")
            instructions()
    else:
        print("Please enter a valid temperature and conversion type.")
        instructions()
        
temp = 0
conv = ""
instructions()





