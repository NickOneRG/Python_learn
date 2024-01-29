
def f(Z):
    if Z == 0: return -1

    count, i, n = 0, 1, Z
    if Z < 0: n *= -1
    
    while i * i <= n:
        if n % i == 0:
            count += 2 if i * i != n else 1
            
        i += 1
    
    return count + 1 if count % 2 == 1 and Z > 0 else count

print(f(int(input())))