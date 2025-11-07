a=(1,2,3,4,7,True,"Deekshith","Hi")

print(type(a))

no=a.count(4)

print(no)

t = (5, 1, 8, 3)
    

print(len(t))    # 4  (number of elements)
print(max(t))    # 8  (largest element)
print(min(t))    # 1  (smallest element)
print(sum(t))    # 17 (sum of elements)
print(sorted(t)) # [1, 3, 5, 8] (returns a list)
print(any(t))    # True (if at least one element is True/non-zero)
print(all(t))    # True (if all elements are True/non-zero)

print(t.index(8))        # 1
print(t.index(3, 2))     # 3 (search starts from index 2)