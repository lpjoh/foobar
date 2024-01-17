def base_to_int(n, b):
    result = 0
    digit_count = len(n)
    
    for i in range(digit_count):
        result += int(n[i]) * pow(b, digit_count - 1 - i)
    
    return result

def int_to_base(n, b):
    result = ""
    m = 1
    
    while True:
        result = str(int(n / m) % b) + result
        
        m *= b
        
        if (n < m):
            return result

def solution(n, b):
    k = len(n)
    seen_nums = []
    
    while True:
        seen_nums.append(n)
        
        digits = list(n)
        digits.sort()
        
        y = "".join(digits)
        x = y[::-1]
        
        z = int_to_base(base_to_int(x, b) - base_to_int(y, b), b)
        z_count = len(z)
        
        if z_count < k:
            for _ in range(k - z_count):
                z = '0' + z
        
        n = z
        
        try:
            return len(seen_nums) - seen_nums.index(n)
        except ValueError:
            pass