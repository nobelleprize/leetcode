from collections import defaultdict

def solution(names:list):
    res = []
    d = dict()
    for name in names:
        if name not in d:
            d[name] = 0
        else:
            d[name] += 1
            temp = name + "(" + str(d[name]) + ")"
            while temp in d:
                d[name] += 1
                temp = name + "(" + str(d[name]) + ")"
            d[temp] = 0
    for key in d.keys():
        res.append(key)
    return res

print(solution(["gta", "gta(1)", "gta", "avalon"]))
print(solution(["kaido", "kaido(1)", "kaido(2)", "kaido(1)(1)"]))
print(solution(["wano", "wano", "wano", "wano"]))
print(solution(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))
print(solution(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))