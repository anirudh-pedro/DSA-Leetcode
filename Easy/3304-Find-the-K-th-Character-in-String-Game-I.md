# 3304. Find the K-th Character in String Game I

## Problem Description

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a positive integer `k`.

Now Bob will ask Alice to perform the following operation forever:

**Generate a new string by changing each character in `word` to its next character in the English alphabet, and append it to the original word.**

For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the **k-th character** in `word`, after enough operations have been done for `word` to have at least `k` characters.

**Note**: The character `'z'` can be changed to `'a'` in the operation.

## Examples

### Example 1:

```
Input: k = 5
Output: "b"
```

**Explanation:**
Initially, `word = "a"`. We need to do the operation three times:

1. Generated string is `"b"`, word becomes `"ab"`
2. Generated string is `"bc"`, word becomes `"abbc"`
3. Generated string is `"bccd"`, word becomes `"abbcbccd"`

The 5th character is `"b"`.

### Example 2:

```
Input: k = 10
Output: "c"
```

## Constraints

- `1 <= k <= 500`

## Solution

```python
class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'
        while len(s) < k:
            d = ""
            for i in s:
                if i == 'z':
                    d += 'a'
                    continue
                d += chr(ord(i) + 1)
            s += d
        return s[k - 1]
```

## Algorithm Explanation

This solution uses a **simulation approach** to build the string step by step:

### Step 1: Initialize

- Start with the initial string `s = "a"`
- Continue the process until the string length is at least `k`

### Step 2: Generate Next Characters

- For each character in the current string:
  - If the character is `'z'`, wrap around to `'a'`
  - Otherwise, increment to the next character using `chr(ord(i) + 1)`
- Build the new string `d` with all transformed characters

### Step 3: Append and Repeat

- Append the generated string `d` to the original string `s`
- Repeat until `len(s) >= k`

### Step 4: Return Result

- Return the character at index `k-1` (0-indexed)

## Step-by-Step Example (k = 5)

| Iteration | Current String | Generated String | New String |
| --------- | -------------- | ---------------- | ---------- |
| 0         | "a"            | "b"              | "ab"       |
| 1         | "ab"           | "bc"             | "abbc"     |
| 2         | "abbc"         | "bccd"           | "abbcbccd" |

Result: `s[4] = "b"`

## Time and Space Complexity

- **Time Complexity**: O(k) - In the worst case, we need to generate a string of length k, and each character is processed once
- **Space Complexity**: O(k) - We store the string which can grow up to approximately 2k characters

## Key Insights

1. **Simulation Strategy**: Direct simulation is efficient given the small constraint (k ≤ 500)
2. **Character Transformation**: Use ASCII values with `ord()` and `chr()` for easy character manipulation
3. **Wrap-around Logic**: Handle the special case where `'z'` becomes `'a'`
4. **Growth Pattern**: The string doubles in size with each iteration, so we reach length k quickly

## Alternative Approach

For larger constraints, we could use bit manipulation to find the k-th character without building the entire string, but given k ≤ 500, the simulation approach is perfectly efficient.

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1751560905/Screenshot_2025-07-03_221118_y6xjyb.png)
