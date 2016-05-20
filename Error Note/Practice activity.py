A = [x for x in range(1, 1000) if x % 5 == 0]
print (A)

B = [x for x in range(1, 1000) if x % 3 == 0]
print (B)



S = sum(A+B)
print (S)