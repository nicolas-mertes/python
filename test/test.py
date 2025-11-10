
import sys as sys

print(sys.argv[0])

"""
# Read the CSV file
df = pd.read_csv("data/data_01.csv")

# View the first 5 rows
#print(df)

ages = pd.Series([22, 35, 58], name="Age")
#print(ages)

print(ages.max())

df.to_excel("./titanic.xls", sheet_name="passengers", index=False)
"""

is_test = True
if is_test:
    print('Is Test')

print("""\
      TEST 2
      """)

print(3*'un')
name = 'Nicolas'
print(name[-1])

print(name[0:10])

name2 = name[:3]
print(name2)
print(len(name2))

# 3.1.3 Lists
squares = [1,2,3,4]
squares.append('Test')
print('squares = [' + str(squares) + ']')

a=0
b=1
while a<10:
    print(a)
    a=b
    b=a+b

def f(a, L=[]):
    L.append(a)
    return L;

def concat(*args, sep="/"):
    return sep.join(args)

print (concat('eine', 'kleine', 'Micky', sep="\n"))

# 4.9.6. Lambda Expressions
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs.sort(key=lambda pair: pair[1], reverse=True))


# 5.1. More on Lists
fruits = ['apple', 'banana', 'cherry', 'orange']
len = len(fruits)

fruits.sort(reverse=True)
print(f"Die Länge der Liste ist {len}")
print(fruits)
print(fruits.pop())
print(fruits)
fruits.append('apple')
print(fruits)