class Solution:

    def recoverSortedArray(self, nums):
        self.quicksort(nums, 0, len(nums)-1)
        return nums
        
    def quicksort(self, nums, first, last):
        if first < last:
            pivot = nums[first]
            leftptr = first+1 
            rightptr = last
            
            while True: 
                while leftptr <= rightptr and nums[leftptr] <= pivot:
                    leftptr += 1 
                    
                while nums[rightptr] >= pivot and rightptr >= leftptr :
                    rightptr -= 1
                
                if leftptr < rightptr:
                    nums[leftptr], nums[rightptr] = nums[rightptr], nums[leftptr]
                else:
                    break
                    
            nums[first], nums[rightptr] = nums[rightptr], nums[first]
            
            self.quicksort(nums, first, rightptr-1)
            self.quicksort(nums, rightptr+1, last)

