def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    if amount <=0:
        return 1
    """
    Not below ,otherwise there are repeated
    思路:如果我需要知道找开【n元】的方法，我可以依次找到找开【n - coins[i]】元有多少种方法（然而直接相加有重叠。。。）
    1：1
    2：1+1 ，2
    3：1+1+1，2+1
    4：1+1+1+1，2+1+1，2+2
    5：1+1+1+1+1，2+1+1+1，2+2+1. 5
    f(1) = 1
    f(2) = [f(1) + 1] + [2]
    f(3) = [f(2) + 1] || [f(1)] + f(2)
    f(4) = [f(3) + 1] + [2 + 2] || [f(2) + 2] + 
    f(5) = [f(4) + 1] + [5]
    最大疑问，这个重复应该如何越过去？
    Tips:背包问题
    通用思路:
    f[i][j]:第i个物品放进去，还剩j个空间，此时价值

    应用:
    f[i][j]:前i个硬币找开j元有多少种
    f[1][1]:1
    f[1][2]:1
    f[2][1]:1
    f[2][2]:f[1][2 - coins[i]]
    f[1][3]:f[1][3 - coins[0]](1+1+1)
    f[2][3]:f[2][3 - coins[0]](1+1+1, 2+1)
    """    
    # temp = [0]*(amount + 1)
    # ans = [list(temp)]*(len(coins)+1)
    ans = []
    for i in range(len(coins)+1):
        ans.append([0]*(amount+1))

    # print(ans)
    for i in range(1, len(coins) + 1):

        # make up 0 zero has 0 method
        ans[i][0] = 0
        for j in range(1, amount + 1):
            ans[i][j] = ans[i-1][j]
            ans[i][j] += ans[i][j - coins[i - 1]] if j -coins[i - 1]>=0 else 0
            if coins[i - 1] == j:
                ans[i][j] += 1

    return ans[len(coins)][amount]

if __name__ == '__main__':
    print(change(4, [2]))