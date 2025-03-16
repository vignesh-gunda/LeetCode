# Best Case solution

class TwoSumSolution:
  def best_case(self, nums, target):
    """
    Best Case solution using a Hash map:
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    nums_array = {}
    for i , num in enumerate(nums):
      complement = target - num
      if complement in nums_array:
        return [nums_array[complement], i]
      nums_array[num] = i
    return []
  
  def worst_case(self, nums, target):
    """
    Worst case solution using brute force:
    Time complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if (nums[i] + nums[j] == target):
          return [i, j]
    
    return []

def main():

  nums = [2,7,11,19]
  target = 9
  
  Solution = TwoSumSolution()

  best_case_solution = Solution.best_case(nums, target)
  print(f"Best case solution using Hashmaps:{best_case_solution}")

  worst_case_solution = Solution.worst_case(nums, target)
  print(f"Worst case solution using Brute Force:{worst_case_solution}")

if __name__ == "__main__":
  main()