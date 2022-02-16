'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# if input number cannot be expresed in the form of 4^a(8b+7)

num = int(input("Enter a number"))

def threesquares(m):
    for p in range(0, m):
        for q in range(0, m):
            for r in range(0, m):
                if p*p + q*q + r*r == m:
                    return True
    return False

print(threesquares(num))

