class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        result = []
        final_res = []

        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        
        for key, value in my_dict.items():
            result.append((key, value))
        
        result.sort(key = lambda x: x[1], reverse = True)
        
        for i in range(k):
            final_res.append(result[i][0])
        return final_res
