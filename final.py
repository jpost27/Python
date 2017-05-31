import math
def main():
    print(" Author: Joshua Post")
    print(" Date: 4/28/2015")
    print(" This program will compute and display the result ")
    print(" which is based on your choice on the menu....... ")
    print()
    print()
    print(" *******************Menu Choice*******************")
    print()
    print(" 1- Convert Kilometers to Miles                   ")
    print(" 2- Convert Miles to Kilometers                   ")
    print(" 3- Convert Fahrenheit to Celcius                 ")
    print(" 4- Convert Celcius to Fahrenheit                 ")
    print(" 5- Convert Inches to Centimeters                 ")
    print(" 6- Convert Centimeters to Inches                 ")
    print(" 7- Convert Kilograms to Pounds                   ")
    print(" 8- Convert Pounds to Kilograms                   ")
    print(" 9- Calculate Compound Interest                   ")
    print(" 10- Calculate Roots                              ")
    print()
    print()
    print(" 0- To quit this program!                         ")
    print(" Please enter one of the menu choices displayed   ")
    print(" above and press enter key...                     ")
    print()
    print()
    print("Would you like to perform a calculation? ")
    print()
    selection = int(input(" Please enter 1 to continue or 0 to quit:" ))

    while selection!=0:
        print()
        print()
        choice = int(input("Please select item #(1-10) to calculate or 0 to quit: "))
        print()
        if choice == 1:
            print( "You've selected converting Kilometers to Miles ")
            K = float(input(" Enter total kilometers: "))
            print()
            if K<=0:
                print(" Please check your data and try again ")
                break
            else:
                totalmiles = ConvKilo_to_Mile(K)
            print()
            print(K, " Kilometers = ",totalmiles, " Miles")

        elif choice == 2:
            print(" You've selected to convert Miles to Kilometers ")
            Mile = float(input(" Enter total miles: "))
            print()
            if Mile<=0:
                print(" Please check your data and try again ")
                break
            else:
                totalkilometer = ConvMile_to_Kilo(Mile)
            print()
            print(Mile," Miles = ",totalkilometer," Kilometers")
            print()

        elif choice == 3:
            print(" You've selected to convert Fahrenheit to Celcius ")
            F = float(input(" Enter temperature in Farhenheit: "))
            print()
            C = ConvF_to_Celcius(F)
            print()
            print(F," degrees Fahrenheit = ",C," Degrees Celcius")
            print()
            
        elif choice == 4:
            print(" You've selected to convert Celcius to Fehrenheit ")
            C = float(input(" Enter temperature in Celcius "))
            print()
            F = ConvC_to_Fahrenheit(C)
            print()
            print(C," degrees Celcius = ",F," degrees Fahrenheit")
            print()

        elif choice == 5:
            print(" You've selected to convert Inches to Centimeters ")
            I = float(input(" Enter total Inches: "))
            print()
            if I<=0:
                print(" Please check your data and try again ")
                break
            else:
                C = ConvI_to_Centi(I)
            print()
            print(I," Inches = ",C," Centimeters")
            print()

        elif choice == 6:
            print(" You've selected to convert Centimeters to Inches ")
            C = float(input(" Enter total Centimeters: "))
            print()
            if C<=0:
                print(" Please check your data and try again ")
                break
            else:
                I = ConvC_to_Inch(C)
            print()
            print(C," Centimeters = ",I," Inches")
            print()

        elif choice == 7:
            print(" You've selected to convert Kilograms to Pounds ")
            K = float(input(" Enter total Kilograms: "))
            print()
            P = ConvK_to_Pound(K)
            print()
            print(K," Kilograms = ",P," Pounds")
            print()

        elif choice == 8:
            print(" You've selected to convert Pounds to Kilograms ")
            P = float(input(" Enter total Pounds: "))
            print()
            K = ConvP_to_Kilo(P)
            print()
            print(P," Pounds = ",K," Kilograms")
            print()

        elif choice == 9:
            print(" You've selected to calculate Compound Interest ")
            P = float(input("Enter initial amount: $"))
            r = float(input("Enter annual rate of intrest:"))
            t = float(input("Enter number of years:"))
            n = float(input("Enter number of times compounded per year:"))
            print()
            A = Calc_Comp_Int(P,r,t,n)
            print()
            print("The total amount is:", A)
            print()

        elif choice == 10:
            print(" You've selected to solve a quadratic equation ")
            a = float(input(" Enter A(x^2): "))
            b = float(input(" Enter B(x): "))
            c = float(input(" Enter C: "))
            print()
            x,y,discriminant = Calc_Roots(a,b,c)
            print()
            if((x!=None) and (y!=None)):
                print("Discriminant is: ",discriminant)
                print()
                print("There are two roots for this equation: ",x," and ",y)
            elif((x!=None) and (y==None)):
                print("Discriminant is: ",discriminant)
                print()
                print("The root for this equation is: ",x)
            else:
                print("Discriminant is: ",discriminant)
                print()
                print("There are no real roots, for this equation ")
            print()

        else:
            break
        print()
        print(" Program is terminated, good bye!")

def ConvKilo_to_Mile(kilom):
       miles = kilom * 0.62
       return miles
    
def ConvMile_to_Kilo(NumMile):
    kilometer = NumMile/0.62
    return kilometer

def ConvF_to_Celcius (F):
    C = (F-32) * (5/9)
    return C

def ConvC_to_Fahrenheit(C):
    F = (C) * (9/5) + 32
    return F

def ConvI_to_Centi(I):
    C = I * 2.54000
    return C

def ConvC_to_Inch(C):
    I = C * 0.39370
    return I

def ConvK_to_Pound(K):
    P = K * 2.20462
    return P

def ConvP_to_Kilo(P):
    K = P * 0.45359
    return K

def Calc_Comp_Int(P,r,t,n):
    A = P*math.pow(1+(r/n),(n*t))
    return A

def Calc_Roots(a,b,c):
    if (((b*b) - (4*a*c))>0):
        x=((-b+math.sqrt((b*b) - (4*a*c)))/(2*a))
        y=((-b-math.sqrt((b*b) - (4*a*c)))/(2*a))
    elif (((b*b) - (4*a*c))==0):
        x=((-b+math.sqrt((b*b) - (4*a*c)))/(2*a))
        y=None
    else:
        return (None,None,((b*b)-(4*a*c)))
    
    return (x,y,((b*b)-(4*a*c)))

