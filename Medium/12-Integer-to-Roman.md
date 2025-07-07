# 12. Integer to Roman

## Problem Description

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

1. **Standard Form**: If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

2. **Subtractive Form**: If the value starts with 4 or 9, use the subtractive form representing one symbol subtracted from the following symbol. For example:

   - 4 is 1 (I) less than 5 (V): **IV**
   - 9 is 1 (I) less than 10 (X): **IX**
   - Only these subtractive forms are used: **4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), 900 (CM)**

3. **Repetition Rule**: Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times. You cannot append 5 (V), 50 (L), or 500 (D) multiple times.

Given an integer, convert it to a Roman numeral.

## Examples

### Example 1:

```
Input: num = 3749
Output: "MMMDCCXLIX"
```

**Explanation:**

- 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
- 700 = DCC as 500 (D) + 100 (C) + 100 (C)
- 40 = XL as 10 (X) less of 50 (L)
- 9 = IX as 1 (I) less of 10 (X)

**Note:** 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places.

### Example 2:

```
Input: num = 58
Output: "LVIII"
```

**Explanation:**

- 50 = L
- 8 = VIII

### Example 3:

```
Input: num = 1994
Output: "MCMXCIV"
```

**Explanation:**

- 1000 = M
- 900 = CM
- 90 = XC
- 4 = IV

## Constraints

- `1 <= num <= 3999`

## Solution

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # Define value-symbol pairs in descending order
        # Include both standard and subtractive forms
        d = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        res = ""

        # Process each value-symbol pair
        for value, symbol in d:
            if num // value:  # If current value fits into num
                count = num // value  # How many times it fits
                res += (symbol * count)  # Add symbols to result
                num = num % value  # Update remaining number

        return res
```

## Algorithm Explanation

This solution uses a **greedy approach** with a predefined mapping of values to Roman symbols:

### Step 1: Create Value-Symbol Mapping

- Define all possible Roman numeral values in **descending order**
- Include both standard symbols (M, D, C, L, X, V, I) and subtractive forms (CM, CD, XC, XL, IX, IV)
- This handles all edge cases including 4, 9, 40, 90, 400, 900

### Step 2: Greedy Conversion

- For each value-symbol pair (starting from largest):
  - Calculate how many times the value fits into the remaining number
  - Append the corresponding symbols to the result
  - Subtract the used value from the number

### Step 3: Continue Until Complete

- Process all pairs until the number becomes 0
- The greedy approach works because Roman numerals follow a positional system

## Step-by-Step Example (num = 1994)

| Step | Current Num | Value | Symbol | Count | Result    | Remaining |
| ---- | ----------- | ----- | ------ | ----- | --------- | --------- |
| 1    | 1994        | 1000  | M      | 1     | "M"       | 994       |
| 2    | 994         | 900   | CM     | 1     | "MCM"     | 94        |
| 3    | 94          | 90    | XC     | 1     | "MCMXC"   | 4         |
| 4    | 4           | 4     | IV     | 1     | "MCMXCIV" | 0         |

Final Result: **"MCMXCIV"**

## Time and Space Complexity

- **Time Complexity**: O(1) - Fixed number of value-symbol pairs (13 pairs max)
- **Space Complexity**: O(1) - Constant space for the mapping and result string

## Key Insights

1. **Greedy Strategy**: Always use the largest possible value first
2. **Predefined Mapping**: Include subtractive forms to handle edge cases elegantly
3. **Descending Order**: Process from largest to smallest values
4. **Integer Division**: Use `//` to count occurrences and `%` for remainder
5. **No Backtracking**: Greedy choice is always optimal for Roman numerals

## Why This Approach Works

- Roman numerals follow a **positional system** where larger values come first
- **Subtractive forms** (IV, IX, XL, XC, CD, CM) are exceptions that we handle explicitly
- The **greedy approach** is optimal because once we use a symbol, we never need to "undo" that choice
- By including all possible values (including subtractive forms), we ensure the shortest representation

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1751900702/Screenshot_2025-07-07_203416_emitlo.png)
