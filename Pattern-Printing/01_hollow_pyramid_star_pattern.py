class Solution:
   def hollow_pyramid_method1(self, rows):
      if rows < 5:
         print("Value of rows should be greater than or equal to 5 to print hollow star pattern")
         return

      total_width = 2 * rows - 1
      mid = total_width // 2
      cur_row = 0

      while cur_row < rows:
         line = [' '] * total_width

         if cur_row == 0:
               line[mid] = '*'
         elif cur_row == rows - 1:
               # Last row: all stars
               for i in range(total_width):
                  line[i] = '*'
         else:
               left = mid - cur_row
               right = mid + cur_row
               line[left] = '*'
               line[right] = '*'

         print(''.join(line))
         cur_row += 1


if __name__ == "__main__":

   obj = Solution()
   num_rows = int(input("Enter the number of rows for the hollow pyramid: "))
   obj.hollow_pyramid_method1(num_rows)