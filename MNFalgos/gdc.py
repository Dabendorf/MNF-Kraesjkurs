def gcd(a, b):
    while b > 0:
        q = a//b 	# quotient
        r = a-q*b	# resten
        print(f"a: {a}, b: {b}, q: {q}, r: {r}")
        a = b
        b = r
        #print(f"a: {a}, b: {b}, q: {q}, r: {r}")
    print("========")
    return a
print(gcd(6,4))
print(gcd(9,4))
print(gcd(8,4))
print(gcd(28,12))
print(gcd(44,22))
print(gcd(72,19))
