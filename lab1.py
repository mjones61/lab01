# Matthew Jones
# CPE 202-01
# 4/5/19

def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   if len(int_list) == 0:
      return None
   maximum = int_list[0]
   for x in int_list:
      if maximum < x:
         maximum = x
   return (maximum)

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   if len(int_list) == 0:
      return []
   return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
      raise ValueError
   if len(int_list) == 0:
      return None
   if high < low:
      raise ValueError('Check your bounds')
   mid = (low + high) // 2
   if high <= low and int_list[high] != target:
      return None
   if int_list[mid] == target:
      return mid
   elif target > int_list[mid]:
      return bin_search(target, mid + 1, high, int_list)
   elif target < int_list[mid]:
      return bin_search(target, low, mid - 1, int_list)
