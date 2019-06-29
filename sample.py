def calc(nums, res):
    n = len(nums)
    if n == 1 and nums[0][0] >= 23.99 and nums[0][0] <= 24.001:
        res.add(nums[0][1])
        return
        
    for i in range(n - 1):
        for j in range(i + 1, n):
            nums2 = nums.copy()
            del nums2[j]
            del nums2[i]
            s = "(" + nums[i][1] + "+" + nums[j][1] + ")"
            nums2.append((nums[i][0] + nums[j][0], s))
            calc(nums2, res)
            nums2.pop()
            s = "(" + nums[i][1] + "-" + nums[j][1] + ")"
            nums2.append((nums[i][0] - nums[j][0], s))
            calc(nums2, res)
            nums2.pop()
            s = "(" + nums[j][1] + "-" + nums[i][1] + ")"
            nums2.append((nums[j][0] - nums[i][0], s))
            calc(nums2, res)
            nums2.pop()
            s = "(" + nums[i][1] + "*" + nums[j][1] + ")"
            nums2.append((nums[i][0] * nums[j][0], s))
            calc(nums2, res)
            if nums[j][0] != 0:
                nums2.pop()
                s = "(" + nums[i][1] + "/" + nums[j][1] + ")"
                nums2.append((nums[i][0] / nums[j][0], s))
                calc(nums2, res)
            if nums[i][0] != 0:
                nums2.pop()
                s = "(" + nums[j][1] + "/" + nums[i][1] + ")"
                nums2.append((nums[j][0] / nums[i][0], s))
                calc(nums2, res)
            
                
input = [8,8,9,10]
nums = []
for i in range(len(input)):
    nums.append((input[i], str(input[i])))
res = set()
calc(nums, res)
print(res)
