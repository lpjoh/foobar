out = ""
n = 1

while True:
    if len(out) >= 10000 + 5:
        break
    
    n += 1
    
    is_prime = False
    
    for i in range(n - 2):
        if n % (i + 2) == 0:
            is_prime = True
            break
    
    if is_prime:
        continue
    
    out += str(n)

print(out)