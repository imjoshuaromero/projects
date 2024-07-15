import pyperclip
ily = int(input("How many ILY for her? "))

output = ""
for i in range(ily):
    output += "I love JOSH!\n"

print(output)

pyperclip.copy(output)
print("The output has been copied.")