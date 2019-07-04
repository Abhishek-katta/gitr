def last(n):
    return n[-1]

def sort(tuples):

    return sorted(tuples, key = last)

# driver code

def str2tupleList(s):
    return eval( "[%s]" % s )

a = input()
a = str2tupleList(a)
m = 2
print("Sorted:"),
print(sort(a))
