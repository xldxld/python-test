
# LC1446. Consecutive Characters - power of a string - same chars
def maxPower(self, s: str) -> int:
    count = max_count = 0  # similar to 485
    previous = None
    for c in s:
        if c == previous: count += 1
        else:
            max_count = max(max_count, count)
            previous = c
            count = 1
    return max(max_count, count)

# LC97. Interleaving String
def isInterleave(self, s1: str, s2: str, s3: str) -> bool:  # O(nm) time and space, space can be O(n)
    if len(s1) + len(s2) != len(s3): return False
    m, n = len(s1), len(s2)
    @lru_cache(None)
    def dp(i, j):
        if i == m and j == n: return True  # Found a valid match
        ans = False
        if i < m and s1[i] == s3[i+j]:  # Case match s1[i] with s3[i+j]
            ans |= dp(i + 1, j)
        if j < n and s2[j] == s3[i+j]:  # Case match s2[j] with s3[i+j]
            ans |= dp(i, j + 1)
        return ans
    return dp(0, 0)

# LC796. Rotate String
def rotateString(self, A: str, B: str) -> bool:  # O(n^2)
    return len(A) == len(B) and B in A + A

# LC784. Letter Case Permutation
def letterCasePermutation(self, s: str) -> List[str]:  # O(2^n), n is # of letters
    ans = [""]
    for c in s:
        ans = [x + cc for x in ans for cc in {c, c.swapcase()}]
    return ans

# LC567. Permutation in String - string permutation check - s1 is a permutation substring of s2
def checkInclusion(self, s1, s2):  # O(|s1|) time and O(1) space (26 chars as keys)
    d1, d2 = Counter(s1), Counter(s2[:len(s1)])
    for start in range(len(s1), len(s2)):
        if d1 == d2: return True
        d2[s2[start]] += 1
        d2[s2[start-len(s1)]] -= 1
        if d2[s2[start-len(s1)]] == 0:
            del d2[s2[start-len(s1)]]
    return d1 == d2

# LC383. Ransom Note
def canConstruct(self, ransomNote, magazine):  # O(m+n)
    return not collections.Counter(ransomNote) - collections.Counter(magazine)
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    magazine_counts = collections.Counter(magazine)
    ransom_note_counts = collections.Counter(ransomNote)
    for char, count in ransom_note_counts.items():
        if magazine_counts[char] < count: return False
    return True

# LC71. Simplify Path -  file paths, canonical path
def simplifyPath(self, path: str) -> str:  # O(n) runtime and space
    stack = []
    for folder in path.split('/'):
        if not folder or folder == '.': continue  # skip this
        elif folder == '..':
            if stack: stack.pop()  # go to parent
        else: stack.append(folder)
    return '/' + '/'.join(stack)

# LC389. Find the Difference
def findTheDifference(self, s: str, t: str) -> str:  # O(n) time and O(1) space
    c = 0
    for cs in s: c ^= ord(cs) #ord is ASCII value
    for ct in t: c ^= ord(ct)
    return chr(c) #chr = convert ASCII into character

# # LC408. Valid Word Abbreviation
def validWordAbbreviation(self, word, abbr):
    # turn "i12iz4n" to "i.{12}iz.{4}n$"
    pattern = re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$'
    return bool(re.match(pattern, word))
def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    wl = len(word)
    i, n = 0, "0"  # i is index in word
    for c in abbr:
        if c.isdigit():
            if n == c: return False  # don't allow abbr starts with 0
            n += c  # accumulate digit, "02"
        else:  # letter
            i += int(n)  # add counts for previous letter
            n = '0'  # reset counts to 0
            if i >= wl or word[i] != c: return False  # core logic
            i += 1  # move to next char
    return i + int(n) == wl

