import re
import math;
import random;

# This is my first comment
print("Hi, this is my firts python code")
print('This is the same but with single quote')


# This is a value assignment
x = 10

# ------------------------------------------------------------------------------
# Python Course #4 - Comments
# ------------------------------------------------------------------------------
print('Nicolas.Mertes@gmx.de')
print("Hello \"Python\"")
print("Path C:\\Users\\Nicolas")

# Use triple quotes ("""") for comments spanning multiple lines
print("""Your learning path"
\t-First step"
\t-Second step
""")

print("The value of X is", x)

# ------------------------------------------------------------------------------
# Python Course #5 - Variables
# ------------------------------------------------------------------------------
x = 1
print(x)

y = 2
print(2)

print("x + y = ", x + y)

name = "Nico"
language = "Python"
print("My name is", name)
print(name, "wants to become a", language, "expert")

# ------------------------------------------------------------------------------
# Python Course #6 - Input
# ------------------------------------------------------------------------------
# name = input("Enter your name: ")
print("Your name is", name)
country = "Germany"
print(name, "comes from", country)

# ------------------------------------------------------------------------------
# Python Course #7 - Data Types
# ------------------------------------------------------------------------------
name = "Nicolas"
print("My name is", name.upper())

# Data Types
a = 10  # integer
b = 3.15  # float
c = "Hello"  # string
d = 'Hello'
e = "1234"
f = True
g = False
h = None
i = ""  # string (blank)
j = " "  # string (empty space)

with open("out.txt", "w") as file:
    print("Hello World", file=file)

print(type(f))

# ------------------------------------------------------------------------------
# Python Course #8 - Data Types - String
# ------------------------------------------------------------------------------

# Functions type() and str()
name = "Nicolas"
print(type(name))

age = 24
print(type(age))

print("Your age is: " + str(age))
print("Your age is: ", age)

age = str(age)

# Math: len() and count()
password = "123a"
print("Length is: ", len(password))

text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""

print(text.count("Python"))

# replace()
text = "2026/05/10"
print(text.replace("/", "-"))

phone = "176-1234-56"
print(phone.replace("-", ""))

price = "$1,299.99"
print(price.replace("$", ""))
print(price.replace("$", "").replace(",", "."))

phone_number = "+49 (176) 123-4567"
phone_number = phone_number.replace("+49", "0049")
phone_number = phone_number.replace("(", "")
phone_number = phone_number.replace(")", "")
phone_number = phone_number.replace("-", "")
phone_number = phone_number.replace(" ", "")
print(phone_number)

# re
phone_number = "+49 (176) 123-4567"
txt, n = re.subn("[+()-]", "", phone_number)
print(txt)

# String transformation
first_name = "Nicolas"
last_name = "Mertes"
full_name = first_name + " " + last_name
print("full_name:", full_name)

# f-string
name = "Nicolas"
age = 42
is_student = False
print("My name is " + name + ", I am " + str(age) + " years old.")
print(
    f"My name is {name}, I am {age} years old and student status is {is_student}.")
print(f"2 + 3 = {2 + 3}")
print(f"{{This is me}}")  # curly brackets in f-string output

# split()
information = "Adam-24-USA"
information.split()

stamp = "2026-09-20 14:30"
print(stamp.split(" "))

csv_file = "123,Max,USA,1979-10-05"
print(csv_file.split(","))

for e in csv_file.split(","):
    print(e)

print("=" * 80)

# Extract parts of a string
text = "This is a text"
print(text[1])

# Extract parts of a string (closed slicing)
text = "This is a text"
print(text[0:3])

# Extract parts of a string (open slicing)
text = "This is a text"
print(text[-3:])  # ext
print(text[:-3])  # This is a t


# Extract parts of a string (open slicing [start:end:step])
text = "This is a text"
print(text[0:4:2])  # Ti

# Extract the last character
text = "This is a text"
print(f"The last character is: {text[-1]}")

date = "2026-09-20"
if isinstance(date, str) and len(date) > 0:
    print(f"The year of string {date} is: {date.split('-')[0]}")
else:
    print("Empty string.")


# Whitespace Cleanup
text = " Engineering".lstrip()
print(text)

text = "Engineering ".rstrip()
print(text)

text = " Engineering ".strip()
print(text)

# Case Conversions
text = "python PROGRAMMING"
print(text.upper())
print(text.lower())

print(text.lower() == "python programming")

# python challenge
text = "968-Maria, ( D@t@ Engineer );; 27 y  "
name = text.split(";")[0].split(",")[0].split("-")[1]
role = text.split(";")[0].split(",")[1].replace("@","a").replace("(","").replace(")","").strip().lower()
age  = text.split(";")[2].replace("y", "").strip()

result = f"name: {name} | role: {role} | age: {age}"
print (result)

# startswith
text = "2026-Feb-10"
result = text.startswith("2026")
print(result)

# endswith
result = text.endswith("110")
print(result)

print(text.find("Feb"))

phone = "+49-176-12345"
print(phone.startswith("+49"))

email = "baraa@gmail.com"
print(phone.endswith("gmail.com"))

# in operatior
print("@" in email)
url = "https://api.company.com/v1/data"
print("/api" in url)

text = "Hallo"
print(text.isalpha())
print(text.isnumeric())

x = 3/2
print(f"Der Wert von x ist {x}")

x = 3//2
print(f"Der Wert von x ist {x}")

x = math.trunc(7.999)
print(f"Der Wert von x ist {x}")

x = int(7.999)
print(f"Der Wert von x ist {x}")


# ------------------------------------------------------------------------------
# Python Course #8 - Data Types - Numbers
# ------------------------------------------------------------------------------
x = random.random();
print(f"Der Wert von x ist {x}")

x = random.randint(1,6); # int number between 1 and 6
print(f"Der Wert von x ist {x}")

x = random.randint(a=1, b=6); # int number between 1 and 6
print(f"Der Wert von x ist {x}")

x = 7.0
print(x.is_integer()) # Check if values is integer

x = 7.1
print(x.is_integer())

x = 70.4
print(isinstance(x, int))

x = random.randint(1, 100)
is_even = (x%2) == 0
print(x)
print(is_even)

# This is a comment
# This is another comment