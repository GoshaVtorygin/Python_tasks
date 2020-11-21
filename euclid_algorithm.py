def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def egcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, cur_gcd = egcd(b, a % b)
    return y, x - (a // b)*y, cur_gcd

print(f"gcd of 0 and 0: {egcd(0, 0)[2]} = {egcd(0, 0)[0]}*0 + {egcd(0, 0)[1]}*0")
print(f"gcd of 2 and 5: {egcd(2, 5)[2]} = {egcd(2, 5)[0]}*2 + {egcd(2, 5)[1]}*5")
print(f"gcd of 12 and 18: {egcd(12, 18)[2]} = {egcd(12, 18)[0]}*12 + {egcd(12, 18)[1]}*18")
print(f"gcd of 17 and 31: {egcd(17, 31)[2]} = {egcd(17, 31)[0]}*17 + {egcd(17, 31)[1]}*31")
print(f"gcd of -99 and -63: {egcd(-99, -63)[2]} = {egcd(-99, -63)[0]}*(-99) + {egcd(-99, -63)[1]}*(-63)")
    

    
