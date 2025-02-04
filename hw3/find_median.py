# pylint: skip-file
def median(X, Y):
    '''
    Write a Python function median(X, Y) that returns the median of all elements 
    from two sorted lists, X and Y. The sizes of X and Y may differ.
    Your algorithm should run in O(log (m + n)) time, where m is the length of X and
    n is the length of Y. Thus, you should not sort the combined list of X and Y. 
    Assume that each list contains at least one number. Duplicated numbers may be present.
    '''
    m = len(X)
    n = len(Y)
    # split X & Y into two parts, left X + left Y, right X + right Y
    if m > n :
        return median(Y, X)
    
    left = 0
    right = m
    while left <= right:
        partition_X = (left+right) // 2
        partition_Y = (m+n+1)//2-partition_X

        max_left_X = float('-inf') if partition_X == 0 else X[partition_X-1]
        min_right_X = float('inf') if partition_X == m else X[partition_X]
        max_left_Y = float('-inf') if partition_Y == 0 else Y[partition_Y-1]
        min_right_Y = float('inf') if partition_Y == n else Y[partition_Y]

        if max_left_X <= min_right_Y and min_right_X >= max_left_Y:
            if (m+n)%2 == 0:
                ans = (max(max_left_X,max_left_Y)+min(min_right_X,min_right_Y))/2
            else:
                ans = max(max_left_X,max_left_Y)
            print( "--> median: ", ans)
            return ans
        elif max_left_X > min_right_Y:
            right = partition_X-1
        else:
            left = partition_X+1


median([1], [2, 3]) # return 2.0
median([1, 3], [2]) # return 2.0
median([1, 2], [3, 4]) # returns 2.5
median([1,2,3,4], [3,4]) # returns 3.0
median([0,0,0,2,2], [1,1,1,1,1]) # returns 1.0
median([1,3,5,7,9], [2,4,6,8,10,11]) # returns 6.0
median([1,3,7,8,9], [2,4,5,6,10,11]) # returns 6.0
median([1], [2,3,4,5,6,7]) # returns 4.0
median([10,20,30,100], [40,60]) # returns 35.0