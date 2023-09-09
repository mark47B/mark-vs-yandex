# Not full
input()
s = input()

co_dv = dict()

if len(s) == 2:
    print(s)
else:
    for i in range(0, len(s)-2):
        if s[i:i+2] not in co_dv.keys():
            co_dv[s[i:i+2]] = 1
        else:
            co_dv[s[i:i+2]] = co_dv[s[i:i+2]] + 1
    result = str()
    result_count = 0
    for k, v in co_dv.items():
        if v > result_count:
            result = k
            result_count = v
    print(result)

