Q = 2**64 - 1
X = 2

def hash(s):
    n = len(s)
    sum = 0
    for i in range(0, n):
        sum += ord(s[i]) * X**(n-(i+1))
    return sum % Q

def Rabin_Karp(s, sub): #возвращает индекс первого вхождения подстроки sub в строку s или -1 
    n = len(s)
    m = len(sub)
    hs = hash(s[:m])
    hsub = hash(sub)
    for i in range(0, n - m + 1):
       print(hs, hsub) 
       if hs == hsub:
           return i
       hs = ((hs - (ord(s[i]) * X**(m-1+i)) * X + ord(s[m+i]) % Q)) % Q
       hs = hash(s[i+1:m+i+1]) 
    return -1


