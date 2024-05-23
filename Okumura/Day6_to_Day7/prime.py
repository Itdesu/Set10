import sys
args = sys.argv

n = int(args[1])

def prime_factor(n):
    a = []

    while n % 2 == 0:
        a.append(2)
        n //= 2
    
    f = 3

    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else: f += 2
    
    if n != 1:
        a.append(n)
    return a

n_len = len(prime_factor(n))

if n >= 1000:
    print("1000以上は判定できません",end="")
elif n_len == 1:
    print("Prime", end="")
else:
    print("not", end="")