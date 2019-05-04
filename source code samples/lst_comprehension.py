# avoid cycles

x = [i for i in range(10)]

for i in x:
    print (i)

# without list comprehensions

squares = []
for x in range(10):
    squares.append(x**2)

print (squares)

squares_lc = [x**2 for x in range(10)]
print (squares_lc)