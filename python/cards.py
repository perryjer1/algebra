"""Order of shuffling a deck of n cards"""

n = 52

top = range(1,n+1)
bot = top[0:n:2]
bot.extend(top[1:n:2])

perm = dict(zip(top,bot))

cur = 1
groups = []
while cur <= n:
    temp = list([cur])
    var = cur
    while perm[var] not in temp:
        var = perm[var]
        temp.append(var)
    groups.append(temp)
    while True:
        cur += 1
        if not any([cur in grp for grp in groups]):
            break

print groups
print [len(grp) for grp in groups]
