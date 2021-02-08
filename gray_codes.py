def to_gray(n):
    return bin(n ^ (n >> 1))


code_n = 127
for i in (125, 126, 127, 128, 129, 130):
    print(i, to_gray(i))
