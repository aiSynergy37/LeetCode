def candy(ratings):
    n,ans = len(ratings), [1] * len(ratings)

    for i in range(n - 1):
        if ratings[i] < ratings[i + 1]:
            ans[i+1] = max(1 + ans[i], ans[i+1])

    for i in range(n - 2, -1, -1):
        if ratings[i+1] < ratings[i]:
            ans[i] = max(1 + ans[i+1], ans[i])

    return sum(ans)


ratings = [1, 2, 2]
print(candy(ratings))


print(candy([1,0,2]))

