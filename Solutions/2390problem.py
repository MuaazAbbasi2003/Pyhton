class Solution(object):
    def removeStars(self, s):
        vak=[]
        for x in s:
            if x == "*":
                vak.pop()
            else:
                vak.append(x)
        return "".join(vak)

s = "leet**cod*e"
arr = list(s)

sol = Solution()
result = sol.removeStars(s)
print(result)