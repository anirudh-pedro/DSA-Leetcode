# 1233. Remove Sub-Folders from the Filesystem

## Problem Description

Given a list of folders `folder`, return the folders after removing all **sub-folders** in those folders. You may return the answer in any order.

If a `folder[i]` is located within another `folder[j]`, it is called a **sub-folder** of it. A sub-folder of `folder[j]` must start with `folder[j]`, followed by a **"/"**. For example, `"/a/b"` is a sub-folder of `"/a"`, but `"/b"` is not a sub-folder of `"/a/b/c"`.

The format of a path is one or more concatenated strings of the form: **'/'** followed by one or more lowercase English letters.

For example, `"/leetcode"` and `"/leetcode/problems"` are valid paths while an empty string and `"/"` are not.

## Examples

### Example 1:

```
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
```

**Explanation:**
Folders `"/a/b"` is a subfolder of `"/a"` and `"/c/d/e"` is inside of folder `"/c/d"` in our filesystem.

### Example 2:

```
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
```

**Explanation:**
Folders `"/a/b/c"` and `"/a/b/d"` will be removed because they are subfolders of `"/a"`.

### Example 3:

```
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
```

**Explanation:**
None of these folders are subfolders of each other.

## Constraints

- `1 <= folder.length <= 4 * 10^4`
- `2 <= folder[i].length <= 100`
- `folder[i]` contains only lowercase letters and `'/'`
- `folder[i]` always starts with the character `'/'`
- Each folder name is unique

## Solution

```python
class Trie:
    def __init__(self):
        self.child = {}  # Dictionary to store child nodes
        self.end = False  # Flag to mark end of a complete folder path

    def add(self, word):
        """Add a folder path to the Trie"""
        cur = self
        # Split path by '/' and traverse/create nodes
        for folder_name in word.split("/"):
            if folder_name not in cur.child:
                cur.child[folder_name] = Trie()
            cur = cur.child[folder_name]
        cur.end = True  # Mark end of complete path

    def search(self, path):
        """Check if path is NOT a subfolder of any existing folder"""
        cur = self
        folders = path.split("/")

        # Check all prefixes except the last folder
        for i in range(len(folders) - 1):
            cur = cur.child[folders[i]]
            # If we find a complete path before reaching the end,
            # this path is a subfolder
            if cur.end:
                return False

        return True  # Not a subfolder

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        trie = Trie()

        # Step 1: Add all folders to the Trie
        for folder_path in folder:
            trie.add(folder_path)

        # Step 2: Check each folder and keep only non-subfolders
        for folder_path in folder:
            if trie.search(folder_path):
                res.append(folder_path)

        return res
```

## Algorithm Explanation

This solution uses a **Trie (Prefix Tree)** to efficiently detect subfolder relationships:

### Step 1: Build Trie Structure

- Split each folder path by `"/"` to get individual folder names
- Insert each path into the Trie, marking the end of complete paths
- Each node represents a folder, and `end=True` indicates a complete folder path

### Step 2: Detect Subfolders

- For each folder, traverse the Trie following its path
- If we encounter a node with `end=True` before reaching the final folder, it means this path is a subfolder
- Only include folders that are NOT subfolders in the result

### Trie Structure Example

For folders `["/a", "/a/b", "/c/d"]`:

```
Root
├── "" (empty from split)
    ├── "a" (end=True) ✓ Complete path "/a"
    │   └── "b" (end=True) ✓ Complete path "/a/b"
    └── "c"
        └── "d" (end=True) ✓ Complete path "/c/d"
```

## Step-by-Step Example (folder = ["/a", "/a/b", "/c/d"])

### Building Trie:

| Folder | Split Result   | Trie Path             | End Marker     |
| ------ | -------------- | --------------------- | -------------- |
| "/a"   | ["", "a"]      | Root → "" → "a"       | "a".end = True |
| "/a/b" | ["", "a", "b"] | Root → "" → "a" → "b" | "b".end = True |
| "/c/d" | ["", "c", "d"] | Root → "" → "c" → "d" | "d".end = True |

### Searching for Subfolders:

| Folder | Search Path    | Check Prefixes | Is Subfolder?    | Include? |
| ------ | -------------- | -------------- | ---------------- | -------- |
| "/a"   | ["", "a"]      | Check: ""      | "" not end       | ✓ Keep   |
| "/a/b" | ["", "a", "b"] | Check: "", "a" | "a" has end=True | ✗ Remove |
| "/c/d" | ["", "c", "d"] | Check: "", "c" | Neither has end  | ✓ Keep   |

**Result**: `["/a", "/c/d"]`

## Why Split by "/" Works

### Path Structure:

- All paths start with `"/"`, so `split("/")` always gives `["", ...]`
- This creates a consistent root structure in the Trie
- Example: `"/a/b"` → `["", "a", "b"]`

### Prefix Checking:

- To check if `"/a/b/c"` is a subfolder, we examine prefixes:
  - `"/a"` (check if this exists as complete path)
  - `"/a/b"` (check if this exists as complete path)
- If any prefix is a complete path, current path is a subfolder

## Time and Space Complexity

- **Time Complexity**: O(N × M)
  - N = number of folders
  - M = average length of folder paths
  - Building Trie: O(N × M)
  - Searching: O(N × M)
- **Space Complexity**: O(N × M) for the Trie structure

## Key Insights

1. **Trie Advantage**: Efficiently stores and searches hierarchical path structures
2. **Prefix Detection**: Subfolders are detected by finding complete paths in prefixes
3. **Path Splitting**: Using `split("/")` naturally creates the folder hierarchy
4. **End Markers**: `end=True` distinguishes complete paths from intermediate nodes
5. **Two-Pass Algorithm**: Build structure first, then query for relationships

## Why This Approach Works

- **Hierarchical Storage**: Trie naturally represents folder hierarchy
- **Efficient Prefix Queries**: Can quickly check if any prefix is a complete folder
- **Exact Matching**: Split by `"/"` ensures exact folder name matching
- **Complete Path Tracking**: `end` flag distinguishes between intermediate and complete paths

## Alternative Approaches

1. **Sorting + Linear Scan**: O(N log N + N×M) - sort paths and check adjacent ones
2. **Set-based Prefix Check**: O(N²×M) - for each folder, check all possible prefixes
3. **Nested Loop Comparison**: O(N²×M) - compare every pair of folders

## Edge Cases Handled

1. **Similar Prefixes**: `"/a/b"` vs `"/a/bc"` (not a subfolder relationship)
2. **Multiple Levels**: `"/a/b/c/d"` with parent `"/a"`
3. **No Subfolders**: All folders are independent
4. **Single Character**: Paths like `"/a"`, `"/b"`

## Optimization Notes

The Trie approach is optimal for this problem because:

- **Reusable Structure**: Once built, can query multiple paths efficiently
- **Space Sharing**: Common prefixes share nodes in the Trie
- **Natural Hierarchy**: Mirrors the actual filesystem structure

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754154211/Screenshot_2025-08-02_223313_c2uvxj.png)
