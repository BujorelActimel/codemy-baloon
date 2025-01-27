def is_prime(nr: int) -> bool:
    if nr == 2:
        return True
    
    if nr % 2 == 0:
        return False
    
    i = 3
    while i * i <= nr:
        if nr % i == 0:
            return False
        i += 2
    
    return True


for nr in range(100):
    if is_prime(nr):
        print(nr)
