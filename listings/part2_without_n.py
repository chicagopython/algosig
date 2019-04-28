def helper(left, right):
    mid = int((right+left)/2)
    if right <= left:
        return left
    if isBadVersion(mid):
        return helper(left, mid)
    else:
        return helper(mid+1, right*2)
    
def firstBadVersion(n):
    return helper(1,2)