from sys import stdin, stdout
import collections
def main():
    t = [int(x) for x in stdin.readline().split()]
    r = [int(x) for x in stdin.readline().split()]
    weights = collections.deque(sorted(r))
    limit = t[1]
    carts = 0
    while (weights):
        if (limit - weights[0] < weights[-1]):
            weights.pop()
            carts += 1
        elif(limit - weights[0] == weights[-1]):
            weights.pop()
            weights.popleft()
            carts += 1
        else:
            x = 0
            y = len(weights) - 2 #I'm going to assume that the second largest weight satisfies the condition
            while (y >= 1 and weights[x + 1] > weights[x]):
                while(x+y < len(weights) and limit - weights[x + y] >= weights[-1]):
                    x += y
                y //= 2 #now weights[x] is the golden boy
            if (x <= len(weights) //2 - 1):
                weights.rotate(-x)
                weights.popleft()
                weights.rotate(x)
                if (weights):
                    weights.pop()
            else:
                weights.rotate(x)
                weights.pop()
                weights.rotate(-x)
                if (weights):
                    weights.pop()
            carts += 1
    print(carts)
main()
