# Get input for the guy's name
guy = input("Who's the lucky guy? ")

# Loop until the girl's name is "Jas"
while True:
    girl = input("Who's the girl? ")
    if girl == "Jas":
        print(f"YES! {guy} loves {girl} so much!")
        break
    else:
        print("Nope!")
