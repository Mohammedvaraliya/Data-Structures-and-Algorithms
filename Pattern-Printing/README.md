# Pattern Printing

## 01. Hollow Pyramid Star Pattern

Design a program that prints a hollow pyramid made of `*` (asterisk) characters.

- Input: an integer `rows` representing the height of the pyramid.
- Output: printed hollow pyramid pattern of height `rows`.

Constraints / Notes:

- This implementation expects `rows >= 5` (the provided implementation prints a helpful message for `rows < 5`).
- Pyramid width (number of columns) = `2 * rows - 1`.
- The pyramid is symmetric and centered horizontally.

```bash
Example 1:
Input:
rows = 5

Output:
    *
   * *
  *   *
 *     *
*********
```

```bash
Example 2:
Input:
rows = 6

Output:
     *
    * *
   *   *
  *     *
 *       *
***********
```

#### Explanation

1. **What the code does (high level)**

   - For each row from top (`cur_row = 0`) to bottom (`cur_row = rows - 1`), we create a line of length `total_width = 2 * rows - 1`.
   - Place `'*'` characters at the appropriate positions:

     - Top row: single `'*'` at the center.
     - Middle rows: two `'*'` at symmetric positions `left = mid - cur_row` and `right = mid + cur_row`.
     - Bottom row: all characters are `'*'`.

   - Print the constructed line.

2. **Why this approach**

   - This is a straightforward, constructive approach that directly computes the star indices for each row. It is intuitive and simple to implement and reason about.
   - It keeps the pyramid symmetric by computing a fixed `mid` index and using offsets from that center.

3. **What pattern/technique this follows**

   - This is a **constructive pattern** / direct simulation: compute the output row-by-row using index math. It relies on symmetry and index arithmetic rather than recursion or advanced data structures.

4. **Why it is clear / elegant**

   - The logic is explicit: center position, left/right offsets, and a clear rule for the last row.
   - Using a mutable list (`line = [' '] * total_width`) makes it easy to place characters at specific indices and then join into a string for printing.

#### Step-by-Step Walkthrough (detailed)

1. Use the concrete example `rows = 6` (chosen because the code requests `rows >= 5`).

   - `total_width = 2 * rows - 1 = 11`
   - `mid = total_width // 2 = 5`
   - `cur_row` ranges `0..5` inclusive.

   | cur_row | left index computed | right index computed |                Action                 | Final line (length 11) |
   | :-----: | :-----------------: | :------------------: | :-----------------------------------: | :--------------------: |
   |    0    |          —          |          —           |       place 1 star at `mid = 5`       |    `'     *     '`     |
   |    1    |     `mid-1 = 4`     |     `mid+1 = 6`      |    place stars at indices 4 and 6     |    `'    * *    '`     |
   |    2    |     `mid-2 = 3`     |     `mid+2 = 7`      |    place stars at indices 3 and 7     |    `'   *   *   '`     |
   |    3    |     `mid-3 = 2`     |     `mid+3 = 8`      |    place stars at indices 2 and 8     |    `'  *     *  '`     |
   |    4    |     `mid-4 = 1`     |     `mid+4 = 9`      |    place stars at indices 1 and 9     |    `' *       * '`     |
   |    5    |          —          |          —           | last row: fill all positions with `*` |    `'***********'`     |

2. Detailed iteration (how the code builds each line):

   1. **cur_row = 0**

      - `line = [' '] * 11`
      - `line[5] = '*'`
      - `print(''.join(line))` → `*`

   2. **cur_row = 1**

      - `line = [' '] * 11`
      - `left = 4`, `right = 6`
      - `line[4] = '*'`, `line[6] = '*'`
      - `print` → `* *`

   3. **cur_row = 2**

      - `left = 3`, `right = 7`
      - `line[3] = '*'`, `line[7] = '*'`
      - `print` → `*   *`

   4. **cur_row = 3**

      - `left = 2`, `right = 8`
      - `print` → `*     *`

   5. **cur_row = 4**

      - `left = 1`, `right = 9`
      - `print` → `*       *`

   6. **cur_row = 5** (last row)

3. set every position to `'*'`

4. `print` → `***********`

5. That produces the hollow pyramid illustrated above.

   ```bash
       *
      * *
     *   *
    *     *
   *********
   ```

#### Implementation Notes and Variants

1. **Minimum rows check**

   - The provided code prints a message if `rows < 5`. You can remove or lower that threshold if you want to support smaller pyramids (e.g., `rows >= 1`).

2. **Memory / building lines**

   - The code uses `line = [' '] * total_width` and assigns characters by index, then `''.join(line)`. This is convenient and easy to read.
   - Alternative: build strings using concatenation or formatted printing (but repeated concatenation can be less efficient).

3. **Alternate printing approach**

   - For very large `rows`, you might prefer streaming characters to output directly rather than building full lists, but for typical pattern-printing tasks this approach is fine.

#### Time & Space Complexity

| Resource |         Complexity         | Reason                                                                                                                                                        |
| -------: | :------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|     Time | O(rows × width) = O(rows²) | For each row (rows), we construct a line of length `total_width = 2*rows-1` and perform constant-time assignments and a join. So overall quadratic in `rows`. |
|    Space |     O(width) = O(rows)     | Temporary `line` list of length `2*rows-1` is used for each row.                                                                                              |

#### Tips for Readers

1. **Indexing intuition**

   - Think of the pyramid as a fixed-width line (width = `2*rows-1`) and a center (`mid`). For row `r` (0-based), the stars are at `mid - r` and `mid + r` (except top and bottom special cases).

2. **Generalizing**

   - You can adapt this to print filled pyramids, inverted pyramids, or pyramids with different characters by changing the placement logic and characters.

3. **Edge cases**

   - For `rows = 1` or `rows = 2` you must decide what behaviour you want — the current code enforces `rows >= 5`. If you want more general behavior, change or remove that guard.

---

---
