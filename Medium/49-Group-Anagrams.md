# 49. Group Anagrams

**Difficulty:** Medium  
**Topics:** Array, Hash Table, String, Sorting  
**Companies:** Amazon, Facebook, Uber

## Problem Description

Given an array of strings `strs`, **group the anagrams together**. You can return the answer in any order.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

### Example 1:

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
```

### Example 2:

```
Input: strs = [""]
Output: [[""]]
```

### Example 3:

```
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters

## Solution

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to group anagrams by their sorted character signature
        anagram_groups = defaultdict(list)

        # Process each string in the input array
        for string in strs:
            # Create a signature by sorting characters
            # Anagrams will have the same sorted signature
            sorted_chars = sorted(string)
            signature = "".join(sorted_chars)

            # Group strings with the same signature
            anagram_groups[signature].append(string)

        # Return all groups as a list of lists
        return list(anagram_groups.values())
```

## Algorithm Explanation

This solution uses **hash table grouping with character sorting** as the key strategy:

### Key Insight

- **Anagram Property**: Two strings are anagrams if they contain the same characters with the same frequency
- **Sorting Signature**: When we sort the characters of anagrams, they produce identical strings
- **Hash Grouping**: Use the sorted string as a key to group anagrams together

### Step-by-Step Process

1. **Initialize Hash Map**: Create a defaultdict to automatically handle new keys
2. **Process Each String**: For every string in the input array:
   - Sort its characters to create a unique signature
   - Use this signature as the key in our hash map
   - Add the original string to the list of values for this key
3. **Extract Groups**: Return all value lists from the hash map

### Example Walkthrough

For input `["eat","tea","tan","ate","nat","bat"]`:

| String | Sorted Signature | Hash Map State                                                        |
| ------ | ---------------- | --------------------------------------------------------------------- |
| "eat"  | "aet"            | {"aet": ["eat"]}                                                      |
| "tea"  | "aet"            | {"aet": ["eat", "tea"]}                                               |
| "tan"  | "ant"            | {"aet": ["eat", "tea"], "ant": ["tan"]}                               |
| "ate"  | "aet"            | {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}                        |
| "nat"  | "ant"            | {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}                 |
| "bat"  | "abt"            | {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"], "abt": ["bat"]} |

**Final Result**: `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

## Complexity Analysis

- **Time Complexity:** `O(n × m log m)` where n is the number of strings and m is the average length
  - For each string, we perform sorting which takes O(m log m)
  - We do this for n strings
- **Space Complexity:** `O(n × m)` for storing all strings in the hash map

## Key Insights

1. **Sorting as Canonical Form**: Sorting creates a unique identifier for anagram groups
2. **Hash Map Efficiency**: O(1) average lookup and insertion for grouping
3. **Automatic Grouping**: defaultdict eliminates the need for key existence checks
4. **Preserve Original Strings**: We store original strings, not their sorted versions

## Edge Cases

- **Empty String**: Handled naturally (empty string sorts to empty string)
- **Single Character**: Each unique character forms its own group
- **All Same Characters**: All strings with same character set group together
- **No Anagrams**: Each string forms its own group

## Alternative Approaches

1. **Character Count Array**: Use fixed-size array for character frequencies (faster for short strings)
2. **Prime Number Encoding**: Assign prime numbers to each character and use product as key
3. **Custom Hash Function**: Create hash based on character frequencies

![Anagram Grouping Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754318087/Screenshot_2025-08-04_200434_kevxny.png)
