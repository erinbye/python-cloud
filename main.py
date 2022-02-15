print("1: F -> C")
print("2: C -> F")
option = input("Choose a number: ")

if option == "1":
    fahr = input("Temp in fahrenheit: ")
    cel = (int(fahr) - 32) / 1.8
    print("Temp in celsius: " + str(cel))
elif option == "2":
    cel = input("Temp in celsius: ")
    fahr = (int(cel) * 1.8) + 32
    print("Temp in fahrenheit: " + str(fahr))
else:
    print("Invalid option")