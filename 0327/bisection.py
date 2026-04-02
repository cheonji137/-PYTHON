import random


x = sorted(random.sample(range(1, 100), 10))
print("리스트:", x)


t = random.choice(x)
print("찾을 값:", t)

l = 0
r = len(x) - 1

for i in range(len(x)):
    m = (l + r) // 2
    print("중간값 인덱스:", m, "값:", x[m])

    if x[m] == t:
        print("찾았다:", m)
        break

    if x[m] < t:
        l = m + 1
    else:
        r = m - 1