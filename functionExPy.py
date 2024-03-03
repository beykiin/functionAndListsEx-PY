def fakt(a):
    if a <= 1:
        return a
    return a*fakt(a-1)

print(fakt(5))