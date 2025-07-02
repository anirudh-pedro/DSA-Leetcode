# 33. Search in Rotated Sorted Array

## Problem Description

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (1 <= k < nums.length) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with **O(log n)** runtime complexity.

## Examples

### Example 1:

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### Example 2:

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

### Example 3:

```
Input: nums = [1], target = 0
Output: -1
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique
- `nums` is an ascending array that is possibly rotated
- `-10^4 <= target <= 10^4`

## Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Step 1: Find the pivot point (smallest element)
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        # Step 2: Binary search helper function
        def binaryp(left, right):
            while left <= right:
                m = (left + right) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    left = m + 1
                else:
                    right = m - 1
            return -1

        # Step 3: Determine which half to search
        if nums[l] <= target <= nums[-1]:
            return binaryp(l, len(nums) - 1)
        else:
            return binaryp(0, l - 1)
```

## Algorithm Explanation

This solution uses a **two-step approach** to achieve O(log n) time complexity:

### Step 1: Find the Pivot Point

- Use binary search to find the rotation point (the index of the smallest element)
- Compare `nums[mid]` with `nums[right]`:
  - If `nums[mid] > nums[right]`, the pivot is in the right half
  - Otherwise, the pivot is in the left half (including mid)
- After this loop, `l` points to the smallest element (pivot)

### Step 2: Determine Search Range

- The array is effectively split into two sorted subarrays:
  - Left subarray: `nums[0]` to `nums[l-1]`
  - Right subarray: `nums[l]` to `nums[n-1]`
- Check which subarray contains the target:
  - If `nums[l] <= target <= nums[-1]`, search in the right subarray
  - Otherwise, search in the left subarray

### Step 3: Binary Search

- Perform standard binary search on the determined subarray
- Return the index if found, otherwise return -1

## Time and Space Complexity

- **Time Complexity**: O(log n) - Two binary searches
- **Space Complexity**: O(1) - Only using constant extra space

## Key Insights

1. **Rotated Array Property**: A rotated sorted array consists of two sorted subarrays
2. **Pivot Finding**: The pivot can be found using binary search by comparing with the rightmost element
3. **Range Determination**: Once we know the pivot, we can determine which sorted subarray contains our target
4. **Standard Binary Search**: Apply regular binary search on the correct subarray

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1751475644/Screenshot_2025-07-02_220727_iuqupo.png)
