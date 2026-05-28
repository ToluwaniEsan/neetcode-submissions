class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        l = 0
        n = len(nums)

        while l < n:
            multiply = 1
            j = 0

            while j < n:
                if j != l:
                    multiply *= nums[j]
                j+=1
            
            output.append(multiply)
            l += 1
        return output

#let's get my though in order. I want to loop over the list once, 
#completing every multiplication with two pointers. so the idea is to 
#have one pointer kinda hide the the element I'm on so the other one goes ahead adding the 
#other elements into like a multiplication bowl of some sort, then the result would be appended into the 
#output list
#What I am seeing for this is usig a loop. I though of using a while loop so 
#it doesn't go over everything for every iteration.
#with a while loop I can select one, multiply the rest and do that for everything
#all in one iteration.
#how to implement it is becoming an issue for me now.

