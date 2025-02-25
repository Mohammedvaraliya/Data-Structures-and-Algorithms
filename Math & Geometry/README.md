# Math & Geometry Data-Structures and Algorithms

## 01. Rotate Image

[Leetcode Problem URL](https://leetcode.com/problems/rotate-image/description/)

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

Example 1:
![matrix 1](assets/mat1.jpg)

```bash
Input: matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

Output: [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]
```

Example 2:
![matrix 2](assets/mat2.jpg)

```bash
Input: matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

Output: [
    [15,13,2,5],
    [14,3,4,1],
    [12,6,8,9],
    [16,7,10,11]
]
```

Example 3:
![matrix 3](assets/mat3.avif)

```bash
Input: matrix = [
    [1,2],
    [3,4]
]

Output: [
    [3,1],
    [4,2]
]
```

### Explanation

To rotate the matrix by 90 degrees clockwise in-place, we can use a **layer-by-layer rotation** approach. This involves rotating the matrix in layers, starting from the outermost layer and moving inward.

#### Why This Approach?

1. **In-Place Rotation**: The problem requires modifying the matrix in-place, so we cannot use extra space for another matrix. This approach ensures that we only use constant extra space.

2. **Efficient and Intuitive**: By rotating the matrix layer by layer, we can systematically handle each element without complex calculations.

3. **Scalable**: This approach works efficiently for matrices of any size `n x n`.

#### Steps

1. Step 1: Understand the Layers

   - For an `n x n` matrix, there are `n//2` layers. For example:
   - A `3x3` matrix has 1 layer.
   - A `4x4` matrix has 2 layers.

2. Step 2: Rotate Each Layer

   - For each layer, perform a **four-way swap** of elements:

   1. Move the top-left element to the top-right position.
   2. Move the top-right element to the bottom-right position.
   3. Move the bottom-right element to the bottom-left position.
   4. Move the bottom-left element to the top-left position.

3. Step 3: Implement the Rotation

   - Use two pointers, `l` (left) and `r` (right), to track the boundaries of the current layer.
   - For each layer, iterate through the elements and perform the four-way swap.

#### Example Walkthrough

Let’s walk through **Example 1** step by step:

1. **Input**: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`

1. **Initialize**:

   - `l = 0`, `r = 2` (since the matrix is `3x3`).

1. **Rotate the Outer Layer**:

   - **First Iteration** (`i = 0`):
     - Save the top-left element: `topLeft = matrix[0][0] = 1`.
     - Move bottom-left to top-left: `matrix[0][0] = matrix[2][0] = 7`.
     - Move bottom-right to bottom-left: `matrix[2][0] = matrix[2][2] = 9`.
     - Move top-right to bottom-right: `matrix[2][2] = matrix[0][2] = 3`.
     - Move saved top-left to top-right: `matrix[0][2] = topLeft = 1`.
     - Updated matrix:
       ```
       [7,2,1],
       [4,5,6],
       [9,8,3]
       ```
   - **Second Iteration** (`i = 1`):
     - Save the top-middle element: `topLeft = matrix[0][1] = 2`.
     - Move bottom-middle to top-middle: `matrix[0][1] = matrix[1][0] = 4`.
     - Move bottom-right-middle to bottom-middle: `matrix[1][0] = matrix[2][1] = 8`.
     - Move top-right-middle to bottom-right-middle: `matrix[2][1] = matrix[1][2] = 6`.
     - Move saved top-middle to top-right-middle: `matrix[1][2] = topLeft = 2`.
     - Updated matrix:
       ```
       [7,4,1],
       [8,5,2],
       [9,6,3]
       ```

1. **Result**:

   - The matrix is now rotated 90 degrees clockwise.

1. **Output**: `[[7,4,1],[8,5,2],[9,6,3]]`

#### Time and Space Complexity

1. Time Complexity

   - **Outer Loop**: The outer loop runs for `n//2` layers.
   - **Inner Loop**: For each layer, the inner loop runs for `n - 2*layer` elements.
   - **Overall Time Complexity**: $O(n^2)$, where `n` is the size of the matrix.

2. Space Complexity

   - **In-Place Modification**: The algorithm uses only constant extra space.
   - **Overall Space Complexity**: `O(1)`.

#### Why This Approach is Efficient

1. **In-Place Rotation**: The algorithm modifies the matrix in-place, satisfying the problem's constraints.
2. **Layer-by-Layer Rotation**: By rotating the matrix layer by layer, the solution is intuitive and easy to implement.
3. **Optimal Time Complexity**: The time complexity of $O(n^2)$ is optimal for this problem since we must touch every element of the matrix.

---

---

## 02. Spiral Matrix

[Leetcode Problem URL](https://leetcode.com/problems/spiral-matrix/description/)

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

Example 1:

![spiral1](assets/spiral1.jpg)

```bash
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

Example 2:

![spiral2](assets/spiral.jpg)

```bash
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

### Explanation

To solve this problem, we can use a **layer-by-layer traversal** approach. This involves traversing the matrix in layers, starting from the outermost layer and moving inward. For each layer, we traverse the top row, right column, bottom row, and left column in order.

#### Why This Approach?

1. **Intuitive and Systematic**: The layer-by-layer approach ensures that we cover all elements of the matrix in a systematic and intuitive manner.
2. **Efficient**: This approach avoids unnecessary computations and ensures that each element is visited exactly once.
3. **Scalable**: The solution works efficiently for matrices of any size `m x n`.

#### Step-by-Step Explanation

1. Step 1: Define Boundaries

   - Use four boundaries to represent the current layer:
   - `left`: Leftmost column of the current layer.
   - `right`: Rightmost column of the current layer.
   - `top`: Topmost row of the current layer.
   - `bottom`: Bottommost row of the current layer.

2. Step 2: Traverse the Matrix in Spiral Order

   - While `left < right` and `top < bottom`:
     1. **Traverse the top row**: Move from `left` to `right` and add elements to the result.
     2. **Traverse the right column**: Move from `top + 1` to `bottom` and add elements to the result.
     3. **Traverse the bottom row**: If `top < bottom`, move from `right - 1` to `left` and add elements to the result.
     4. **Traverse the left column**: If `left < right`, move from `bottom - 1` to `top + 1` and add elements to the result.
   - After traversing a layer, update the boundaries to move to the next inner layer.

3. Step 3: Handle Edge Cases

   - If the matrix has only one row or one column, ensure that the traversal does not revisit elements.

#### Example Walkthrough

Let’s walk through **Example 1** step by step:

1. **Input**: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`

1. **Initialize Boundaries**:

   - `left = 0`, `right = 3` (number of columns).
   - `top = 0`, `bottom = 3` (number of rows).
   - `res = []` (to store the result).

1. **First Layer**:

   - **Traverse the top row**:
     - Add elements from `matrix[0][0]` to `matrix[0][2]`: `[1, 2, 3]`.
     - Update `res = [1, 2, 3]`.
     - Increment `top` to `1`.
   - **Traverse the right column**:
     - Add elements from `matrix[1][2]` to `matrix[2][2]`: `[6, 9]`.
     - Update `res = [1, 2, 3, 6, 9]`.
     - Decrement `right` to `2`.
   - **Traverse the bottom row**:
     - Add elements from `matrix[2][1]` to `matrix[2][0]`: `[8, 7]`.
     - Update `res = [1, 2, 3, 6, 9, 8, 7]`.
     - Decrement `bottom` to `2`.
   - **Traverse the left column**:
     - Add element `matrix[1][0]`: `[4]`.
     - Update `res = [1, 2, 3, 6, 9, 8, 7, 4]`.
     - Increment `left` to `1`.

1. **Second Layer**:

   - **Traverse the top row**:
     - Add element `matrix[1][1]`: `[5]`.
     - Update `res = [1, 2, 3, 6, 9, 8, 7, 4, 5]`.
     - Increment `top` to `2`.
   - **Traverse the right column**:
     - No elements to add (since `top == bottom`).
   - **Traverse the bottom row**:
     - No elements to add (since `left == right`).
   - **Traverse the left column**:
     - No elements to add (since `top == bottom`).

1. **Result**:

   - The spiral order traversal is `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

1. **Output**: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

#### Time Complexity

- **Traversal**: Each element of the matrix is visited exactly once.
- **Overall Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns.

#### Space Complexity

- We use an additional list `res` to store the output.
- The worst-case space usage is `O(m × n)` (for the output).
- No extra data structures are used, so `O(1)` auxiliary space.

#### Why This Approach is Efficient

1. **Optimal Traversal**: Each element is visited exactly once, ensuring optimal time complexity.
2. **In-Place Boundaries**: The boundaries are updated in-place, avoiding the need for extra data structures.
3. **Scalable**: The solution works efficiently for matrices of any size.

---

---
