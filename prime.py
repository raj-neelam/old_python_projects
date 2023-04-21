def is_prime(n):
    z = int(n**0.5)
    if n == 1:
        return False
    if n == 2:
        return True
    if n>2 and n%2==0:
        return False
    for i in range(2,z+1):
        if n%i == 0:
            return False
    return True

l = []
for i in range(1,10000000):
    if is_prime(i):
        l.append(i)
    # is_prime(i)
print(l)
    # v1 = 50.983
    # v2 = 0.571