# LC767. Reorganize String - rearrange chars
def reorganizeString(self, s: str) -> str:
    if not s: return ""  # O(n) there is no sort
    n, counts = len(s), Counter(s)
    maxk, maxc = None, -1
    for k, c in counts.items(): # only max matters
        if c > maxc: maxk, maxc = k, c
    if maxc > (n+1) // 2: return ""  # we could have ababa
    res = [''] * n
    res[:maxc*2:2] = [maxk] * maxc
    # to continue fill in lower count chars. "bfrbs", if more lower freq chars
    i = maxc*2 if maxc * 2 < n else 1
    for k, c in counts.items():
        if k == maxk: continue
        for j in range(c):
            res[i] = k
            i += 2
            if i >= n: i = 1 # revert back to index 1 to fill odd
    return ''.join(res)

# LC1055. Shortest Way to Form String
def shortestWay(self, source, target):
    idxs = defaultdict(list)
    for i, c in enumerate(source): idxs[c].append(i)
    result, i = 0, 0  # i: next index of source to check
    for c in target:  # O(nlogm)
        if c not in idxs: return -1  # cannot make target if char not in source
        j = bisect.bisect_left(idxs[c], i)  # index in idxs[c] that is >= i
        if j == len(idxs[c]):           # wrap around to beginning of source
            result += 1
            j = 0
        i = idxs[c][j] + 1              # next index in source
    return result if i == 0 else result + 1     # add 1 for partial source



# LC2262. Total Appeal of A String
def appealSum(self, s: str) -> int:
    last = {}
    res = 0
    for i,c in enumerate(s):
        last[c] = i + 1
        res += sum(last.values())  # for each v, we have v strings of that key char.
    return res

# LC2062. Count Vowel Substrings of a String
def countVowelSubstrings(self, word: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    ans, last_consonant = 0, -1
    last_seen_vowels = {v: -2 for v in vowels}
    for i, x in enumerate(word):
        if x not in vowels:
            last_consonant = i
        else:
            last_seen_vowels[x] = i
            ans += max(min(last_seen_vowels.values())-last_consonant, 0)
    return ans

# LC2063. Vowels of All Substrings
def countVowels(self, s: str) -> int:
    # for each vowel c on i, there are 0...i for left, and n-i for right
    return sum((i + 1) * (len(s) - i) for i, c in enumerate(s) if c in 'aeiou')

# LC828. Count Unique Characters of All Substrings of a Given String
def uniqueLetterString(self, s: str) -> int:
    index = {c: [-1, -1] for c in ascii_uppercase}
    res = 0
    for i, c in enumerate(s):
        k, j = index[c]
        res += (i - j) * (j - k)
        index[c] = [j, i]
    for c in index:
        k, j = index[c]
        res += (len(s) - j) * (j - k)
    return res % (10**9 + 7)




# LC681. Next Closest Time
def nextClosestTime(self, time: str) -> str:
    hour, minute = time.split(":")  # 19:34
    # Generate all possible 2 digit values. There are at most 16 sorted values here
    nums = sorted(set(hour + minute))  # 1, 3, 4, 9
    two_digit_values = [a+b for a in nums for b in nums]  # 11, 13, 14,
    i = two_digit_values.index(minute)  # index is 6 for 34, next is 39
    if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "60":
        return hour + ":" + two_digit_values[i+1]
    i = two_digit_values.index(hour)
    if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "24":
        return two_digit_values[i+1] + ":" + two_digit_values[0]
    return two_digit_values[0] + ":" + two_digit_values[0]
def nextClosestTime1(self, time):
    return min((t <= time, t) for i in range(24 * 60) for t in ['%02d:%02d' % divmod(i, 60)]
                if set(t) <= set(time))[1]

# LC844. Backspace String Compare
def backspaceCompare(self, S: str, T: str) -> bool:  # O(n+m) in runtime and space
    def build(S):
        ans = []
        for c in S:
            if c != '#': ans.append(c)
            elif ans: ans.pop()
        return "".join(ans)
    return build(S) == build(T)
def backspaceCompare(self, S, T): # O(n+m) in runtime and O(1) space
    def F(S):  # iterator, O(1)
        skip = 0
        for x in reversed(S):  # reversed is an iterator, O(1)
            if x == '#': skip += 1
            elif skip: skip -= 1
            else: yield x
    return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))  # zip_longest is an iterator

