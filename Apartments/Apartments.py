from collections import deque, OrderedDict
from sys import stdin, stdout

def main():
    r = [int(x) for x in stdin.readline().split()]        #The amount of applicants, the amount of apartments and delta
    n = [int(x) for x in stdin.readline().split()]        #Size wishes of the applicants
    p = [int(x) for x in stdin.readline().split()]        #Sizes of the apartments
    n = deque(sorted(n))
    p.sort()
    m = OrderedDict()                                     #OrderedDict for the apartments with string indicies as keys
    if (p):                                               #To check if p has anything inside
        for i in range(len(p)):
            m[str(i)] = p[i]
    d = r[-1]                                             #delta is the last element in r
    counter = 0
    while(m and n):
        while (m and n[0] - d > m[next(iter(m))]):        #Here we take out the apartments which will not satisfy anyones needs.
            del m[next(iter(m))]
        i = next((i for i,a in m.items() if abs(n[0] - a) <= d), "NotFound") #Index of the apartment for the smallest size wish
        if (i != "NotFound"):
            del m[i]
            n.popleft()
            counter += 1
        else:
            n.popleft()
    print(counter)
main()
