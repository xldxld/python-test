
2's compliment:
```-x = ~x + 1```

XOR
```a ^ b = 0 if a == b else 1 ```

Properties:  
```
n ^ n = 0
n ^ 0 = n
n ^ 1 = n-1 if n is odd or n+1 if n is even
```

### Right Most Bit 
Given x, (x-1) will have all the bits same as x, except for the rightmost 1 in x 
and all the bits to the right of the rightmost 1.  
```110 & 101 = 100 for 6 & (6-1) = 4```

To check whether x is a power of 2:
```x & (x-1) == 0```

To count number of 1's in x: (O(k), worst is O(logn))
```
def ones(n):
    cnt = 0
    while n:
        n = n & (n-1) # this erases the rightmost bit to 0.
        cnt += 1
    return cnt
```
Both ```x & (-x)``` and ```x ^ ( x & (x-1) )``` gives the right most bit

### Most Significant Bit
For given x, to get MSB we fill 1's to x by n | (n >> 2 ** i) for i in 0 ... 6
```
def msb(n):
    for i in range(6): # for 64 bits
        n = n | (n >> 2 ** i)
    return (n+1) >> 1
```

x = x ^ 1 ^ 1  # flip

### References:
- https://hackernoon.com/xor-the-magical-bit-wise-operator-24d3012ed821
- https://www.hackerearth.com/practice/notes/bit-manipulation/

