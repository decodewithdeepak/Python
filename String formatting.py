val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
name = 'Deepak'
age = 20
print(f"Hello! My name is {name} and I'm {age} years old.")


letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Deepak"
print(letter.format(country, name))  # traditional way

print(f"Hey my name is {name} and I am from {country}")  # modern way
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)


print(f"{2 * 30}")
print(type(f"{2 * 30}"))