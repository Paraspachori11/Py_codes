#WAP to find out whether a given post is talking about "harry" or not

post = input("Enter the post \n")

lpost = post.lower()

if "harry" in lpost :
    verify = True
else :
    verify = False

if (verify):
    print("YES they are talking about harry")
else :
    print("NO they aren't talking about harry")