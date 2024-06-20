def converttemp(temp,unit):
    if unit=="celcius":
        cel=temp
        far=9/5*temp+32
        kel=temp+273
    elif unit=="fahrenheit":
        far=temp
        cel=((temp-32)*5/9)
        kel=(5/9*(temp-32))+273
    else:
        kel=temp
        cel=temp-273
        far=((temp-273)*9/5)+32
       
    return cel,far,kel

print("converting temperatures")
temperatures=float(input("enter the temperature:"))
unit=input("enter the unit in celcius,fahrenheit,kelvin:")


cel,far,kel=converttemp(temperatures,unit)
print(cel,"°C" )
print(far,"°F" )
print(kel,"K" )
