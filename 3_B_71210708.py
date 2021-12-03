
print()
inp = input("Input : ")
print("Output : ")

kata = ""
count = len(inp)-1

for i in inp:
    kata += i
    print((" "*count)+kata)
    count -= 1

count = 1
for i in range(len(inp)-1, 0, -1):
    print((" "*count)+inp[:i])
    count += 1

print()
