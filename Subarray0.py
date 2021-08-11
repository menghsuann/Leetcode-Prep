def subArrayExists(arr, n):
    n_sum = 0
    s = set()
 
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
 
    return False

#https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
