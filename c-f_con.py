#WAP using fuction to convert celsius to farenheit

cel = int(input("Enter the temp in celsius"))
def farh(cel):
    return (cel*(9/5))+32

c = farh(cel)
print("temperature in farenheit"+str(c))