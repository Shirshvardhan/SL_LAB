def fartocel():
    temp = int(input("ENTER THE FARENHEIT TEMPERATURE:\t"))
    ans = ((temp-32)*5)/9
    conv.append((temp,ans))
    print(ans)
def fartokel():
    temp = int(input("ENTER THE FARENHEIT TEMPERATURE:\t"))
    ans = ((temp-32)*5)/9+273
    conv.append((temp,ans))
    print(ans)
def celtofar():
    temp = int(input("ENTER THE CELSIUS TEMPERATURE:\t"))
    ans = ((temp*9)/5)+32
    conv.append((temp,ans))
    print(ans)
def celtokel():
    temp = int(input("ENTER THE CELSIUS TEMPERATURE:\t"))
    ans = temp + 273
    conv.append((temp,ans))
    print(ans)
def keltofar():
    temp = int(input("ENTER THE KELVIN TEMPERATURE:\t"))
    ans = ((temp-273)*9/5)+32
    conv.append((temp,ans))
    print(ans)
def keltocel():
    temp = int(input("ENTER THE KELVIN TEMPERATURE:\t"))
    ans = temp-273
    conv.append((temp,ans))
    print(ans)
c = "y"
tup = (
    (1,"FARENHEIT","CELSIUS"),
    (2,"FARENHEIT","KELVIN"),
    (3,"CELSIUS","FARENHEIT"),
    (4,"CELSIUS","KELVIN"),
    (5,"KELVIN","FARENHEIT"),
    (6,"KELVIN","CELSIUS"),
    (7,"SHOW TUPLE"),
    )
conv = []
while True:
    print(tup)
    ch = int(input("ENTER YOUR CHOICE:\t"))
    if(ch==1):
        fartocel()
    elif(ch==2):
        fartokel()
    elif(ch==3):
        celtofar()
    elif(ch==4):
        celtokel()
    elif(ch==5):
        keltofar()
    elif(ch==6):
        keltocel()
    elif(ch==7):
        print(conv)
    else:
        print("WRONG CHOICE")

    c = input("Continue? (y/n)")
    if(c == "n"):
        break


    
    