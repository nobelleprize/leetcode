# https://www.geeksforgeeks.org/friends-pairing-problem/
# https://math.stackexchange.com/questions/2833504/friends-pairing-problem

def friends(n):
    dp = [0 for _ in range(n+1)]
    for i in range(n + 1):
        if i <= 2:
            dp[i] = i
        else:
            dp[i] = dp[i-1] + (i-1) * dp[i-2]
    return dp[n]

print(friends(3))
# print(friends(4))