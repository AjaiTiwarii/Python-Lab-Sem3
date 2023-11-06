#Ques2 - Given a string S, find the length of the longest substring without repeating
        #characters and also print the substring(s).
def longestString(S):
    n = len(S)
    mp = {}
    LengthofSW = 0
    result = ''

    i = 0
    j = 0

    while j < n:
        if S[j] not in mp:
            mp[S[j]] = 0
        mp[S[j]] += 1

        if len(mp) == j - i + 1:
            if j - i + 1 > LengthofSW:
                LengthofSW = j - i + 1
                result = S[i:j+1]
            j += 1
        elif len(mp) < j - i + 1:
            while len(mp) < j - i + 1:
                mp[S[i]] -= 1
                if mp[S[i]] == 0:
                    del mp[S[i]]
                i += 1
            j += 1
        else:
            j += 1

    return result




#Q-1. Given an integer list nums. Return all the triplets [nums[i], nums[j],
        #nums[k]], such that, (i != j), (i != k), (j != k) and (nums[i] + nums[j] + nums[k] = 0).
def findTriplets(nums):
    n = len(nums)
    ans = []

    nums.sort()

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue 

        l=i+1
        r=n-1

        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                ans.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1 
                l += 1
                r -= 1
            elif sum < 0:
                l += 1
            else:
                r -= 1

    return ans




#Q-3. Given a string S. Return the longest palindromic substring in S.
def longestPalindromicSubstring(s):
    if not s:
        return ""

    def checkPalindrome(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    maxi = ""
    for i in range(len(s)):
        #single char ko centre mann kr
        validString1 = checkPalindrome(i, i)
        if len(validString1) > len(maxi):
            maxi = validString1

        # double char ko centre maan kr
        validString2 = checkPalindrome(i, i + 1)
        if len(validString2) > len(maxi):
            maxi = validString2

    return maxi



s = "ajaytiwari"
result = longestPalindromicSubstring(s)
print(result)  


S="ajaytiwari"
#S="abcdcdefghiiij"
ans = longestString(S)
print(ans)


nums = [-5,-2,0,-1,5]
print(findTriplets(nums))