# LC848. Shifting Letters
def shiftingLetters(self, s: str, shifts: List[int]) -> str:
    ans = []
    X = sum(shifts) % 26
    for i, c in enumerate(s):
        index = ord(c) - ord('a')
        ans.append(chr(ord('a') + (index + X) % 26))
        X = (X - shifts[i]) % 26
    return "".join(ans)


# LC161. One Edit Distance, return true if so
def isOneEditDistance(self, s, t):  # O(n) time and space
    if s == t: return False
    i = 0
    while i < min(len(s),len(t)):
        if s[i] == t[i]: i += 1
        else: break
    return s[i+1:] == t[i+1:] or s[i:] == t[i+1:] or s[i+1:]==t[i:]
def isOneEditDistance(self, s: 'str', t: 'str') -> 'bool':  # O(n) time and space
    ns, nt = len(s), len(t)
    if ns > nt: return self.isOneEditDistance(t, s)
    if nt - ns > 1: return False
    for i in range(ns):
        if s[i] != t[i]:
            if ns == nt: return s[i + 1:] == t[i + 1:]  # can be O(1) in space
            else: return s[i:] == t[i + 1:]  # can be O(1) in space
    return ns + 1 == nt

# LC468. Validate IP Address
def validIPAddress(self, IP: str) -> str:
    def isIPv4(s):
        try: return str(int(s)) == s and 0 <= int(s) <= 255  # prevent leading 0
        except: return False
    def isIPv6(s):
        try: return len(s) <= 4 and int(s, 16) >= 0 # hex
        except: return False
    segs = IP.split(".")
    if len(segs) == 4 and all(isIPv4(i) for i in segs): return "IPv4"
    segs = IP.split(":")
    if len(segs) == 8 and all(isIPv6(i) for i in segs): return "IPv6"
    return "Neither"

# LC1202. Smallest String With Swaps
def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    class UF:  ## O(n) space, O(n + mlogn) time, m = len(pairs)
        def __init__(self, n): self.p = list(range(n))
        def union(self, x, y): self.p[self.find(x)] = self.find(y)
        def find(self, x):
            if x != self.p[x]: self.p[x] = self.find(self.p[x])
            return self.p[x]
    uf, res, m = UF(len(s)), [], defaultdict(list)
    for x,y in pairs: uf.union(x,y)
    for i in range(len(s)): m[uf.find(i)].append(s[i])
    for comp_id in m.keys(): m[comp_id].sort(reverse=True)
    for i in range(len(s)): res.append(m[uf.find(i)].pop())
    return ''.join(res)

# LC884. Uncommon Words from Two Sentences
def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    c = collections.Counter((s1 + " " + s2).split())
    return [w for w in c if c[w] == 1]

# LC388. Longest Absolute File Path
def lengthLongestPath(self, input: str) -> int:
    ret, tmp = 0, {-1: 0}
    for line in input.split('\n'):
        depth = line.count('\t')
        # len(line) - depth -> remove tabs
        tmp[depth] = tmp[depth - 1] + len(line) - depth
        if line.count('.'):  # \n replaced by /
            ret = max(ret, tmp[depth] + depth)
    return ret

# LC1108. Defanging an IP Address
def defangIPaddr(self, address: str) -> str:
    return '[.]'.join(address.split('.'))

