a = int(input("Enter any number between 5 and 9: "))

if (a < 5 or a > 9):
    raise ValueError("Value should be between 5 and 9")


a = (input("Enter any String: "))
if (a != "quiet"):
    raise ValueError("String should be quiet")
