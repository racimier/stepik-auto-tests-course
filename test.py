def jj(st):
    st = list(map(int, st.split(' ')))
    len_st = len(st)
    res = []
    for i in range(len_st - 1):
        res.append(abs(st[i] - st[i + 1]))
    return 'Jolly' if set(res) == {i for i in range(1, len_st)} else 'Not jolly'


print(jj('1 -3 -4 -1 1'))
