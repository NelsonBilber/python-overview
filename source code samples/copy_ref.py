def func(other):
    print ("func -> other before change: ", id(other))
    print (first is other)
    other = 2
    print ("func -> other after change: ",id(other))
    print (first is other)

first = 1
print (id(first))

func(first)

print (first)
print (id(first))
print ("=============")

# --------------------------------------------

def funcList(other):
    other[0] += 1
    print (lst is other)
    other += [1]
    print (lst is other)

lst = [1]
funcList(lst)
print (lst)

# imutable objects (int, str, long, tuples)
# mutables objctes (list, dictionaries)