def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)

    ans = []
    for candy in candies:
        if candy + extraCandies >= max_candies:
            ans.append(True)
        else:
            ans.append(False)

    return ans


candies = list(map(int, input("Enter candies: ").split()))
extraCandies = int(input("Enter extra candies: "))
print(kidsWithCandies(candies, extraCandies))
