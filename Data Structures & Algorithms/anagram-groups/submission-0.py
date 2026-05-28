class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        my_dict = {}

        #I am trying to group anagrams together
        #Anagrams are words that have the same letters but not necessarily
        #in the same locations or indexes
        #so words that have the same letters
        #I can use a loop to go through every string and check if when sorted
        #they equal another string in the string, and when it gets to the end of the
        ##string it just extends itself to the end of the result list
        #But that may not be very efficient.
        #another way could be with a hashmap.
        #With a hashmap I can sort them out, when they are sorted but the issue 
        #I face is what will the keys be has it has to be unique
        #what if the keys are the sorted out strings.
        #So I compare the string and the key and if the sorted out string
        #matches the key then I can add it to the key's values
        
        for i in strs:
            if tuple(sorted(i)) not in my_dict:
                my_dict[tuple(sorted(i))] = [i]
            else:
                my_dict[tuple(sorted(i))].append((i))
        
        for value in my_dict.values():
            result.append(value)

        return result




