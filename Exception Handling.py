# try:
#     a = int(input("Enter the Number:"))
#     print(f"Multiplication Table of {a} is :")
#     for i in range(1, 11):
#        print(f"{a} X {i} = {a*i}")

# except:
#     print("Invald Input !")

# print("Some imp lines of code")
# print("End of program")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3, 1, 7]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error.")
