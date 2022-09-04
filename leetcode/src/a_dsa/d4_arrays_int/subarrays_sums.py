
# LC53. Maximum Subarray   - max sum amount all subarrays
def maxSubArray(self, nums: List[int]) -> int:
    total = max_total = nums[0]
    for i in range(1, len(nums)):
        total += nums[i]
        # if the total is not worth to keep, start a new total
        # we can also add code to keep track the start index.
        total = max(total, nums[i])
        max_total = max(max_total, total)  # this is our goal.
    return max_total

# LC1658. Minimum Operations to Reduce X to Zero - reduce to zero
def minOperations(self, nums: List[int], x: int) -> int:  # O(n) time and O(1) space - O(1) space is excellent
    # This problem is equivalent to finding the longest subarray whose sum is == totalSum - x
    target = sum(nums) - x
    if target < 0: return -1
    res, cur, start = -1, 0, 0
    for end in range(len(nums)):
        cur += nums[end]
        while cur > target and start <= end:
            cur -= nums[start]
            start += 1
        if cur == target:
            res = max(res, end - start + 1)
    return len(nums) - res if res > -1 else -1

# LC325. Maximum Size Subarray Sum Equals k
def maxSubArrayLen(self, nums: List[int], k: int) -> int:  # O(n) time and space
    maxl, cumu, cache = 0, 0, dict()  # cumu -> index
    for i, v in enumerate(nums):
        cumu += v
        if cumu == k: maxl = max(maxl, i+1)
        elif cumu - k in cache:  # middle subarray
            maxl = max(maxl, i - cache[cumu - k])
        if cumu not in cache: cache[cumu] = i  # maintain earliest index
    return maxl

# LC209. Minimum Size Subarray Sum - min size with sum target, all positives
def minSubArrayLen(self, s: int, nums: List[int]) -> int:  # 2 pointers , O(n) time and O(1) space
    total = left = 0 # since all numbers are positive, this works.
    result = len(nums) + 1
    for right, n in enumerate(nums):
        total += n
        while total >= s:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    return result if result <= len(nums) else 0

# LC560. Subarray Sum Equals K - total count of subarrays whose sum equals to k
from typing import List
def subarraySum(self, nums: List[int], k: int) -> int:
    count = cusum = 0  # O(n)
    counts = collections.defaultdict(int)
    for i in range(len(nums)):
        cusum += nums[i]
        if cusum == k: count += 1
        if cusum - k in counts: count += counts[cusum - k]
        counts[cusum] += 1
    return count

# LC523. Continuous Subarray Sum - if exist s.t. sum to multiple of k
def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    if not nums: return False
    summ, sd = 0, {0: -1}  # [2,4,3] 6, we need -1 for 2-element requirement
    for i, n in enumerate(nums):
        summ += n
        if k != 0: summ = summ % k
        if summ in sd:  # sd is sum dict, map sum -> index
            if i - sd[summ] > 1: return True  # [0] 0 if we have =, it returns true but answer is false.
        else: sd[summ] = i
    return False




