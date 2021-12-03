
inputan = int(input("Input : "))
print("Output : ")

for i in range(inputan):
    for j in range(inputan-i-1):
        print(" ", end="   ")
    for j in range(inputan):
        if j == 0 or i == (inputan-1) or i == j:
            print("*", end="   ")
        else:
            print(end="    ")
    print()
