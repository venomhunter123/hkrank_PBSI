def check(n, i, maxSum, m):
    for d in range(1, m):
        if maxSum < 0:
            break
        if i + d < n:
            maxSum -= m - d
        if i - d >= 0:
            maxSum -= m - d
    return maxSum >= 0

def maxElement(n, maxSum, k):
    l = 0
    r = maxSum
    while l < r:
        m = (l + r + 1) // 2
        if check(n, k, maxSum - n - m, m):
            l = m
        else:
            r = m - 1
    return l + 1

if __name__ == '__main__':
    n = int(input().strip())
    maxSum = int(input().strip())
    k = int(input().strip())

    result = maxElement(n, maxSum, k)
    print(result)
