def solve_in_int(a, b, c, d):
    if a == 0:
            if any((b != 0,all((b == 0, c == 0, d == 0)))):
                return "NO"
            else:
                return "INF"
    else:           
         x =  - b/a 
    if x.is_integer():
        x = int(x)
    else:
        return "NO"
    if ( c*x + d != 0 ):
        return x
    return "NO"

a, b, c, d = map(int, (input() for _ in range(4)))
print (solve_in_int(a, b, c, d))
