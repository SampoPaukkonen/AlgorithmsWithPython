from sys import stdin, stdout
import math


'''
Here we implement a binary search as follows:
z is the upperbound. x is the index of latest time.
If we can produce the number of products m in the time x + z, then we divide z
by half. If we can't we then increment x by the latest z. The smallest required
time is x + 1 at the end of the program.
'''
def main():
    t = [int(x) for x in stdin.readline().split()]
    a = [int(x) for x in stdin.readline().split()]
    #a.sort()
    n = t[0]
    m = t[1]
    z = (10**15) + 5
    x = 0
    while(z>= 1):
        while(not(efficiency(z + x, a, m))):
            x += z
        z //= 2
    x+=1
    print(x)


'''
Function efficiency tells how many full products will the factory
produce in a given time. If during the summing the sum happens to exceed m or
a partial sum happens to be zero (since the list is sorted) the process is
terminated.
params:
    z is the given time
    a is the efficiencies of the machines
    m is the number of products
return: does number of produces products match the param products.
'''
def efficiency(z, a, m):
    sum = 0
    for time in a:
        #if (z//time == 0):
        #    return sum >= m
        sum += z//time
        if (sum >= m):
            return True
    return sum >= m

main()
