

def hash(s):
    n = len(s)
    sum = 0
    for i in range(0, n):
        sum += ord(s[i]) * 2**(i+1)
    return sum

def Rabin_Karp(s, sub): #возвращает список индексов вхождений подстроки sub в строку s
    ind = []
    n = len(s)
    m = len(sub)
    hs = hash(s[:m])
    hsub = hash(sub)
    for i in range(0, n - m):
        if hs == hsub:
            ind += [i]
        hs = (hs - 2*ord(s[i])) // 2 + ord(s[m+i]) * 2**m
    if hs == hsub:
        ind += [i+1]    
    return ind


print(Rabin_Karp('abcefadbcghabcdabcd', 'abcd'))


