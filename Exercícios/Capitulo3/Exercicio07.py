A = {1,2,3}
B = {'a','b','c'}
C = {-1,0,1}
D = {1,'a'}
E = set([])
F = A.union(B.union(C))
G = C.union(A.union(F.intersection(A)))

print(E.issubset(A))

print(E.issubset(B))

print(E.issubset(C))

print(E.issubset(D))

print(E.issubset(E))

print(E.issubset(F))

print(E.issubset(G))