# LC833. Find And Replace in String
def findReplaceString(self, S, indexes, sources, targets):  # O(len(ops) * len(S))
    n, m = len(S), len(indexes)
    idxs = [[]] * n
    for i, s, t in zip(indexes, sources, targets):  # O(m)
        if S[i:i + len(s)] == s: idxs[i] = (s, t)
    for i in range(len(idxs))[::-1]:  # O(m)
        if idxs[i]:
            s, t = idxs[i]
            S = S[:i] + t + S[i + len(s):]  # O(n)
    return S

# LC345. Reverse Vowels of a String
def reverseVowels(self, s):
    s = list(s)  # take the vowel sequence, reverse it
    vows = set('aeiouAEIOU')
    l, r = 0, len(s) - 1
    while l < r:
        while l <= r and s[l] not in vows: l += 1
        while l <= r and s[r] not in vows: r -= 1
        if l > r: break
        s[l], s[r] = s[r], s[l]
        l, r = l + 1, r - 1
    return ''.join(s)

# LC72. Edit Distance - between 2 words
def minDistance(self, word1: str, word2: str) -> int:  # O(mn) time and space
    @lru_cache(None)  # O(mn) runtime and space
    def levenshtein(i, j):  # distance of word1[:i] and word2[:j]
        if i == 0: return j  # Need to insert j chars
        if j == 0: return i  # Need to delete i chars
        if word1[i-1] == word2[j-1]: return levenshtein(i-1, j-1)
        # delete or replace
        return min(levenshtein(i-1, j), levenshtein(i, j-1), levenshtein(i-1, j-1)) + 1
    return levenshtein(len(word1), len(word2))
def minDistance(self, word1: str, word2: str) -> int:  # O(mn) time and O(n) space
    # In the above, recursion relies only previous row, so we could save space
    n, m = len(word1), len(word2)
    if n == 0 or m == 0: return max(n, m)
    # dp(j) is the distance between word1[:0] and word2[:j]
    dp = [j for j in range(m+1)] # all inserts
    for i in range(1, n+1):
        prev = dp[0] # prev = dp[i-1][j-1], save before overwritten
        dp[0] = i # all deletes
        for j in range(1, m+1):
            tmp = dp[j] # save for next round
            if word1[i-1] == word2[j-1]: dp[j] = prev # no edit
            else:
                # try to add 1 char to one of both words
                # this update (make them same),
                # + prev=dp[i-1][j-1], new dp[j-1], and old dp[i-1][j]
                dp[j] = 1 + min(prev, dp[j-1], dp[j])
            prev = tmp
    return dp[-1]

# LC1790. Check if One String Swap Can Make Strings Equal
def areAlmostEqual(self, s1: str, s2: str) -> bool:
    diff = [[x, y] for x, y in zip(s1, s2) if x != y]
    return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]

# LC6. ZigZag Conversion - string zigzag
def convert(self, s: str, numRows: int) -> str:
    if numRows == 1: return s
    rows = [''] * numRows
    cur_row, down = 0, -1
    for c in s:
        rows[cur_row] += c
        if cur_row == 0 or cur_row == numRows-1:
            down *= -1
        cur_row += down
    return ''.join(rows)





# LC942. DI String Match
def diStringMatch(self, s: str) -> List[int]:
    lo, hi = 0, len(s)
    ans = []
    for x in s:
        if x == 'I':
            ans.append(lo)
            lo += 1
        else:
            ans.append(hi)
            hi -= 1
    return ans + [lo]

# LC28. Implement strStr() - index of needle in hay, KMP
def strStr(self, haystack: str, needle: str) -> int:
    if not needle: return 0  # '' or None
    if not haystack: return -1  # order matters, needle is not empty
    h_len, n_len = len(haystack), len(needle)
    for i in range(h_len - n_len + 1):
        if needle == haystack[i:i+n_len]: return i  # O(n^2)
    return -1
