def gcdExtended(a, b):
    if a == 0:
    	print(f"Base case: gcd: {b}, x: {0}, y: {1}")
    	return b, 0, 1
            
    gcd, x1, y1 = gcdExtended(b%a, a)
    
    x = y1 - (b//a) * x1
    y = x1
    print(f"gcd: {gcd}, x1: {x1}, y1: {y1}, x: {x}, y: {y}")
    
    #print("bla")
    return gcd, x, y

"""a,b = 6,4
gcd,x,y = gcdExtended(a,b)
print("gcd(", a , "," , b, ") = ", gcd)
print(f"{a}*{x} + {b}*{y} = {gcd}")
a,b = 9,4
gcd,x,y = gcdExtended(a,b)
print("gcd(", a , "," , b, ") = ", gcd)
print(f"{a}*{x} + {b}*{y} = {gcd}")
a,b = 8,4
gcd,x,y = gcdExtended(a,b)
print("gcd(", a , "," , b, ") = ", gcd)
print(f"{a}*{x} + {b}*{y} = {gcd}")
a,b = 12,28
gcd,x,y = gcdExtended(a,b)
print("gcd(", a , "," , b, ") = ", gcd)
print(f"{a}*{x} + {b}*{y} = {gcd}")
a,b = 44,22
gcd,x,y = gcdExtended(a,b)
print("gcd(", a , "," , b, ") = ", gcd)
print(f"{a}*{x} + {b}*{y} = {gcd}")"""
a,b = 23,72
gcd,x,y = gcdExtended(a,b)
print("gcd(", a , "," , b, ") = ", gcd)
print(f"{a}*{x} + {b}*{y} = {gcd}")
