print("Welcome to the Simple Temprature Converter!")
print("Units Available:(C(celsius), F(Farenheit), K(Kelvin))")

while True:

    temp=float(input("Enter the temperature: "))
    convert_from = str(input("Enter the unit to covert from (C, F, or K):")).upper()
    convert_to = str(input("Enter the unit to covert to (C, F, or K):")).upper()

    if convert_from == "C":
        if convert_to == "F":
            temp1=(temp*9/5)+32
            print(temp1,"°F")
        elif convert_to == "C":
            tempc=temp
            print(tempc,"°C")
        else:
            temp2=temp+273.15
            print(temp2,"°K")


    elif convert_from == "F":
        if convert_to == "C":
            temp3=(temp-32)*(5/9)
            print(temp3,"°C")
        elif convert_to == "K":
            temp4=((temp-32)*(5/9))+273.15
            print(temp4,"°K")
        else:
            temp5=temp
            print(temp5,"°F")


    elif convert_from == "K":
        if convert_to == "C":
            temp6=temp-273.15
            print(temp6,"°C")
        elif convert_to == "F":
            temp7=((temp-273.15)*(9/5))+32
            print(temp7,"°F")
        else:
            temp8=temp
            print(temp8,"°K")

    else:
        print("😵‍💫check whether the input must contains only symbol is(K,C,&F) used. \n")
        print("❗Invalid measurement parameter used...")

    again = input("\nDo you want to convert again? (yes/no): ").lower()
    if again == "no":
        print("thanks for using our system!")
        break