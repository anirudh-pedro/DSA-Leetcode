# 735. Asteroid Collision

## Problem Description

We are given an array `asteroids` of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the **absolute value** represents its **size**, and the **sign** represents its **direction** (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Examples

### Example 1:

```
Input: asteroids = [5,10,-5]
Output: [5,10]
```

**Explanation:**
The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

### Example 2:

```
Input: asteroids = [8,-8]
Output: []
```

**Explanation:**
The 8 and -8 collide exploding each other.

### Example 3:

```
Input: asteroids = [10,2,-5]
Output: [10]
```

**Explanation:**
The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

## Constraints

- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

## Solution

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            # Add current asteroid to stack
            stack.append(asteroids[i])

            # Check for collisions: right-moving asteroid followed by left-moving asteroid
            while len(stack) > 1 and (stack[-1] < 0 and stack[-2] > 0):
                left_asteroid = stack[-2]   # Moving right (positive)
                right_asteroid = stack[-1]  # Moving left (negative)

                # Compare sizes (absolute values)
                if abs(right_asteroid) == abs(left_asteroid):
                    # Same size: both explode
                    stack.pop()  # Remove right asteroid
                    stack.pop()  # Remove left asteroid
                elif abs(right_asteroid) > abs(left_asteroid):
                    # Right asteroid is larger: left asteroid explodes
                    stack.pop(-2)  # Remove left asteroid (second to last)
                elif abs(right_asteroid) < abs(left_asteroid):
                    # Left asteroid is larger: right asteroid explodes
                    stack.pop()  # Remove right asteroid (last)

        return stack
```

## Algorithm Explanation

This solution uses a **stack-based simulation** to handle asteroid collisions:

### Step 1: Process Each Asteroid

- Add each asteroid to the stack sequentially
- After adding each asteroid, check for potential collisions

### Step 2: Collision Detection

- Collisions only occur when:
  - A **right-moving asteroid** (positive) is followed by a **left-moving asteroid** (negative)
  - Condition: `stack[-2] > 0 and stack[-1] < 0`

### Step 3: Collision Resolution

Based on the sizes (absolute values) of the colliding asteroids:

1. **Equal Size**: Both asteroids explode → Remove both from stack
2. **Left-moving is Larger**: Right-moving asteroid explodes → Remove the positive asteroid
3. **Right-moving is Larger**: Left-moving asteroid explodes → Remove the negative asteroid

### Step 4: Continuous Collision Handling

- Use a `while` loop to handle chain reactions
- After each collision, check if new collisions are possible
- Continue until no more collisions can occur

## Step-by-Step Example (asteroids = [10,2,-5])

| Step | Current | Stack After Adding | Collision Check | Action               | Final Stack |
| ---- | ------- | ------------------ | --------------- | -------------------- | ----------- |
| 1    | 10      | [10]               | No collision    | -                    | [10]        |
| 2    | 2       | [10,2]             | No collision    | -                    | [10,2]      |
| 3    | -5      | [10,2,-5]          | 2 > 0, -5 < 0   | 2 vs 5: 2 explodes   | [10,-5]     |
| 4    | -       | [10,-5]            | 10 > 0, -5 < 0  | 10 vs 5: -5 explodes | [10]        |

Final Result: **[10]**

## Collision Scenarios

### Case 1: No Collision

- `[+, +]`: Both moving right → No collision
- `[-, -]`: Both moving left → No collision
- `[-, +]`: Left moving left, right moving right → Moving apart

### Case 2: Collision Occurs

- `[+, -]`: Left moving right, right moving left → **Collision!**

## Time and Space Complexity

- **Time Complexity**: O(n) - Each asteroid is pushed and popped at most once
- **Space Complexity**: O(n) - Stack can contain all asteroids in worst case

## Key Insights

1. **Stack Simulation**: Stack naturally handles the sequential processing and collision detection
2. **Collision Condition**: Only `[positive, negative]` pairs can collide
3. **Chain Reactions**: One collision can trigger multiple subsequent collisions
4. **Greedy Processing**: Process asteroids left to right, handling collisions immediately
5. **State Management**: Stack maintains the current state after each collision

## Why This Approach Works

- **Sequential Processing**: Asteroids are processed in order, simulating time progression
- **Immediate Collision Resolution**: Handle collisions as soon as they're detected
- **Chain Reaction Handling**: The while loop ensures all cascading collisions are resolved
- **Efficient State Tracking**: Stack naturally maintains the current asteroid configuration

## Edge Cases Handled

1. **No Collisions**: All same direction asteroids
2. **Complete Annihilation**: All asteroids destroy each other
3. **Chain Reactions**: Multiple consecutive collisions
4. **Mixed Scenarios**: Combination of collisions and survivals

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1753540479/Screenshot_2025-07-26_200300_j6c7wd.png)
