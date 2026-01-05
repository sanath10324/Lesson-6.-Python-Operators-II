character = str(input("Enter a character: "))

if len(character) == 1 and character.isalpha():
    print("The entered character is an alphabet.")
else:
    print("The entered character is not an alphabet.")