def strStr(self, haystack: str, needle: str) -> int:  # KMP, O(m + n)
    def createNeedleSuffixArr(needle):
        result = [0]*len(needle)
        i, j = 1, 0
        while i < len(needle):
            if needle[i] == needle[j]:
                result[i] = j + 1
                i += 1
                j += 1
            elif j > 0: j = result[j-1]
            else: i += 1
        return result
    if not needle: return 0
    if not haystack or len(haystack) < len(needle): return -1
    needleArr = createNeedleSuffixArr(needle)
    i = j = 0
    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        elif j > 0: j = needleArr[j-1]
        else: i += 1
    return i - j if j == len(needle) else -1

# LC1071. Greatest Common Divisor of Strings
def gcdOfStrings(self, str1: str, str2: str) -> str:
    # make sure that str1 and str2 must have `Greatest Common Divisor`
    if str1 + str2 != str2 + str1: return ''
    sz1, sz2 = len(str1), len(str2)
    while sz1 != 0 and sz2 != 0: # GCD
        if sz1 > sz2: sz1 = sz1 % sz2
        else: sz2 = sz2 % sz1
    return str1[:sz1] if sz1 else str2[:sz2]

# LC1247. Minimum Swaps to Make Strings Equal
def minimumSwap(self, s1: str, s2: str) -> int:
    # https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/discuss/419874/Simply-Simple-Python-Solution-with-detailed-explanation
    x_y, y_x = 0, 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if c1 == 'x': x_y += 1
            else: y_x += 1
    if (x_y + y_x) % 2 == 1: return -1
    # Both x_y and y_x count shall either be even or odd to get the result.
    # x_y + y_x should be even
    res = x_y // 2
    res += y_x // 2
    if x_y % 2 == 1: res += 2
    # If there count is odd i.e. we have "xy" and "yx" situation
    # so we need 2 more swaps to make them equal
    return res

# LC165. Compare Version Numbers
def compareVersion(self, version1: str, version2: str) -> int:
    nums1 = version1.split('.')
    nums2 = version2.split('.')
    n1, n2 = len(nums1), len(nums2)
    for i in range(max(n1, n2)): # compare versions
        i1 = int(nums1[i]) if i < n1 else 0
        i2 = int(nums2[i]) if i < n2 else 0
        if i1 != i2: return 1 if i1 > i2 else -1
    return 0 # the versions are equal

# LC1763. Longest Nice Substring
def longestNiceSubstring(self, s: str) -> str:
    if not s: return "" # boundary condition
    ss = set(s)
    for i, c in enumerate(s):
        if c.swapcase() not in ss:
            s0 = self.longestNiceSubstring(s[:i])
            s1 = self.longestNiceSubstring(s[i+1:])
            return max(s0, s1, key=len)
    return s

# LC763. Partition Labels - substring no repeating chars
def partitionLabels(self, s: str) -> List[int]: # O(n) time and space
    max_idx = {letter: i for i, letter in enumerate(s)}
    ret = []
    start = maxl = 0
    for i, e in enumerate(s):  # O(n) time
        maxl = max(maxl, max_idx[e])
        if maxl == i:
            ret.append(i - start + 1)
            start = i+1
    return ret



# LC1156. Swap For Longest Repeated Character Substring
def maxRepOpt1(self, S):
    # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
    A = [[c, len(list(g))] for c, g in itertools.groupby(S)]
    # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
    count = collections.Counter(S)
    # only extend 1 more, use min here to avoid the case that there's no extra char to extend
    res = max(min(k + 1, count[c]) for c, k in A)
    # merge 2 groups together
    for i in range(1, len(A) - 1):
        # if both sides have the same char and are separated by only 1 char
        if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
            # min here serves the same purpose
            res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
    return res

# LC1832. Check if the Sentence Is Pangram
def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

# LC859. Buddy Strings - swap 2 letters
def buddyStrings(self, A, B):
    if len(A) != len(B): return False
    if A == B and len(set(A)) < len(A): return True
    dif = [(a, b) for a, b in zip(A, B) if a != b]
    return len(dif) == 2 and dif[0] == dif[1][::-1]
