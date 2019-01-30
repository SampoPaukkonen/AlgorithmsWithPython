from sys import stdin, stdout
import collections


def main():
    queries = stdin.readlines()[1:]
    entry = collections.deque([])
    exit = collections.deque([])
    current_people = 0
    max_people = 0
    for cq in queries:
        a, b = [int(x) for x in cq.split()]
        entry.append(a)
        exit.append(b)
    entry = collections.deque(sorted(entry))
    exit = collections.deque(sorted(exit))
    while (entry and exit):
        change = 0
        if (entry[0] < exit[0]):
            entry.popleft()
            current_people += 1
        else:
            exit.popleft()
            current_people -= 1
        if (current_people > max_people):
            max_people = current_people
    print(max_people)
main()
