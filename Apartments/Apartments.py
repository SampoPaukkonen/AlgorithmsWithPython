from collections import deque
from sys import stdin, stdout

def main():
    r = [int(x) for x in stdin.readline().split()]        #The amount of applicants, the amount of apartments and delta
    n = [int(x) for x in stdin.readline().split()]        #Size wishes of the applicants
    m = [int(x) for x in stdin.readline().split()]        #Sizes of the apartments
    n = deque(sorted(n))
    m.sort()
    d = r[-1] #delta is the last element in r
    counter = 0
    while(m and n):
        i = next((i for i,a in enumerate(m) if abs(n[0] - a) <= d), "NotFound") #Index of the apartment for the smallest size wish
        if (i != "NotFound"):
            #print("{}".format(i))
            m.pop(i)
            n.popleft()
            counter += 1
        else:
            n.popleft()
    print(counter)
main()

"""TODO: Currently seems to bug with the aparment selection. If delta is zero doens't act accordingly.
There could be a shortcut for cases where n and m are equal after sorting by simply printing out the size of
either list"""
