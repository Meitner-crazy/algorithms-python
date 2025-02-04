# pylint: skip-file
def maxSubArray(A:list):
    cur=A[0]
    curSum=cur
    ans=[cur]
    temp = [cur]

    for i in range(1,len(A)):
        if cur + A[i] > A[i]: # 0 will be excluded 
            cur += A[i]
            temp.append(A[i])
        else:
            cur = A[i]
            temp = [A[i]] # reset

        if cur > curSum:
            curSum = cur
            ans = temp[:]
    
    print(f"Max subarray: {ans},  {curSum}")


print('----------------Test maxSubArray----------------')
maxSubArray([-100]) # returns ([-100], -100)
maxSubArray([13, -100, 20]) # returns ([20], 20)
maxSubArray([-100, 20, -10, 60, 80]) # returns ([20, -10, 60, 80], 150)
maxSubArray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])# returns ([18, 20, -7, 12], 43)
#all numbers greater than 0
maxSubArray([100, 20, 10, 60, 80]) # returns ([100, 20, 10, 60, 80], 270)
#first number is negative
maxSubArray([-100, 20, 10, 60, 80]) # returns ([20, 10, 60, 80], 170)
maxSubArray([80,-20]) # returns ([80], 60)
#all negative
maxSubArray([-10,-1,-3,-5,-19]) # returns ([-1], -1)
maxSubArray([-2,10,-3,-5,-19]) # returns ([10], 10)
maxSubArray([2,-10,-3,-5,-19]) # returns ([2], 2)
maxSubArray([200000,5,-19]) # returns ([200000,5], 200005)
print('------------------------------------------------')
