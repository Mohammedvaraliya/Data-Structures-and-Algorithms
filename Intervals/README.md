# Intervals Data-Structures and Algorithms

## 01. Insert Interval

[Leetcode Problem URL](https://leetcode.com/problems/insert-interval/description/)

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represents the start and the end time of the `ith` interval. `intervals` is initially sorted in ascending order by `start_i`.

You are given another interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and also `intervals` still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return `intervals` after adding `newInterval`.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

```bash
Example 1:

Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
Output: [[1,6]]
```

```bash
Example 2:

Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
Output: [[1,2],[3,5],[6,7],[9,10]]
```

### Explanation

This problem can be efficiently solved using a greedy approach by iterating through the given intervals and handling each interval in one of the following ways:

1. **Before Overlap**: If the new interval ends before the current interval starts, we add the new interval to the result and append all remaining intervals as they are.
2. **After Overlap**: If the new interval starts after the current interval ends, we add the current interval to the result and continue.
3. **Overlap**: If there is any overlap between the new interval and the current interval, we merge them by updating the start of the new interval to the minimum of both starts and the end of the new interval to the maximum of both ends. This merging process continues as long as the intervals overlap.

Once all intervals have been processed, we append the merged or updated new interval to the result list.

#### Why this Approach?

I've chose this greedy approach because it allows us to handle each interval in a single pass, ensuring an efficient solution. By merging intervals as we encounter overlaps, we maintain a simple structure without having to backtrack or reorder intervals. This results in a clean and efficient `O(n)` solution.

Other approaches, such as sorting and merging separately, could introduce unnecessary complexity and time overhead (`O(n log n)`), which is not needed since the input intervals are already sorted.

#### Example Walkthrough:

Let's walk through the example `intervals = [[1,3], [4,6]]`, `newInterval = [2,5]`:

1. **First Interval** (`[1,3]`):

   - We check if the new interval `[2,5]` ends before this interval starts (`5 < 1`). False.
   - We check if the new interval starts after this interval ends (`2 > 3`). False.
   - Since there is an overlap, we merge the intervals: `[min(2,1), max(5,3)] = [1,5]`.
   - `newInterval` is now `[1,5]`.

2. **Second Interval** (`[4,6]`):

   - We check if the new interval `[1,5]` ends before this interval starts (`5 < 4`). False.
   - We check if the new interval starts after this interval ends (`1 > 6`). False.
   - There is an overlap again, so we merge the intervals: `[min(1,4), max(5,6)] = [1,6]`.
   - `newInterval` is now `[1,6]`.

3. No more intervals left, so we append the final `newInterval` `[1,6]` to the result.

4. **Result**:

   - The final `res` is `[[1,6]]`.

### Time Complexity:

- The algorithm iterates through the list of intervals once, performing constant time checks and operations for each interval.
- **Time complexity**: `O(n)`, where `n` is the number of intervals.

### Space Complexity:

- We only use extra space for storing the result, which requires space proportional to the number of intervals.
- **Space complexity**: `O(n)`.

---

---

## 02. Merge Intervals

[Leetcode Problem URL](https://leetcode.com/problems/merge-intervals/description/)

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

```bash
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

```bash
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

### Explanation

To solve the problem efficiently, I've used the following approach:

1. **Sorting the intervals**:

   - The intervals are first sorted based on their starting time. This ensures that we process the intervals in the correct order.

2. **Iterating through intervals**:

   - Start with the first interval and compare it with the next interval. If the intervals overlap, merge them by updating the end time of the first interval.
   - If they do not overlap, add the interval to the result and move to the next.

3. **Handling overlaps**:

   - Overlapping intervals are merged by taking the maximum of the end times of the overlapping intervals.

4. **Final result**:

   - The result is a list of merged, non-overlapping intervals.

#### Why this approach?

This approach ensures that:

- The intervals are processed in order, which simplifies the merging process.
- Each interval is checked only once, making the solution efficient.

#### Example Walkthrough:

Let’s go through the steps with an example `intervals = [[1,3],[2,6],[8,10],[15,18]]`:

1. **Step 1: Sort the intervals**

   - Sorted intervals: `[[1,3], [2,6], [8,10], [15,18]]`

2. **Step 2: Initialize the output with the first interval**

   - `output = [[1,3]]`

3. **Step 3: Iterate through the sorted intervals**

   1. Compare `current = [2,6]` with `lastInterval = [1,3]`:

      - `current[0] <= lastInterval[1]` (2 ≤ 3), so they overlap.
      - Merge intervals: Update `lastInterval` to `[1,6]` using `max(lastEnd, end)`.
      - Why use `max(lastEnd, end)`? Consider intervals like `[1,5]` and `[2,4]`. Without using `max(lastEnd, end)`, the end of the merged interval might incorrectly become `4` instead of the correct value `5`.
      - Updated `output = [[1,6]]`.

   2. Compare `current = [8,10]` with `lastInterval = [1,6]`:

      - `current[0] > lastInterval[1]` (8 > 6), so they do not overlap.
      - Add `current` to output: `output = [[1,6], [8,10]]`.

   3. Compare `current = [15,18]` with `lastInterval = [8,10]`:
      - `current[0] > lastInterval[1]` (15 > 10), so they do not overlap.
      - Add `current` to output: `output = [[1,6], [8,10], [15,18]]`.

#### Final Output:

```bash
[[1,6],[8,10],[15,18]]
```

#### Time Complexity:

- **Sorting**: The sorting step takes $O(n \log n)$, where $n$ is the number of intervals.
- **Iteration**: We iterate through the intervals once, which takes $O(n)$.
- **Overall**: $O(n \log n)$, dominated by the sorting step.

#### Space Complexity:

- The algorithm uses $O(1)$ additional space, as the merging is done in place using the output list.

#### Why This Approach is Efficient

1. **Sorting ensures simplicity**:

   - By sorting the intervals, we only need to compare adjacent intervals, reducing complexity.

2. **Efficient merging**:

   - Each interval is processed once, and overlaps are resolved immediately.

3. **Scalability**:
   - This approach works well for a large number of intervals due to its $O(n \log n)$ complexity.

---

---

## 03. Non-overlapping Intervals

[Leetcode Problem URL](https://leetcode.com/problems/non-overlapping-intervals/)

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, `[1, 2]` and `[2, 3]` are non-overlapping.

```bash
Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

```bash
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
```

```bash
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

### Explanation

#### **Approach: Greedy Algorithm**

A **greedy** approach is well-suited for this problem because our goal is to remove **the fewest intervals possible** while ensuring the remaining intervals are non-overlapping.

By **sorting intervals by their start time** and iterating through them, we can always make the optimal decision at each step—either **keeping** an interval or **removing** it based on overlap conditions.

1. **Step 1: Sort Intervals**

   - We first **sort** the intervals **by their start time**. This ensures that we process intervals in a left-to-right manner, allowing us to track overlapping intervals effectively.

2. **Step 2: Iterate Through the Sorted Intervals**

   - We keep track of the `prevEnd`, which represents the **end of the last non-overlapping interval**.
   - As we iterate through the intervals:
   - **If the current interval starts after or at `prevEnd`**, it means there's no overlap, so we update `prevEnd`.
   - **If the current interval starts before `prevEnd`**, there is an overlap. In this case, we increment the `result` (since one interval must be removed), and we update `prevEnd` to the **smaller** `end` value to minimize overlap.

#### **Example Walkthrough**

Let’s take an example to understand the step-by-step execution of our approach.

1. **Example Input**

   ```bash
   intervals = [[1,3],[2,6],[8,10],[15,18]]
   ```

2. **Step 1: Sort Intervals**

   - Sorted intervals (by start time):

     ```bash
     [[1,3], [2,6], [8,10], [15,18]]
     ```

3. **Step 2: Initialize Variables**

   - `prevEnd = 3` (end of first interval)
   - `result = 0` (no intervals removed yet)

4. **Step 3: Iterate Through the Intervals**

   1. **Compare `[2,6]` with `prevEnd = 3`**

      - Overlapping (`2 < 3`)
      - We remove one interval and update `prevEnd = min(6, 3) = 3`
      - **result = 1**

   2. **Compare `[8,10]` with `prevEnd = 3`**

      - No overlap (`8 >= 3`), update `prevEnd = 10`
      - **result = 1**

   3. **Compare `[15,18]` with `prevEnd = 10`**
      - No overlap (`15 >= 10`), update `prevEnd = 18`

   - **result = 1**

5. **Final Output**

   ```bash
   Output: 1
   ```

#### **Time and Space Complexity Analysis**

1. **Time Complexity**

   - **Sorting the intervals** takes **O(n log n)**.
   - **Iterating through the intervals** takes **O(n)**.
   - **Overall Complexity:** **O(n log n) + O(n) = O(n log n)**.

2. **Space Complexity**

   - We only use a few extra variables (`prevEnd`, `result`), making the space complexity **O(1)** (constant extra space).

#### **Why This Approach?**

1. **Why Sorting by Start Time?**

   Sorting helps in processing the intervals in a structured order, making it easier to track and handle overlaps efficiently.

2. **Why Keeping the Interval with the Smallest End Time?**

   When two intervals overlap, removing the one with the larger end time ensures that we minimize future overlaps.

3. **Why is this Greedy Approach Optimal?**

   The **greedy choice** ensures that at each step, we are keeping the non-overlapping intervals while **minimizing removals**, leading to the most optimal solution.

---

---

## 04. Meeting Rooms

[Leetcode Problem URL](https://leetcode.com/problems/meeting-rooms/description/)

Given an array of meeting time interval objects consisting of start and end times `[[start_1,end_1],[start_2,end_2],...] (start_i < end_i)`, determine if a person could add all meetings to their schedule without any conflicts.

```bash
Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
```

```bash
Example 2:

Input: intervals = [(5,8),(9,15)]
Output: true
```

### Explanation

To solve this problem, we need to determine if there are any overlapping intervals in the given list of meeting times. If any two intervals overlap, it means the person cannot attend all meetings without conflicts.

#### Why This Approach?

1. **Sorting by Start Time**: By sorting the intervals based on their start time, we can easily check if the next meeting starts before the previous one ends. This is the key to identifying overlaps.

2. **Single Pass Through Intervals**: After sorting, we only need to traverse the list once to check for overlaps. This makes the solution efficient.

#### Step-by-Step Explanation

1. **Sort Intervals**: First, sort the intervals based on their start time. This allows us to compare each meeting with the next one in a linear fashion.

2. **Check for Overlaps**: Iterate through the sorted intervals and check if the current meeting starts before the previous meeting ends. If it does, there's a conflict.

3. **Return Result**: If no conflicts are found after traversing the entire list, return `true`. Otherwise, return `false`.

#### Example Walkthrough

Let's walk through **Example 1** step by step:

**Input**: `intervals = [(0,30),(5,10),(15,20)]`

1. **Sort Intervals**:

   - The intervals are already sorted by start time: `[(0,30),(5,10),(15,20)]`.

2. **Initialize**:

   - Set `prevEnd = intervals[0].end = 30`.

3. **Iterate Through Intervals From 1st Indext to End**:

   - **Second Interval**: `(5,10)`
     - Check if `5 < 30` (start of current interval < end of previous interval).
     - Since `5 < 30`, there's a conflict. Return `false`.

4. **Output**: `false`

Now, let's walk through **Example 2**:

**Input**: `intervals = [(5,8),(9,15)]`

1. **Sort Intervals**:

   - The intervals are already sorted by start time: `[(5,8),(9,15)]`.

2. **Initialize**:

   - Set `prevEnd = intervals[0].end = 8`.

3. **Iterate Through Intervals From 1st Indext to End**:

   - **Second Interval**: `(9,15)`
     - Check if `9 < 8` (start of current interval < end of previous interval).
     - Since `9 >= 8`, there's no conflict. Update `prevEnd = 15`.

4. **No More Intervals**:

   - Since no conflicts were found, return `true`.

5. **Output**: `true`

#### Time and Space Complexity

1. Time Complexity

   - **Sorting**: Sorting the intervals takes `O(n log n)`, where `n` is the number of intervals.
   - **Traversal**: After sorting, we traverse the list once, which takes `O(n)`.
   - **Overall Time Complexity**: `O(n log n)`.

2. Space Complexity

   - **Sorting**: Depending on the sorting algorithm, the space complexity can be `O(1)` (in-place sorting) or `O(n)` (if additional space is used).
   - **Traversal**: We use a constant amount of extra space (`prevEnd`).
   - **Overall Space Complexity**: `O(1)` or `O(n)` depending on the sorting implementation.

#### Why This Approach is Efficient

1. **Optimal Sorting**: Sorting the intervals by start time allows us to check for overlaps in a single pass, making the solution efficient.
2. **No Nested Loops**: Unlike a brute-force approach that compares every pair of intervals (which would take $O(n^2)$), this approach avoids nested loops by leveraging sorting.
3. **Scalability**: This solution scales well for large inputs due to its $O(n \ log \ n)$ time complexity.

---

---

## 05. Meeting Rooms II

[Leetcode Problem URL](https://leetcode.com/problems/meeting-rooms-ii/description/)

Given an array of meeting time interval objects consisting of start and end times `[[start_1,end_1],[start_2,end_2],...] (start_i < end_i)`, find the minimum number of days required to schedule all meetings without any conflicts.

```bash
Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)
```

```bash
Example 2:

Input: intervals = [(4,9)]
Output: 1
```

### Explanation

To solve this problem, we need to determine the **maximum number of overlapping meetings** at any point in time. This maximum number represents the minimum number of rooms required.

#### Why This Approach?

1. **Sorting Start and End Times**: By sorting the start and end times separately, we can efficiently track the number of overlapping meetings using a two-pointer technique.

2. **Simulating Meeting Overlaps**: We simulate the process of meetings starting and ending, keeping track of the number of active meetings at any given time.

3. **Efficient and Scalable**: This approach avoids nested loops and works in `O(n log n)` time, making it suitable for large inputs.

#### Step 1: Sort Start and End Times

- Extract and sort the start times of all intervals.
- Extract and sort the end times of all intervals.

#### Step 2: Use Two Pointers to Track Overlaps

- Initialize two pointers, `s` (for start times) and `e` (for end times).
- Initialize `count` to track the number of active meetings and `result` to store the maximum number of active meetings at any point.

#### Step 3: Traverse Through Intervals

- Compare the current start time (`start[s]`) with the current end time (`end[e]`):
- If `start[s] < end[e]`, it means a new meeting has started before the previous one ended. Increment the `count` and move the start pointer (`s++`).
- If `start[s] >= end[e]`, it means a meeting has ended. Decrement the `count` and move the end pointer (`e++`).
- Update `result` with the maximum value of `count` at each step.

#### Step 4: Return the Result

- The value of `result` at the end of the traversal represents the minimum number of rooms required.

#### Example Walkthrough

Let’s walk through **Example 1** step by step:

1. **Input**: `intervals = [(0,40),(5,10),(15,20)]`

1. **Sort Start and End Times**:

   - Start times: `[0, 5, 15]`
   - End times: `[10, 20, 40]`

1. **Initialize**:

   - `s = 0`, `e = 0`
   - `count = 0`, `result = 0`

1. **Traverse Through Intervals**:

   - **First Comparison**: `start[0] = 0` vs `end[0] = 10`
     - Since `0 < 10`, a new meeting starts. Increment `count` to `1`.
     - Update `result = max(0, 1) = 1`.
     - Move start pointer: `s = 1`.
   - **Second Comparison**: `start[1] = 5` vs `end[0] = 10`
     - Since `5 < 10`, another meeting starts. Increment `count` to `2`.
     - Update `result = max(1, 2) = 2`.
     - Move start pointer: `s = 2`.
   - **Third Comparison**: `start[2] = 15` vs `end[0] = 10`
     - Since `15 >= 10`, a meeting ends. Decrement `count` to `1`.
     - Update `result = max(2, 1) = 2`.
     - Move end pointer: `e = 1`.
   - **Fourth Comparison**: `start[2] = 15` vs `end[1] = 20`
     - Since `15 < 20`, a new meeting starts. Increment `count` to `2`.
     - Update `result = max(2, 2) = 2`.
     - Move start pointer: `s = 3`.
   - **Fifth Comparison**: `start[3]` (out of bounds) vs `end[1] = 20`
     - Since all start times are processed, exit the loop.

1. **Result**:

   - The maximum number of overlapping meetings is `2`, so the minimum number of rooms required is `2`.

1. **Output**: `2`

#### Time and Space Complexity

1. Time Complexity

   - **Sorting**: Sorting the start and end times takes `O(n log n)` each, where `n` is the number of intervals.
   - **Traversal**: The two-pointer traversal takes `O(n)`.
   - **Overall Time Complexity**: `O(n log n)`.

2. Space Complexity

   - **Sorting**: Sorting requires `O(n)` space to store the start and end times.
   - **Pointers and Counters**: Constant space is used for pointers and counters.
   - **Overall Space Complexity**: `O(n)`.

#### Why This Approach is Efficient

1. **Optimal Sorting**: Sorting the start and end times separately allows us to efficiently track overlapping meetings.
2. **Single Traversal**: The two-pointer technique ensures that we only traverse the list once, making the solution scalable.
3. **Avoids Nested Loops**: Unlike a brute-force approach that compares every pair of intervals (which would take `O(n^2)`), this approach avoids nested loops by leveraging sorting and two pointers.

---

---