# LC974. Subarray Sums Divisible by K - return # of such sums
def subarraysDivByK(self, A: List[int], K: int) -> int:
    if not A: return 0
    cumu = list(accumulate(A))
    # pre-append 0 because we count x // K == 0 in down below formula. need one more 0 for c*c(-1)
    res = [0] + [x % K for x in cumu]  # check case 2, 3, 4
    counts = Counter(res) # number of cumus having same residue.
    # once we subtract any of these 2, we have the subarray sum divided by K.
    # so selecting 2 elements has C(C-1) / 2 possibilities.
    return sum(c * (c - 1) // 2 for c in counts.values())


# LC862. Shortest Subarray with Sum at Least K - could be negative
def shortestSubarray(self, nums: List[int], k: int) -> int:  # O(n) in time and space
    d = collections.deque([[0, 0]])  # idx and cumu value
    res, cur = float('inf'), 0
    for i, a in enumerate(nums):
        cur += a
        while d and cur - d[0][1] >= k:
            res = min(res, i + 1 - d.popleft()[0])
        # if cur < v, the later on, cur1 - cur > cur1 - v with shorter idx
        while d and cur <= d[-1][1]: d.pop()  # so d is increasing on cumus
        d.append([i + 1, cur])
    return res if res < float('inf') else -1

# LC548. Split Array with Equal Sum - split 4 sums
def splitArray(self, nums): # O(n^2)
    def split(A):  # return half sum
        for i in range(1, len(A)): A[i] += A[i-1]  # cum sum
        return {A[i-1] for i in range(1, len(A)-1) if A[i-1] == A[len(A)-1] - A[i]}

    return any(split(nums[:j]) & split(nums[j+1:]) for j in range(3, len(nums)-3))



# LC643. Maximum Average Subarray I - max window average
def findMaxAverage(self, nums: List[int], k: int) -> float:
    best = window = sum(nums[:k])
    for i in range(k,len(nums)):
        window += nums[i] - nums[i-k]  # sliding window
        if window > best: best = window
    return best/k

# LC581. Shortest Unsorted Continuous Subarray
def findUnsortedSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    maxv, minv = nums[0], nums[n-1]
    begin, end = -1, -2  # so that end - begin + 1 = 0 if sorted
    for i in range(1, n):
        maxv = max(maxv, nums[i])
        minv = min(minv, nums[~i])
        if nums[i] < maxv: end = i  # last seen smaller value with index i
        if nums[~i] > minv: begin = n - 1 - i  # last seen larger value from right side
    return end - begin + 1

# LC2025. Maximum Number of Ways to Partition an Array - to  2 parts with equal sum with change k
def waysToPartition(self, nums: List[int], k: int) -> int:
    # https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/discuss/1499026/Short-Python-solution-Compute-prefix-sums%3A-O(n)
    prefix_sums = list(accumulate(nums))
    total_sum = prefix_sums[-1]
    # not replace with k, :-1 is because it's half sum, -1 is the other half, [0, 0, 0]
    best = prefix_sums[:-1].count(total_sum // 2) if total_sum % 2 == 0 else 0
    # diff = after pivot - before pivot = total sum - prefix_sum * 2, exclude last
    # [0, 1, 0], 0 requires last exclusion
    after_counts = Counter(total_sum - 2 * prefix_sum for prefix_sum in prefix_sums[:-1])
    before_counts = Counter()
    best = max(best, after_counts[k - nums[0]])  # If we change first num
    for prefix, x in zip(prefix_sums, nums[1:]):  # O(n)
        gap = total_sum - 2 * prefix  # diff need to fix
        after_counts[gap] -= 1
        before_counts[gap] += 1
        # k-num[i] is the diff to replace num[i], and the diff of presums
        # This value, for a fixed i, is the count of indices j with j > i that satisfy gap[j] == k - nums[i],
        # plus the number of indices j with 1 <= j <= i such that -gap[j] == k - nums[i]
        best = max(best, after_counts[k - x] + before_counts[x - k])
    return best



# LC152. Maximum Product Subarray
def maxProduct(self, nums: List[int]) -> int:
    if not nums: return 0
    max_all = curr_max = curr_min = nums[0]
    for i in range(1, len(nums)):
        e = nums[i]
        emx = e * curr_max
        emn = e * curr_min
        curr_max = max([e, emx, emn])  # we track both for +/-
        curr_min = min([e, emx, emn])
        max_all = max(max_all, curr_max)
    return max_all

# LC689. Maximum Sum of 3 Non-Overlapping Subarrays
def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:  # O(n)
    bestSeq, best2Seq, best3Seq = 0, [0, k], [0, k, k*2]
    seqSum, seq2Sum, seq3Sum = sum(nums[0:k]), sum(nums[k:k*2]), sum(nums[k*2:k*3])
    # Sums of combined best windows
    best1Sum, best2Sum, best3Sum = seqSum, seqSum + seq2Sum, seqSum + seq2Sum + seq3Sum
    seqIndex, seq2Index, seq3Index = 1, k + 1, k*2 + 1  # Current window positions
    while seq3Index <= len(nums) - k:
        # Update the three sliding windows
        seqSum += - nums[seqIndex - 1] + nums[seqIndex + k - 1]
        seq2Sum += - nums[seq2Index - 1] + nums[seq2Index + k - 1]
        seq3Sum += - nums[seq3Index - 1] + nums[seq3Index + k - 1]
        if seqSum > best1Sum:  # Update best single window
            bestSeq, best1Sum = seqIndex, seqSum
        if seq2Sum + best1Sum > best2Sum:  # Update best two windows
            best2Seq, best2Sum = [bestSeq, seq2Index], seq2Sum + best1Sum
        if seq3Sum + best2Sum > best3Sum:  # Update best three windows
            best3Seq, best3Sum = best2Seq + [seq3Index], seq3Sum + best2Sum
        seqIndex += 1  # Update the current positions
        seq2Index += 1
        seq3Index += 1
    return best3Seq
