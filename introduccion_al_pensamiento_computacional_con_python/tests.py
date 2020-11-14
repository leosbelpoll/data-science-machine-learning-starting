a, b = (34, 456)
print(a, b)

r = range(1, 5)
print(type(r))

for i in r:
    print(i)
r2 = range(1, 5)

print(id(r2))
print(id(r))

print(r == r2)
print(r is r2)

for i in range(1, 10, 2):
    print(i)

l = list(range(4))
l.append(234)
print(l)

l2 = list(range(100))
d = [(0, i) for i in l2 if i % 2 == 0]
print(d)
