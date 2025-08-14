# 179. Largest Number

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Array](https://img.shields.io/badge/Topic-Array-blue)
![Sorting](https://img.shields.io/badge/Topic-Sorting-green)
![String](https://img.shields.io/badge/Topic-String-purple)

## Problem Description

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

## Examples

### Example 1:

```
Input: nums = [10,2]
Output: "210"
```

### Example 2:

```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```

## Constraints

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 10^9

## Solution

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,j in enumerate(nums):
            nums[i] = str(j)
        def compare(a,b):
            return (a+b < b+a) - (a+b > b+a)
        nums = sorted(nums,key = cmp_to_key(compare))
        return str(int("".join(nums)))
```

## Algorithm Explanation

The solution uses **custom sorting** with a special comparator:

1. **String Conversion**: Convert all numbers to strings for concatenation comparison
2. **Custom Comparator**: Compare two strings `a` and `b` by checking which concatenation is larger
   - Compare `a+b` vs `b+a` (e.g., "30"+"3" vs "3"+"30" → "303" vs "330")
3. **Sorting Logic**: If `a+b < b+a`, then `b` should come before `a` in the final arrangement
4. **Result Construction**: Join all sorted strings and convert back through int to handle edge cases like leading zeros

### Key Insight

- The problem is about finding the optimal arrangement, not the largest individual numbers
- Custom comparator `(a+b < b+a) - (a+b > b+a)` returns -1, 0, or 1 for proper sorting
- Converting to int and back to string handles the edge case where all numbers are 0

## Complexity Analysis

- **Time Complexity**: O(n log n × m) where n is the number of elements and m is the average length of strings
  - Sorting takes O(n log n) comparisons, each comparison takes O(m) time
- **Space Complexity**: O(n × m) for storing the string representations

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755155121/Screenshot_2025-08-14_123510_a0vcq0.png)
