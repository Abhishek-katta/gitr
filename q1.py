def binarySearch (list, l, r, x):
    if r >= l:

        mid = int(l + (r - l)/2)
        if list[mid] == x:
            return mid

        elif list[mid] > x:
            return binarySearch(list, l, mid-1, x)

        else:
            return binarySearch(list, mid+1, r, x)

    else:

        return -1

print ("Enter the size of list")
k = int(input())
print ("enter the list elements")
list=[]
i  = 0
while (i < k):
    a = input()
    list.append(a)
    i = i + 1
print ("enter the element that needs to be found")
x=input()
result = binarySearch(list, 0, len(list)-1, x)

if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in list")
