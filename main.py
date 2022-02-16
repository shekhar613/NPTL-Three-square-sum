num = int(input("Enter a number"))

def threesquares(m):
    for p in range(0, m):
        for q in range(0, m):
            for r in range(0, m):
                if p*p + q*q + r*r == m:
                    return True
    return False

print(threesquares(num))

