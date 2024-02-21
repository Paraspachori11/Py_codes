#write a python function which converts inches to cms
inch = int(input("enter length in inches\n"))

def convert(inch):
    cms = inch * (2.54)
    return cms

z = convert(inch)
print(str(z)+" cms")