########################################################################################################################
# Task
# Given the participants score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.
########################################################################################################################

#  Done using sets
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b = set(arr)
    high = max(b)
    b.remove(high)
    high = max(b)
    print(high)

# sticking to the requirement of using lists
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b = list(arr)
    high = max(b)
    i=0
    while(i<n):
        if high == max(b):
            b.remove(high)
        i += 1
    print(max(b))
