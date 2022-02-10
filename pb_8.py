def findlcs(t1,t2):
    dp = [[0]*(len(t2)+1)]*(len(t1)+1)
    for i in range (1,len(t1)+1):
        for j in range (1,len(t2)+1):
            if t1[i-1]==t2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                print(t1[i-1],end="")
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

u = "acegi"
v = "abcdefgh"
findlcs(u,v)


