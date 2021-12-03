bilangan = int(input("Masukkan banyak bilangan : "))
total = 1

print("Total = ", end = "")

for i in range(1, bilangan+1):
    if(i%7==0):
        total = total + 0
        print("+ 0", end = " ")
    elif(i%3==0):
        total = total + (i * -1)
        print("- " + str(i), end = " ")
    elif(i==1):
        print(str(i), end = " ")
    else:
        total = total + i
        print("+ " + str(i), end = " ")

print ()
print("Hasil perhitungan diatas ialah " + str(total))