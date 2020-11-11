print("Hello, this program will convert kilometers to miles")


while True:
    Km = int(input("Please enter number of kilometers: "))
    Miles = (Km * 1.6)
    print (str(Km) + " kilometers is " + str(Miles) + " miles")
    additional= input("Would you like another query (Yes/No): ")
    if additional!="Yes":
        break
#Comments