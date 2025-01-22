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
