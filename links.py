

# a = [1, 2, 3, 4, 5]
#
# b = a.copy()
#
#
# a.append(100)
#
# print(b)
# print(a)



q = [
    1, 2, 3, 4,
    "hello",
    [12, 13, 14]
]


w = q.copy()

# w.append(1000)
w[5].append(1000)

print(q, w)